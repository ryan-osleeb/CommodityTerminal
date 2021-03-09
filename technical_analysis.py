import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def macd(df):
	exp1 = df.Settle.ewm(span = 12, adjust = False).mean()
	exp2 = df.Settle.ewm(span = 26, adjust = False).mean()
	macd = exp1 - exp2
	exp3 = macd.ewm(span = 9, adjust = False).mean()
	return macd, exp3
	# pd.plotting.register_matplotlib_converters()
	# plt.plot(df.Date, macd)
	# plt.plot(df.Date, exp3)
	# plt.show()

def moving_avgs(df, days):
	sma = df.Settle.rolling(window = days).mean()
	sma = sma.replace(np.nan, np.mean(df.Settle))
	return sma
	# pd.plotting.register_matplotlib_converters()
	# plt.plot(df.Date, df.Settle)
	# plt.plot(df.Date, sma)
	# plt.show()

def rsi(df):
	gains = []
	losses = []
	for prices in range(len(df.Settle)-1):
		change = df.Settle[prices+1] - df.Settle[prices]
		if change > 0:
			gains.append(change)
			losses.append(0)
		else:
			losses.append(abs(change))
			gains.append(0)
	RSI = [30] * 15
	for i in range(len(gains)-14):
		avg_gain = np.mean(gains[i:i+14])
		avg_loss = np.mean(losses[i:i+14])
		rs = (avg_gain/avg_loss)
		rsi = (100-(100/(1+rs)))
		RSI.append(rsi)
	oversold = [30] * len(RSI)
	overbought = [70] * len(RSI)
	return RSI
	# pd.plotting.register_matplotlib_converters()
	# plt.plot(df.Date[15:], RSI)
	# plt.plot(df.Date[15:], oversold)
	# plt.plot(df.Date[15:], overbought)
	# plt.show()

def stoch(df):
	low = df.Settle.rolling(window = 14).min()
	high = df.Settle.rolling(window = 14).max()
	K = 100*((df.Settle-low)/(high-low))
	D = K.rolling(window = 3).mean()
	return K, D
	# pd.plotting.register_matplotlib_converters()
	# plt.plot(df.Date, K)
	# plt.plot(df.Date, D)
	# plt.show()

def bollinger_band(df):
	avg = df.Settle.rolling(window = 20).mean()
	std = df.Settle.rolling(window = 20).std()
	upper = avg + (2 * std)
	lower = avg - (2 * std)
	return avg, upper, lower
	# pd.plotting.register_matplotlib_converters()
	# plt.plot(df.Date, df.Settle)
	# plt.plot(df.Date, avg)
	# plt.plot(df.Date, upper)
	# plt.plot(df.Date, lower)
	# plt.show()

def support_line(df, i):
	support = df.Low[i] < df.Low[i-1] and df.Low[i] < df.Low[i+1] and df.Low[i-1] < df.Low[i-2] and df.Low[i+1] < df.Low[i+2]
	return support

def resistance_line(df, i):
	resistance = df.High[i] > df.High[i-1] and df.High[i] > df.High[i+1] and df.High[i-1] > df.High[i-2] and df.High[i+1] > df.High[i+2]
	return resistance

def sup_res(df):
	levels = []
	for i in range(2,len(df.Settle)-2):
		if support_line(df, i):
			levels.append((i, df.Low[i]))
		elif resistance_line(df, i):
			levels.append((i, df.High[i]))
	# for level in levels:
	# 	plt.hlines(level[1], xmin=df.Date[level[0]],\
 #               xmax=max(df.Date),colors='green')
	# plt.plot(df.Settle)
	# plt.show()

def technical_summary(df):
	#bollinger bands
	avg = df.Settle.rolling(window = 20).mean()
	std = df.Settle.rolling(window = 20).std()
	upper = avg + (2 * std)
	lower = avg - (2 * std)

	#rsi
	gains = []
	losses = []
	for prices in range(len(df.Settle)-1):
		change = df.Settle[prices+1] - df.Settle[prices]
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
	oversold = [30] * len(RSI)
	overbought = [70] * len(RSI)

	#macd
	exp1 = df.Settle.ewm(span = 12, adjust = False).mean()
	exp2 = df.Settle.ewm(span = 26, adjust = False).mean()
	macd = exp1 - exp2
	exp3 = macd.ewm(span = 9, adjust = False).mean()

	pd.plotting.register_matplotlib_converters()
	fig, axs = plt.subplots(3)
	fig.suptitle('Technical Analysis')
	axs[0].plot(df.Date, df.Settle)
	axs[0].plot(df.Date, upper)
	axs[0].plot(df.Date, avg)
	axs[0].plot(df.Date, lower)
	axs[0].set_title('Bollinger Bands')
	axs[1].plot(df.Date[15:], RSI)
	axs[1].plot(df.Date[15:], oversold)
	axs[1].plot(df.Date[15:], overbought)
	axs[1].set_title('RSI')
	axs[2].plot(df.Date, macd)
	axs[2].plot(df.Date, exp3)
	axs[2].set_title('MACD')
	for ax in axs:
		ax.label_outer()
	plt.show()
