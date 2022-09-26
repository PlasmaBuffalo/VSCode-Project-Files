#Authors: Mathias Boddicker, Kylie Hall, Liam Zalubas, Caleb Jenkins
#Assignment: Sockets Homework

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
from TcpServerQt import Bank

if __name__ == "__main__":
	
	app = QApplication([])
	
	bank = Bank('127.0.0.1',8000,1000)
	bank.start()
	QTimer.singleShot(20000, app, 'quit()')

	app.exec()