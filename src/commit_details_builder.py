import sys
import json
import subprocess
import re

class CommitDetailsBuilder():
  def __init__(self, rating_file):
    self.commit_details = []
    self.rating_file = rating_file

  def build(self):
    self.commit_details = self.fetch_last_commit()

    self.commit_details["rating"] = self.fetch_rating()
    self.commit_details["branch"] = self.fetch_current_branch()
    self.commit_details["files"] = self.fetch_commit_files()

    self.commit_details["git_location"], self.commit_details["location"] = self.fetch_location()

    return self.commit_details

  def fetch_last_commit(self):
    # TODO - extract the Git specific code into a pluggable class
    # TODO - Use a configuration file for this command in case the syntax changes with Git versions
    command = 'git log -1 HEAD --format=format:{\"id\":\"%H\",\"shortId\":\"%h\",\"authorName\":\"%an\",\"committerName\":\"%cn\",\"committerEmail\":\"%ce\",\"subject\":\"%s\",\"body\":\"%b\"}'
    
    result = self.run_command(command).strip()

    print(result)

    commit_details = json.loads(result)

    return commit_details

  def fetch_rating(self):
    with open(self.rating_file, 'r') as file:
      rating = file.read()
      file.close()
      return rating

  def fetch_location(self):
    # TODO - Use a configuration file for this command in case the syntax changes with Git versions
    git_location = self.run_command("git config --get remote.origin.url").strip()

    https_location = self.git_to_https_for(git_location)

    return git_location, https_location

  def fetch_current_branch(self):
    # TODO - Use a configuration file for this command in case the syntax changes with Git versions
    return self.run_command("git branch --show-current").strip()

  def fetch_commit_files(self):
    # TODO - Use a configuration file for this command in case the syntax changes with Git versions
    return self.multi_line_to_array(self.run_command('git diff --name-only HEAD~1'))

  def run_command(self, command):
    words = command.split(" ")

    result = subprocess.run(words, capture_output=True, text=True, encoding="utf-8")

    return result.stdout

  def git_to_https_for(self, git_location):
    return re.sub(r'.*(\@|\/\/)(.*)(\:|\/)([^:\/]*)\/([^\/\.]*)\.git', r'https://\2/\4/\5/', git_location)

  def multi_line_to_array(self, lines):
    return lines.splitlines()
