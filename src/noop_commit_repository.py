import json
import urllib.request

from commit_repository import CommitRepository

class NoopCommitRepository(CommitRepository):
  def save(self, commit_details):
    # Echo the commit details to the console
    print("This is the Noop Commit Repository. This can be changed in post-commit.py")
    print(commit_details)
