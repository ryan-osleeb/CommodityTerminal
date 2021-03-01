import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from technical_analysis import macd, moving_avgs, rsi

COMMODITY = {"crude oil": "EIA/PET_RWTC_D"}

def get_price(commodity, start, end):
	data = quandl.get(COMMODITY[commodity], start_date = start, end_date = end)
	data = pd.DataFrame(data)
	data['Date'] = data.index
	return data

if __name__ == "__main__":
	comm = get_price("crude oil", "2019-01-01", "2021-02-10")
	#print(comm)
	rsi(comm)