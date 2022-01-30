# Copyright © 2022 Dave Rooney
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
