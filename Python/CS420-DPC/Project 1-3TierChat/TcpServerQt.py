# Authors: Mathias Boddicker, Kylie Hall, Liam Zalubas, Caleb Jenkins
# Assignment: Sockets Homework

import sys
import json
from random import randint, random, choice

from PyQt6.QtCore import QObject, QByteArray, QTimer
from PyQt6.QtNetwork import QTcpSocket, QTcpServer, QHostAddress, QAbstractSocket
from PyQt6.QtWidgets import QApplication


import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class Branch(QObject):

    def __init__(self, ip, port, branch_id):
        super().__init__()
        self._branchId = branch_id
        self._ip = ip
        self._port = port
        self._transactTimer = QTimer()
        self._transactTimer.timeout.connect(self._sendTransaction)

        # create your TCP Socket
        self._client = QTcpSocket(self)
        # when you call self._client.connectToHost you should immediately handle the connection in _handleConnected
        self._client.connected.connect(self._handleConnected)
        # callback for whenever your QTcpSocket is disconnected
        self._client.disconnected.connect(self._handleDisconnected)
        # callback for when an error occurs on the socket
        self._client.errorOccurred.connect(self._handleError)
        # this lets you know the socket wrote data to the buffer. Mostly for awareness
        self._client.bytesWritten.connect(self._handleBytesWritten)
        # this is where all the data you receive comes in. Handle messages from the Bank here in _handleReadyRead
        self._client.readyRead.connect(self._handleReadyRead)
        # this lets you know when the state of your socket changes. Whether you are connecting, disconnecting, not connected, etc..
        self._client.stateChanged.connect(self._handleStateChange)

    def start(self):
        self._client.connectToHost(QHostAddress(self._ip), self._port)
        # wait max 5 seconds for connection
        self._client.waitForConnected(5000)

    def _handleConnected(self):
        print('Branch {} is connected.'.format(self._branchId))
        data = {
            'from': self._branchId,
            'msg': 'acknowledged'
        }
        self.sendMessage(data)

        # interval in milliseconds
        # make sure its over 1 second just for our sanity. It can go as fast as you want but that will be terrible to track
        msgInterval = int(random() * 3000 + 1000)
        self._transactTimer.start(msgInterval)

    def _handleDisconnected(self):
        print('Branch {} is disconnected.'.format(self._branchId))

    def _handleError(self, err):
        print('Error: ', err)
        self._transactTimer.stop()
        print('Branch is closed due to socket error.')

    def _handleBytesWritten(self, totalBytesWritten):
        print('Branch {} wrote {} bytes.'.format(
            self._branchId, totalBytesWritten))

    def _handleReadyRead(self):
        print('Recieved a message')
        bData = self._client.readAll()
        msg = json.loads(bData.data())
        print(msg)

    def _sendTransaction(self):

        number = randint(0, 1)
        type_trans = ''

        if (number == 0):
            type_trans = 'deposit'
        else:
            type_trans = 'withdraw'

        data = {
            'from': self._branchId,
            'type': type_trans,
            'amount': randint(0, 100)
        }
        self.sendMessage(data)

    def _handleStateChange(self, state):
        print('Branch {} is now {}'.format(self._branchId, state))
        if state in [QAbstractSocket.SocketState.ClosingState, QAbstractSocket.SocketState.UnconnectedState]:
            print('Branch is not connected to the server.')
            print('Closing the branch.')
            self._transactTimer.stop()

    def sendMessage(self, msg):
        bData = QByteArray(json.dumps(msg).encode('utf-8'))
        self._client.write(bData)
        self._client.waitForBytesWritten()


class Bank(QObject):

    def __init__(self, ip, port, starting_money):
        super().__init__()
        self._money = starting_money
        self._ip = ip
        self._port = port
        self._branches = []
        self._openTimer = QTimer()
        self._openTimer.timeout.connect(self.closeUpShop)
        self._server = QTcpServer(self)
        self._server.newConnection.connect(self._handleNewConnection)

    def start(self):
        self._server.listen(QHostAddress(self._ip), self._port)
        self._openTimer.start(20000)

    def closeUpShop(self):
        msg = {
            'Msg': 'Closing time.'
        }
        for br in self._branches:
            self.sendMessage(br, msg)
        self._server.close()

    def _handleNewConnection(self):
        # get the next available connection. The 'branchClient' is the QTcpSocket returned from the QTcpServer that allows you to communicate with the connecting client
        branchClient = self._server.nextPendingConnection()
        self._branches.append(branchClient)
        # read data from the connecting client.
        branchClient.readyRead.connect(self._handleBranchMessage)
        # lets you know if one of you sockets state has been altered
        branchClient.stateChanged.connect(self._handleBranchStateChange)

    def _handleBranchStateChange(self, state):
        # self.sender() gives you the object that emitted the signal.
        # For this function, look on line 113. We connect the branchClient (which is a QTcpSocket) signal 'stateChanged' to connect to _handleBranchStateChange.
        # so the self.sender() here is the 'branchClient' from _handleNewConnection. It is the QTcpSocket that allows you to communicate back with the
        # client it is connected to from another process
        branchClient = self.sender()

        if state in [QAbstractSocket.SocketState.ClosingState, QAbstractSocket.SocketState.UnconnectedState]:
            print('Branch is not connected to the server.')
            print('Closing the branch.')
            self._transactTimer.stop()
        # ^^ might want to add code here to handle a possible closed connected
        # check out line 77 for an example

    def _handleBranchMessage(self):
        # get the tcp client that triggered this signal. read _handleBranchStateChange for more details
        branchClient = self.sender()
        bData = branchClient.readAll()  # raw bytes
        msg = json.loads(bData.data())
        print(msg)  # this is now a python dictionary
        if ('type' in msg):

            if (msg['type'] == 'deposit'):
                amount = msg['amount']
                self.deposit(amount)
                print("Money left in bank: {}".format(self.money()))
                sdata = {
                    'from': 'Bank',
                    'type': 'deposit successful'
                }
                self.sendMessage(branchClient, sdata)

            if (msg['type'] == 'withdraw'):
                amount = msg['amount']
                if (amount > self.money()):
                    sdata = {
                        'msg': 'Insufficient funds in bank'
                    }
                else:
                    self.withdraw(amount)
                    print("Money left in bank: {}".format(self.money()))
                    sdata = {
                        'from': 'Bank',
                        'type': 'withdraw successful'
                    }
                self.sendMessage(branchClient, sdata)

    def sendMessage(self, client, msg):
        # use this function to send data if you wish
        bData = QByteArray(json.dumps(msg).encode('utf-8'))
        client.write(bData)
        client.waitForBytesWritten()

    def money(self):
        return self._money

    def deposit(self, depositAmnt):
        self._money = self._money + depositAmnt

    def withdraw(self, withdrawAmnt):
        self._money = self._money - withdrawAmnt
