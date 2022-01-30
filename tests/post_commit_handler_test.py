import sys
import pytest

from doubles import allow

# Adds the 'src' directory to the search path for modules
sys.path.insert(0, './src/')

from post_commit_handler import PostCommitHandler
from commit_repository import CommitRepository

config_file = "./tests/code_joy.cfg"

def test_post_commit_handler():
    handler = PostCommitHandler(config_file)

    handler.execute()

class DummyCommitRepository(CommitRepository):
    def save(self, commit_details):
        print(commit_details)
