import json

class ConfigReader:

    def __init__(self, config_file):

        with open(config_file) as f:
            self._data = json.load(f)

        self._mqtt = self._data["MQTT"]
        self._cirrus = self._data["Cirrus"]
        self._layout = self._data["Layout"]

    @property
    def data(self):
        return self._data

    @property
    def mqtt(self):
        return self._mqtt

    @property
    def cirrus(self):
        return self._cirrus

    @property
    def layout(self):
        return self._layout
