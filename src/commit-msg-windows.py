#!%userprofile%\AppData\Local\Microsoft\WindowsApps\python.exe

import sys
from commit_message_handler import CommitMessageHandler

def main():
   handler = CommitMessageHandler()

   commit_file = sys.argv[1]
   
   result = handler.process_rating_in(commit_file)

   sys.exit(result.value)

if __name__ == '__main__':
   main()
