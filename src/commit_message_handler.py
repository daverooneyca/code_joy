import sys
import re

from enum import Enum

class ExitCodes(Enum):
    SUCCESS = 0
    FAIL = 1

class CommitMessageHandler():
   def process_rating_in(self, commit_file):
      print("Checking commit message in {}".format(commit_file))

      content = self.read_content_from(commit_file)

      rating, content = self.extract_rating_from(content)

      if (rating == ""):
         print("Commit rejected: Message [{}] does not contain a rating between 0 and 5.".format(content))
         return ExitCodes.FAIL

      self.write_rating_file_with(rating)
      self.rewrite_commit_file_with(content, commit_file)

      return ExitCodes.SUCCESS

   def extract_rating_from(self, content):
      expression = re.compile("\-[0-5]\-")

      result = expression.search(content)

      rating = ""

      if(result):
         rating = result[0].strip("-")

      return rating, content

   def read_content_from(self, commit_file):
      with open(commit_file, 'r') as file:
         content = file.read()
         file.close()
         return content
   
   def write_rating_file_with(self, rating):
      rating_file = "./rating_file"
      with open(rating_file, 'w') as file:
         file.write(rating)
         file.close()

   def rewrite_commit_file_with(self, content, commit_file):
      stripped_content = re.sub("\-[0-5]\-", "", content).strip()

      with open(commit_file, 'w') as file:
         file.write(stripped_content)
         file.close()


if __name__ == '__main__':
   checker = CheckCommit()
   
   result = checker.check(sys.argv[1])

   sys.exit(result.value)
