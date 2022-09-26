#Authors: Mathias Boddicker, Kylie Hall, Liam Zalubas, Caleb Jenkins
#Assignment: Sockets Homework

import sys
from PyQt6.QtWidgets import QApplication
from TcpServerQt import Branch

if __name__ == "__main__":

	app = QApplication([])
	
	branch_id = int(sys.argv[1])
	
	branch = Branch('127.0.0.1',8000,branch_id)
	branch.start()
	
	app.exec()