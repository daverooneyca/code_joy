# Copyright © 2022 Dave Rooney
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import re

from enum import Enum

class ExitCodes(Enum):
    SUCCESS = 0
    FAIL = 1

class CommitMessageHandler():
   def __init__(self, rating_file="./rating_file"):
      self.rating_file = rating_file

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
      expression = re.compile(r"\-[0-5]\-")

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
      with open(self.rating_file, 'w') as file:
         file.write(rating)
         file.close()

   def rewrite_commit_file_with(self, content, commit_file):
      stripped_content = re.sub(r"\-[0-5]\-", "", content).strip()

      with open(commit_file, 'w') as file:
         file.write(stripped_content)
         file.close()


if __name__ == '__main__':
   checker = CheckCommit()
   
   result = checker.check(sys.argv[1])

   sys.exit(result.value)
