# This Python file uses the following encoding: utf-8
import sys
import os
import pandas
import paho.mqtt.client as mqtt
from PyQt6.QtCore import QThread, pyqtSignal


class MqttClient(QThread):

    connected = pyqtSignal()

    def __init__(self, ip, port, uuid=""):
        super().__init__()
        self.ip = ip
        self.port = port
        self.uuid = uuid
        self.__isConnected = False
        self.topicsToSubscribe = []
        self.client = mqtt.Client(uuid)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe

    def run(self):
        self.client.connect(self.ip, self.port)
        self.client.loop_start()

    def isConnected(self):
        return self.__isConnected

    def on_connect(self, client, userdata, flags, rc):
        print("Connected : {}".format(rc))
        self.connected.emit()
        self.__isConnected = True
        for topic in self.topicsToSubscribe:
            self.client.subscribe(topic)

    def on_disconnect(self, client, userdata, rc):
        print('disconnected from server')
        self.__isConnected = False

    def on_message(self, client, userdata, msg):
        print('Got a message!')
        print(msg.topic)
        print(msg.payload)

    def on_subscribe(self, client, userdata, mid, granted_qos):
        if granted_qos[0] <= 2:
            print('subscribed to topic')
        else:
            print('subscription failed!')

        print(mid)
        print(granted_qos)

    def subscribe(self, topic):
        if self.__isConnected:
            self.client.subscribe(topic)
        self.topicsToSubscribe.append(topic)

    def publish(self, topic, data, qos=0, retain=False):
        self.client.publish(topic, data, qos, retain)
