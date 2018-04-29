import json

class ConfigReader:

    def __init__(self, config_file):

       with open(config_file) as f:
           self._data = json.load(f)


    @property
    def data(self):
        return self._data
