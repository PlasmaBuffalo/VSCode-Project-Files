
import sys
import json
import matplotlib.pyplot as  plt
from xmlrpc.client import ServerProxy
 
import pymysql

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
if __name__ == "__main__":

	ticker   = sys.argv[1]
	num_sims = int(sys.argv[2])

	rpcClient = ServerProxy('http://169.254.213.62:8000')
	
	simPrices = rpcClient.runSimulation(ticker, num_sims)
	print('Running MonteCarlo Simulation for ',ticker)
	
	plt.figure(figsize=(10,6))
	plt.title('Stock Prediction : {}  {} Simulations'.format(ticker, num_sims))
	plt.ylabel('Price (P)')
	plt.xlabel('Time (Days)')
	
	for simPrice in simPrices:
		plt.plot(simPrice)

	plt.show()
