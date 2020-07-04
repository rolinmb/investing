from alpha_vantage.timeseries import TimeSeries
import matplotlib.pylab as plt
import pandas as pd
from analysis import *
from config import *
import sys

def formatData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	return df

def genCharts(data,t):
	comChannel = cci(data['high'],data['low'],data['close'],20)
	print('\n(Generating charts)')
	plt.figure(0)
	plt.title(t+' Daily Close Price')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.grid()
	plt.plot(data['close'],label='Close')
	plt.plot(ema(data['close'],7),label='7-EMA')
	plt.plot(ema(data['close'],25),label='25-EMA')
	plt.legend()
	plt.figure(1)
	plt.title('Rates of Change')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(roc(data['close'],12),label='ROC(12):Close')
	plt.plot(roc(ema(data['close'],7),12),label='ROC(12):7-EMA')
	plt.plot(roc(ema(data['close'],25),12),label='ROC(12):25-EMA')
	plt.legend()
	plt.figure(2)
	plt.title('Commodity Channel Index')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(comChannel,label='CCI')
	plt.plot(ema(comChannel,18),label='18-EMA')
	plt.plot(sma(comChannel,200),label='200-SMA')
	plt.legend()
	print('\t*Displaying charts')
	plt.show()
	
if __name__ == '__main__':
	try:
		ticker = sys.argv[1].upper()
	except IndexError:
		sys.exit('No ticker entered for first argument.')
	if not ticker.isalpha():
		sys.exit('Invealid characters/ticker entered; use alphabetical characters.')
	ts = TimeSeries(AV_API_KEY,output_format='pandas')
	try:
		data = ts.get_daily(symbol=ticker,outputsize='full')[0]
	except ValueError:
		sys.exit('Could not fetch data, '+ticker+' does not exist.')
	data = formatData(data)
	genCharts(data,ticker)