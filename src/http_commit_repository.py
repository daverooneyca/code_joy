import json
import urllib.request

from commit_repository import CommitRepository

class HttpCommitRepository(CommitRepository):
  def __init__(self, destination_url="http://127.0.0.1:5000/commit"):
    # TODO - use a configuration file for these settings
    self.destination_url = destination_url

  def save(self, commit_details):
    parameters = json.dumps(commit_details).encode('utf8')

    request = urllib.request.Request(self.destination_url, data=parameters, headers={'content-type': 'application/json'})

    response = None

    try:
    
      response = urllib.request.urlopen(request)

    except (Exception) as error:
      print("ERROR posting the commit details to " + self.destination_url)
      print("NOTE: This does not affect your commit, just reporting of it")
      print(error)

    if(response is not None):
      print(response.read().decode())
