#!/usr/bin/env python

from post_commit_handler import PostCommitHandler

def main():
   handler = PostCommitHandler()

   handler.execute()

if __name__ == '__main__':
   main()
