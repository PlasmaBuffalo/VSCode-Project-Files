# This Python file uses the following encoding: utf-8
import sys
import os
import pandas
import paho.mqtt.client as mqtt
from PyQt6.QtCore import QThread, pyqtSignal
from getmac import get_mac_address as gma


class MqttClient(QThread):

    connected = pyqtSignal()
    #defines basic behavior for main functions 
    def __init__(self, ip, port, uuid=''):
        super().__init__()
        self.ip = ip
        self.port = port
        self.uuid: str = gma() or ''
        self.__isConnected = False
        self.topicsToSubscribe = []
        #mqtt methods
        self.client = mqtt.Client(uuid)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe

    #connects the client to the server defined by the client IP and port args on start
    def run(self):
        self.client.connect(self.ip, self.port)
        self.client.loop_start()

    #returns a boolean value indicating whether the client is connected to the server
    def isConnected(self):
        return self.__isConnected

    #on connect, subscribes client to each topic specified by the constructor
    def on_connect(self, client, userdata, flags, rc):
        print("Connected : {}".format(rc))
        self.connected.emit()
        self.__isConnected = True
        for topic in self.topicsToSubscribe:
            self.client.subscribe(topic)

    #on disconnect, prints disconnected and sets isConnected to False
    def on_disconnect(self, client, userdata, rc):
        print('disconnected from server')
        self.__isConnected = False

    #on message, prints message and payload by default
    def on_message(self, client, userdata, msg):
        print('Got a message!')
        print(msg.topic)
        print(msg.payload)

    #on subscribe, prints subscribed and prints error if otherwise
    def on_subscribe(self, client, userdata, mid, granted_qos):
        if granted_qos[0] <= 2:
            print('subscribed to topic')
        else:
            print('subscription failed!')

        print(mid)
        print(granted_qos)

    #defines subsciption behavior, will subscribe to topic if qos makes sense and appends it to subscribed topics list
    def subscribe(self, topic):
        if self.__isConnected:
            self.client.subscribe(topic)
        self.topicsToSubscribe.append(topic)

    #defines publish behavior, will publish to topic and defines some special behavior for retaining info
    def publish(self, topic, data, qos=0, retain=False):
        self.client.publish(topic, data, qos, retain)
""" 
each mqttclient has the following defined behaviors and properties: 
- ip
- port
- uuid
- __isConnected
- topicsToSubscribe
- 
"""