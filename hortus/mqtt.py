#!/usr/bin/env python
# -*- coding:utf-8-*-
from logger import Logger
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import logging


class Subscriber(Logger):
    

    def __init__(self, namespace, client, on_message=None):
        #change default logging from INFO to DEBUG
        Logger.__init__(self, level=logging.DEBUG)
            
        client.on_connect = self._on_connect
        client.on_message = on_message or self._on_message

        self._namespace = namespace
        
    def _on_connect(self, client, userdata, flags, rc):
        
        if rc == 0:
            self.log.info("Successfully connected to {}".format(client.socket().getpeername()[0]))
            client.subscribe(self._namespace)
        else :
            self.log.warn("Failled to connect to {}. Error {}".format(client.socket().getpeername()[0], str(rc)))

    def _on_message(self, client, userdata, msg):

        self.debug("Message recieved on namespace{}".format(self._namespace)) 

    def subscribe(self, namespace, callback):

        client.message_callback_add(namespace, callback)




if __name__ == "__main__":

    client = mqtt.Client()
    subscriber = Subscriber("hello/#", client)
    client.connect("127.0.0.1", 1883, 60)
    client.loop(timeout=2.0)    
