import sys
from mqtt import MqttClient
from threading import Timer
from random import choice, random
import json
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

class ChatClient(MqttClient):

    def __init__(self, chatClientId, *args, **kwargs):
        #this contains ip, port, uuid of MqttClient
        super().__init__(*args, **kwargs)

        #each client has its own unique id
        self._chatClientId = chatClientId
        #clients will publish all messages on the request topic using RPC calls
        self._pubTopic = '/msgServer/request/chatClient{}'.format(self._chatClientId)
        #clients will subscribe to the server status topic
        self._serverStatusTopic = '/msgServer/status'
        #clients listen on the chat response topc
        self._chatResponseTopic = '/msgServer/response/chatClient{}'.format(
            self._chatClientId)
        self.subscribe(self._serverStatusTopic)
        self.subscribe(self._chatResponseTopic)

    # overriding method from MqttClient
    def on_message(self, client, userdata, msg):
        #when a client sends a message, it goes to the chatServer message handler using RPC methods
        print('')

    def typestate(self) -> None:
        while (self.isConnected):
            target = input("Enter chat client ID to message: ")
            msg = input("Enter message: ")

if __name__ == "__main__":
    app = QApplication([])

    chatClientId = sys.argv[1]

    # client connects on localhost for now given the above ID name
    cc = ChatClient(chatClientId=chatClientId, ip='127.0.0.1', port=1883)

    cc.start()
    
    app.exec()

    cc.typestate()
        