#!%userprofile%\AppData\Local\Microsoft\WindowsApps\python.exe

from post_commit_handler import PostCommitHandler
from http_commit_repository import HttpCommitRepository

if __name__ == '__main__':
   repository = HttpCommitRepository()

   handler = PostCommitHandler(repository)
   
   handler.execute()
