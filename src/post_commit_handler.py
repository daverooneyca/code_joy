import sys

from pydoc import locate
from commit_repository import CommitRepository
from commit_details_builder import CommitDetailsBuilder
from config_loader import ConfigurationLoader


class PostCommitHandler():
  def __init__(self, config_file="code_joy.cfg", repository_class="noop_commit_repository.NoopCommitRepository", rating_file=""):
    self.load_configuration(config_file, repository_class, rating_file)

  def execute(self):
    builder = CommitDetailsBuilder(self.rating_file)

    commit_details = builder.build()

    self.repository.save(commit_details)

  def load_configuration(self, config_file, repository_class, rating_file):
    config_loader = ConfigurationLoader(config_file)

    configuration = config_loader.load()

    if(rating_file == ""):
      self.rating_file = configuration["rating_file"]

    repository_class = configuration["commit_repository_class"]

    clazz = locate(repository_class)
    self.repository = clazz()
