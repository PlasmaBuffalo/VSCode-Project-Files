import sys
from xmlrpc.client import boolean
from mqtt import MqttClient
from threading import Timer
from random import choice, random
import json
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

class ChatClient(MqttClient):

    def __init__(self, chatClientId, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #each chat client can choose its own display name, since UUID is unique identifier
        self._name = sys.argv[0]
        #when the server is open, things happen. This keeps track of that
        self._serverIsOpen = False
        self._pubTopic: str = '/data/chatroom/chatClient{}'.format(self.uuid)
        self._serverStatusTopic = '/bank/status'
        self._chatResponseTopic: str = '/bank/response/chatClient{}'.format(
            self.uuid)
        self.subscribe(self._serverStatusTopic)
        self.subscribe(self._chatResponseTopic)

    # overriding method from MqttClient
    def on_message(self, client, userdata, msg):
        print('-----------------------')
        print(msg.topic)
        print(msg.payload)
        data = json.loads(msg.payload)
        if 'status' in data:
            if data['status'] == 'open':
                self._serverIsOpen = True
            elif data['status'] == 'closed':
                self._serverIsOpen = False
                self.terminate()
        elif 'was_success' in data:
            pass

    def sendMoneyRequest(self):
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

    chatClient = ChatClient(chatClientId=chatClientId, ip='127.0.0.1', port=1883)

    msgTimer = QTimer()
    msgTimer.timeout.connect(chatClient.sendMoneyRequest)

    chatClient.start()
    msgTimer.start(2500)

    app.exec()
