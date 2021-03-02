import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from technical_analysis import macd, moving_avgs, rsi, stoch, bollinger_band, technical_summary

COMMODITY = {"crude oil": "CHRIS/CME_CL1"}

def get_price(commodity, start):
	data = quandl.get(COMMODITY[commodity], start_date = start)
	data = pd.DataFrame(data)
	data['Date'] = data.index
	return data

if __name__ == "__main__":
	comm = get_price("crude oil", "2020-07-01")
	#print(comm)
	technical_summary(comm)