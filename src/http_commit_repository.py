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
      self.display_error_message("ERROR: {0}".format(error))

    if(response is not None):
      raw_data = response.read()
      encoding = response.info().get_content_charset('utf8')  # JSON default
      
      message = json.loads(raw_data.decode(encoding))

      if(message["code"] != 0):
        self.display_error_message("Remote error: {0}".format(message["message"]))

  def display_error_message(self, message):
    print("ERROR posting the commit details to " + self.destination_url)
    print("NOTE: This does not affect your commit, just the reporting of it")

