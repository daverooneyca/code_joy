import sys

from commit_repository import CommitRepository
from commit_details_builder import CommitDetailsBuilder

class PostCommitHandler():
  def __init__(self, repository, rating_file="./rating_file"):
    
    # TODO - use a configuration file for these settings
    self.rating_file = rating_file
    self.repository = repository

  def execute(self):
    builder = CommitDetailsBuilder(self.rating_file)

    commit_details = builder.build()

    self.repository.save(commit_details)
