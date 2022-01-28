#!/usr/bin/env python

from post_commit_handler import PostCommitHandler

if __name__ == '__main__':
   repository = HttpCommitRepository(self.destination_url)

   handler = PostCommitHandler(repository)
   
   handler.execute()
