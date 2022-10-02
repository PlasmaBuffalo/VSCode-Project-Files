
import sys
import json
import pandas as pd
import numpy as np
import pymysql
from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread 

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class StockTicker():

	def __init__(self):
		hostname  = "pimqttdb"  
		db_user   = "cosc420"       
		db_pswd   = "cosc420"           
		db        = "MonteCarlo"
		self.conn = pymysql.connect(host=hostname, user=db_user, password=db_pswd, database=db)
		self.cur  = self.conn.cursor() # Create a cursor object. Allows you to navigate the DB
	  

	def runSimulation(self, ticker, number_simulations):
	
		query    = ("Select * " +
					"from StockPrices " +
					"where Ticker = '{}'").format(ticker)
	
		data     = pd.read_sql(query, self.conn)
		data0 = data['Close']
	
		returns = np.log(1 + data0.pct_change())
		avg = returns.mean()
		stdDev = returns.std()

		simPrices = []
		for i in range(number_simulations):
			simReturns = np.random.normal(avg, stdDev, 252)
			price = data0.iloc[-1] # take last row.. most recent price
			simPrice = price * (simReturns + 1).cumprod()

			simPrice = simPrice.flatten() 
			simPrice = np.insert(simPrice, 0, data0.values.tolist(),0)

			simPrices.append(simPrice.tolist())
		
		print('Monte Carlo Simulation executed {} times for the stock {}.'.format(number_simulations, ticker))
		return simPrices

if __name__ == "__main__":

	rpcServer = SimpleXMLRPCServer(('127.0.0.1',8000))
	rpcServer.register_instance(StockTicker())

	thread = Thread(target=rpcServer.serve_forever, args=())
	thread.start()

	print('Stock MonteCarlo RPC Server is running..')

