
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
        db = "ChatHistory"
        self.conn = pymysql.connect(
            host=hostname, user=db_user, password=db_pswd, database=db)
        # cursor object is needed for navigating the database
        self.cur = self.conn.cursor()

    def run(self):
        # this is the code connecting the RPC server to the clients
        rpcServer: SimpleXMLRPCServer = SimpleXMLRPCServer(('localhost', 8000))
        rpcServer.register_instance(ChatServer())
        # response server is handled on a thread
        thread: Thread = Thread(target=rpcServer.serve_forever, args=())
        thread.start()
        print('im up')

    def on_message(self, client, userdata, msg):
        print('Got a message!')
        print(msg.topic)
        print(msg.payload)
        #when server gets a message on its manage channel, send the message to receiver and then log in database

    def logMessage(self, client, message):
        print()

if __name__ == "__main__":

    cs = ChatServer()
    print('Pants chumd')
    
    
    