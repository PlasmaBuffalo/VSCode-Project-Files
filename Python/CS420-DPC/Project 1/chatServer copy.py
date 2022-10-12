
import signal
import json
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

    def __init__(self):
        hostname = "chum"
        db_user = "CS420"
        db_pswd = "CS420"
        self.conn = pymysql.connect(
            host=hostname, user=db_user, password=db_pswd)
        # Create a cursor object. Allows you to navigate the DB
        self.cur = self.conn.cursor()


if __name__ == "__main__":

    # RPC server communicates to clients
    rpcServer = SimpleXMLRPCServer(('localhost', 8000))
    rpcServer.register_instance(ChatServer())

    thread = Thread(target=rpcServer.serve_forever, args=())
    thread.start()


class Bank(MqttClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._serverStatusTopic = '/bank/status'
        self._branchTopic = '/bank/response/branch{}'
        self.connected.connect(self.publishOpen)

    def publishOpen(self):
        msg = {
            'from': 'chatServer',
            'status': 'open'
        }
        self.publish(self._statusTopic, json.dumps(
            msg).encode('utf-8'), 0, True)
        print('Open status published')

    def sendClosingCommand(self):
        msg = {
            'from': 'chatServer',
            'status': 'closed'
        }
        self.publish(self._statusTopic, json.dumps(
            msg).encode('utf-8'), 0, True)
        print('Sending closing bell!')
        closingTimer.stop()

    # overriding method from MqttClient
    def on_message(self, client, userdata, msg):
        print('Processing Message on topic : ', msg.topic)
        data = json.loads(msg.payload)
        print(data)

        amnt = data['amount']
        branchId = data['from']

        wasSuccessful = False
        if data['msg'] == 'withdraw':
            wasSuccessful = self.withdraw(amnt)
        elif data['msg'] == 'deposit':
            wasSuccessful = self.deposit(amnt)

        response = {
            'from': 'bank',
            'msg': 'withdraw',
            'was_success': wasSuccessful
        }

        self.publish(self._branchTopic.format(branchId),
                     json.dumps(response).encode('utf-8'))


if __name__ == "__main__":

    app = QApplication([])

    bank = Bank('127.0.0.1', 1883)
    bank.subscribe('/bank/request/#')

    closingTimer = QTimer()
    closingTimer.setSingleShot(True)
    closingTimer.timeout.connect(bank.sendClosingCommand)
    closingTimer.start(10000)

    bank.start()

    app.exec()
