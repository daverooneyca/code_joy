#!%userprofile%\AppData\Local\Microsoft\WindowsApps\python.exe

from post_commit_handler import PostCommitHandler

if __name__ == '__main__':
   handler = PostCommitHandler()
   
   handler.execute()
