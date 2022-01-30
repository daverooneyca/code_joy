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
