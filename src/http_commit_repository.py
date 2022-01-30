import json
import urllib.request

from commit_repository import CommitRepository
from config_loader import ConfigurationLoader

class HttpCommitRepository(CommitRepository):
  def __init__(self, config_file_path="http_commit_repository.cfg"):
    config_loader = ConfigurationLoader(config_file_path)

    configuration = config_loader.load()

    self.destination_url = configuration["destination_url"]

  def save(self, commit_details):
    parameters = json.dumps(commit_details).encode('utf8')

    request = urllib.request.Request(self.destination_url, data=parameters, headers={'content-type': 'application/json'})

    response = None

    try:
    
      response = urllib.request.urlopen(request)

    except (Exception) as error:
      display_error_message("OS error: {0}".format(error))

    if(response is not None):
      raw_data = response.read()
      encoding = response.info().get_content_charset('utf8')  # JSON default
      
      message = json.loads(raw_data.decode(encoding))

      if(message["code"] != 0):
        self.display_error_message("Remote error: {0}".format(message["message"]))

  def display_error_message(self, message):
    print("ERROR posting the commit details to " + self.destination_url)
    print("NOTE: This does not affect your commit, just the reporting of it")

