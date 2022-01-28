import sys
import json
import subprocess
import re

from git_command_runner import GitCommandRunner

class CommitDetailsBuilder():
  def __init__(self, rating_file, command_runner=GitCommandRunner()):
    self.commit_details = []
    self.rating_file = rating_file

    self.runner = command_runner

  def build(self):
    raw_commit = self.runner.fetch_last_commit()

    self.commit_details = json.loads(raw_commit)

    self.commit_details["branch"] = self.runner.fetch_current_branch()
    self.commit_details["files"] = self.runner.fetch_commit_files()
    self.commit_details["git_location"] = self.runner.fetch_location()
    self.commit_details["location"] = self.git_to_https_for(self.commit_details["git_location"])
    self.commit_details["rating"] = self.fetch_rating()
    self.commit_details["files"] = self.multi_line_to_array(self.runner.fetch_commit_files())

    return self.commit_details

  def fetch_rating(self):
    with open(self.rating_file, 'r') as file:
      rating = file.read()
      file.close()
      return rating

  def git_to_https_for(self, git_location):
    return re.sub(r'.*(\@|\/\/)(.*)(\:|\/)([^:\/]*)\/([^\/\.]*)\.git', r'https://\2/\4/\5/', git_location)

  def multi_line_to_array(self, lines):
    return lines.splitlines()
