# -*- coding:utf-8 -*-

class Hortus:

    def __init__(self, config):

        self._config_mqtt = config.mqtt
        self._config_cirrus = config.cirrus
        self._config_setup = config.setup

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_val, tb):
        pass

    def init_mqtt(self):
                  

        
    def init_cirrusClient(self):
        pass

    def run(self):
        pass

    def __str__(self):
        return "Hortus()"
