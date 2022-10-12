
import json
import signal
import sys
from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer

import numpy as np
import pandas as pd
import pymysql
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication

from mqtt import MqttClient


class ChatServer(MqttClient):

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        # this is the code connecting the SQL database to the RPC server
        hostname = "PythonChatServer"
        db_user = "CS420"
        db_pswd = "CS420"
        db = "ChatLog"
        self.conn = pymysql.connect(
            host=hostname, user=db_user, password=db_pswd, database=db)
        # cursor object is needed for navigating the database
        self.cur = self.conn.cursor()

        # this is the code connecting the RPC server to the clients
        rpcServer: SimpleXMLRPCServer = SimpleXMLRPCServer(('localhost', 8000))
        rpcServer.register_instance(ChatServer())
        # response server is handled on a thread
        thread: Thread = Thread(target=rpcServer.serve_forever, args=())
        thread.start()

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


if __name__ == "__main__":

    cs = ChatServer()
    print('Pants chumd')
