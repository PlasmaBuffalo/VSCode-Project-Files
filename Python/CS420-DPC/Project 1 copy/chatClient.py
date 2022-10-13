import sys
from mqtt import MqttClient
from threading import Timer
from random import choice, random
import json
from PyQt6.QtWidgets import QApplication


class ChatClient(MqttClient):

    def __init__(self, chatClientId, *args, **kwargs):
        # this contains ip, port, uuid of MqttClient
        super().__init__(*args, **kwargs)

        # each client has its own unique id
        self._chatClientId = chatClientId
        # tracks if server is online
        self._serverIsOpen = False
        # clients will publish all messages on the request topic using RPC calls
        self._pubTopic = '/msgServer/request/chatClient{}'.format(
            self._chatClientId)
        # clients will subscribe to the server status topic
        self._serverStatusTopic = '/msgServer/status'
        # clients listen on the chat response topc
        self._chatResponseTopic = '/msgServer/response/chatClient{}'.format(
            self._chatClientId)
        # clients subscribe to server status topic so that they know when server is active/online
        self.subscribe(self._serverStatusTopic)

    # overriding method from MqttClient
    def on_message(self, client, userdata, msg):
        # when a client sends a message, it goes to the chatServer message handler using RPC methods
        print('')

    def sendMoneyRequest(self):
        # if server is closed, stop method preemptively
        if not self._serverIsOpen:
            return

        data = {
            'from': self._chatClientId,
        }

        isWithdraw = choice([0, 1])
        if isWithdraw:
            data['msg'] = 'withdraw'
            action = 'withdraw'
        else:
            data['msg'] = 'deposit'
            action = 'deposit'

        data['amount'] = random() * 100

        self.publish(self._pubTopic, json.dumps(data).encode('utf-8'))
        print('ChatClient {} sending a money request.'.format(self._chatClientId))
        print(data)


if __name__ == "__main__":
    app = QApplication([])

    chatClientId = sys.argv[1]

    # client connects on localhost for now given the above ID name
    chatClient = ChatClient(chatClientId=chatClientId,
                            ip='127.0.0.1', port=1883)

    chatClient.start()

    app.exec()
