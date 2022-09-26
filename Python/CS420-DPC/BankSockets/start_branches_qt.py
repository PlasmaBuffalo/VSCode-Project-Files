#Authors: Mathias Boddicker, Kylie Hall, Liam Zalubas, Caleb Jenkins
#Assignment: Sockets Homework

from subprocess import Popen, PIPE

if __name__ == "__main__":
	
	processes = []
	for i in range(2):
		proc = Popen(['python3','start_branch_qt.py',str(i)], stderr=PIPE, stdout=PIPE)
		processes.append(proc)