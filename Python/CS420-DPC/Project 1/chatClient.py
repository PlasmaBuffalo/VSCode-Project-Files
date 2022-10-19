from re import X
import sys
from mqtt import MqttClient
from threading import Thread
import json
from PyQt6.QtWidgets import QApplication

class ChatClient(MqttClient):

    def __init__(self, chatClientId, *args, **kwargs):
        #this contains ip, port, uuid of MqttClient
        super().__init__(*args, **kwargs)

        #each client has its own unique id
        self._chatClientId = chatClientId
        #clients will publish all messages on the request topic using RPC calls
        self._mySendChannel = '/msgServer/request/chatClient{}'.format(self._chatClientId)
        #clients listen on their own chat response topic
        self._myReceiveChannel = '/msgServer/response/chatClient{}'.format(self._chatClientId)
        self.subscribe(self._myReceiveChannel)

    # overriding method from MqttClient
    def on_message(self, client, userdata, msg):
        #when a client sends a message, it goes to the chatServer message handler using RPC methods
        pass

    def typestate(self) -> None:
        while (self.isConnected):
            receiver = input("Enter chat client ID to message: ")
            msg = input("Enter message: ")
            message={
                "sender":self._chatClientId,
                "receiver":receiver,
                "text":msg,
            }
            self.publish(self._mySendChannel, message)

if __name__ == "__main__":
    app = QApplication([])

    chatClientId = sys.argv[1]

    # client connects on localhost for now given the above ID name
    cc = ChatClient(chatClientId=chatClientId, ip='127.0.0.1', port=1883)

    cc.start()
    
    app.exec()

    cc.typestate()
        