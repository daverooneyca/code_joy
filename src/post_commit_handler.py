import sys
import json
import subprocess
import re
import urllib.request

class PostCommitHandler():
  rating_file = "./rating_file"  
  destination_url = "http://127.0.0.1:5000/commit"

  def execute(self):
    commit_details = self.populate_commit_details()

    self.post_commit_to(commit_details, self.destination_url)

  def populate_commit_details(self):

    command = 'git log -1 HEAD --format=format:{\"id\":\"%H\",\"shortId\":\"%h\",\"authorName\":\"%an\",\"committerName\":\"%cn\",\"committerEmail\":\"%ce\",\"subject\":\"%s\",\"body\":\"%b\"}'
    
    result = self.run_command(command).strip()

    commit_details = json.loads(result)

    rating = self.load_rating_from(self.rating_file)

    commit_details["rating"] = rating
    commit_details["branch"] = self.run_command("git branch --show-current").strip()
    commit_details["files"] = self.multi_line_to_array(self.run_command('git diff --name-only HEAD~1'))

    git_location = self.run_command("git config --get remote.origin.url").strip()

    https_location = re.sub(r'.*(\@|\/\/)(.*)(\:|\/)([^:\/]*)\/([^\/\.]*)\.git', r'https://\2/\4/\5/', git_location)

    commit_details["git_location"] = git_location
    commit_details["location"] = https_location

    return commit_details

  def multi_line_to_array(self, lines):
    return lines.splitlines()

  def load_rating_from(self, rating_file):
    with open(rating_file, 'r') as file:
      rating = file.read()
      file.close()
      return rating

  def post_commit_to(self, details, destination_url):
    params = json.dumps(details).encode('utf8')

    req = urllib.request.Request(destination_url, data=params, headers={'content-type': 'application/json'})

    response = None

    try:
    
      response = urllib.request.urlopen(req)

    except (Exception) as error:
      print("ERROR posting the commit details to " + destination_url)
      print("NOTE: This does not affect your commit, just reporting of it")
      print(error)

      if(response):
        print(response)

  def run_command(self, command):
    words = command.split(" ")

    result = subprocess.run(words, capture_output=True, text=True, encoding="utf-8")

    return result.stdout
