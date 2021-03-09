import sqlite3
from sqlite3 import Error
import quandl
import pandas as pd
import numpy as np
from technical_analysis import moving_avgs, rsi, macd

COMMODITY = {"crude oil": "CHRIS/CME_CL1",
				"gasoline": "CHRIS/CME_RB1",
				"natural gas": "CHRIS/CME_NG1", 
				"corn": "CHRIS/CME_C1", 
				"soybean": "CHRIS/CME_S1"}

def get_price(commodity, start):
	data = quandl.get(COMMODITY[commodity], start_date = start)
	data = pd.DataFrame(data)
	data['Date'] = data.index
	return data

if __name__ == "__main__":
	#comm = get_price("gasoline", "2020-07-01")
	#print(comm.columns)

	for comm in COMMODITY:
		prices = []
		prices = pd.DataFrame(get_price(comm, '2016-01-01'))
		prices['50DMA'] = moving_avgs(prices, 50)
		prices['100DMA'] = moving_avgs(prices, 100)
		prices['RSI'] = rsi(prices)
		# macd, exp = macd(prices)
		# prices['MACD'] = macd
		# prices['EXP'] = exp
		file_name = comm+'.csv'
		prices.to_csv(file_name, index=False)