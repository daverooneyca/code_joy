#!/usr/bin/env python

from post_commit_handler import PostCommitHandler

if __name__ == '__main__':
   handler = PostCommitHandler()
   
   handler.execute()
