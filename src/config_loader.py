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
