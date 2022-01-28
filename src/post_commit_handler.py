import sys

from http_commit_sender import HttpCommitSender
from commit_details_builder import CommitDetailsBuilder

class PostCommitHandler():
  def __init__(self, rating_file="./rating_file", destination_url="http://127.0.0.1:5000/commit"):
    
    # TODO - use a configuration file for these settings
    self.rating_file = rating_file
    self.destination_url = destination_url

  def execute(self):
    builder = CommitDetailsBuilder(self.rating_file)

    commit_details = builder.build()

    sender = HttpCommitSender(commit_details, self.destination_url)

    sender.send()
