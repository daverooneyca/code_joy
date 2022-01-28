#!/usr/bin/env python

#from post_commit_handler import PostCommitHandler
from noop_commit_handler import NoopCommitHandler
from http_commit_repository import HttpCommitRepository

if __name__ == '__main__':
   #repository = HttpCommitRepository()
   repository = NoopCommitRepository()

   handler = PostCommitHandler(repository)
   
   handler.execute()
