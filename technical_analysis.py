import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def macd(df):
	exp1 = df.Value.ewm(span = 12, adjust = False).mean()
	exp2 = df.Value.ewm(span = 26, adjust = False).mean()
	macd = exp1 - exp2
	exp3 = macd.ewm(span = 9, adjust = False).mean()
	pd.plotting.register_matplotlib_converters()
	plt.plot(df.Date, macd)
	plt.plot(df.Date, exp3)
	plt.show()


def moving_avgs(df, days):
	rolling = df.Value.rolling(window = days).mean()
	rolling = rolling.replace(np.nan, np.mean(df.Value))
	pd.plotting.register_matplotlib_converters()
	plt.plot(df.Date, df.Value)
	plt.plot(df.Date, rolling)
	plt.show()


def rsi(df):
	gains = []
	losses = []
	for prices in range(len(df.Value)-1):
		change = df.Value[prices+1] - df.Value[prices]
		if change > 0:
			gains.append(change)
			losses.append(0)
		else:
			losses.append(abs(change))
			gains.append(0)
	RSI = []
	for i in range(len(gains)-14):
		avg_gain = np.mean(gains[i:i+14])
		avg_loss = np.mean(losses[i:i+14])
		rs = (avg_gain/avg_loss)
		rsi = (100-(100/(1+rs)))
		RSI.append(rsi)
	pd.plotting.register_matplotlib_converters()
	plt.plot(df.Date[15:], RSI)
	plt.show()

#def stoch(df):



