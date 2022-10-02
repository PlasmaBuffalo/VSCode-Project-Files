from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from mqtt import MqttClient
import json

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Bank(MqttClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._money = 1000
        self._statusTopic = '/bank/status'
        self._branchTopic = '/bank/response/branch{}'
        self.connected.connect(self.publishOpen)

    def publishOpen(self):
        msg = {
            'from': 'bank',
            'status': 'open'
        }
        self.publish(self._statusTopic, json.dumps(
            msg).encode('utf-8'), 0, True)
        print('Open status published')

    def sendClosingCommand(self):
        msg = {
            'from': 'bank',
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

    bank = Bank('127.0.0.1', 1883)
    bank.subscribe('/bank/request/#')

    closingTimer = QTimer()
    closingTimer.setSingleShot(True)
    closingTimer.timeout.connect(bank.sendClosingCommand)
    closingTimer.start(10000)

    bank.start()

    app.exec()
