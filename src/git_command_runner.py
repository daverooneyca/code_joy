import sys
import json
import subprocess
import re

class GitCommandRunner():
  commands = {
    "last_commit": 'git log -1 HEAD --format=format:{"id":"%H","shortId":"%h","authorName":"%an","committerName":"%cn","committerEmail":"%ce","subject":"%s","body":"%b"}',
    "repo_location": "git config --get remote.origin.url",
    "current_branch": "git branch --show-current",
    "commit_files": "git diff --name-only HEAD~1"
  }

  def fetch_last_commit(self):
    return self.run_command("last_commit")

  def fetch_location(self):
    return self.run_command("repo_location")

  def fetch_current_branch(self):
    return self.run_command("current_branch")

  def fetch_commit_files(self):
    return self.run_command("commit_files")

  def run_command(self, command_key):
    command = self.commands[command_key]

    words = command.split(" ")

    result = subprocess.run(words, capture_output=True, text=True, encoding="utf-8")

    return result.stdout.strip()
