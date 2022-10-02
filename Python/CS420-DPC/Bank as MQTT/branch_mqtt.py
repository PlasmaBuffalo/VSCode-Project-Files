import sys
from mqtt import MqttClient
from threading import Timer
from random import choice, random
import json
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Branch(MqttClient):

    def __init__(self, branchId, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._money = 1000
        self._branchId = branchId
        self._bankIsOpen = False
        self._pubTopic = '/bank/request/branch{}'.format(self._branchId)
        self._bankStatusTopic = '/bank/status'
        self._bankResponseTopic = '/bank/response/branch{}'.format(
            self._branchId)
        self.subscribe(self._bankStatusTopic)
        self.subscribe(self._bankResponseTopic)

    # overriding method from MqttClient
    def on_message(self, client, userdata, msg):
        print('-----------------------')
        print(msg.topic)
        print(msg.payload)
        data = json.loads(msg.payload)
        if 'status' in data:
            if data['status'] == 'open':
                self._bankIsOpen = True
            elif data['status'] == 'closed':
                self._bankIsOpen = False
                self.terminate()
        elif 'was_success' in data:
            pass

    def sendMoneyRequest(self):
        if not self._bankIsOpen:
            return

        data = {
            'from': self._branchId,
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
        print('Branch {} sending a money request.'.format(self._branchId))
        print(data)

    def deposit(self, depositAmnt):
        self._money += depositAmnt
        return True

    def withdraw(self, withdrawAmnt):

        if withdrawAmnt < self._money:
            self._money -= withdrawAmnt
            return True
        else:
            print('Withdraw failed. Not enough funds.')
            return False


if __name__ == "__main__":
    app = QApplication([])

    branchId = sys.argv[1]

    branch = Branch(branchId=branchId, ip='127.0.0.1', port=1883)

    msgTimer = QTimer()
    msgTimer.timeout.connect(branch.sendMoneyRequest)

    branch.start()
    msgTimer.start(2500)

    app.exec()
