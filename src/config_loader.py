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

import os
import json

class ConfigurationLoader():
   def __init__(self, config_file):
      self.config_file = config_file

   def load(self):
      config = {}

      try:
         raw_data = self.read_config_file()

         config = json.loads(raw_data)

      except (Exception) as error:
         print("ERROR: Invalid configuration file: {0}\nError: {1}".format(self.config_file, error))         

      return config

   def read_config_file(self):
      # If the config file doesn't exist in the current working directory, 
      # add the path in which this file lives

      if(not os.path.isfile(self.config_file)):
         self.config_file = os.path.join(os.path.dirname(__file__), self.config_file)

      print(self.config_file)

      with open(self.config_file, 'r') as file:
         content = file.read()
         file.close()
         return content
