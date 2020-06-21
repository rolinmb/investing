from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
from analysis import *
import sys

def formatData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	return df

def checkTicker(t):
	if not t.isalpha():
		sys.exit('Non-letters entered for ticker/symbol.')

if __name__ == '__main__':
	# Anyone can use this key, AlphaVantage gives them out for free w/ no limits.
	key = 'K2CQV5DF42ONO1EY' 
	try:
		ticker = sys.argv[1].upper()
	except IndexError:
		sys.exit('No ticker/symbol entered.')
		
	checkTicker(ticker)
	ts = TimeSeries(key,output_format='pandas')
	print('Fetching data for ticker/symbol '+ticker+':')
	try:
		data = ts.get_daily(symbol=ticker,outputsize='full')[0]
	except ValueError:
		sys.exit('Ticker is invalid/non-existant.')
	
	data = formatData(data)
	c = data['close']
	#o = data['open']
	#h = data['high']
	#l = data['low']
	#v = data['volume']
	print('Generating Charts:')
	
	plt.figure(0)
	plt.title(ticker+' Daily Close Price')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.grid()
	plt.plot(c,label='Close')
	plt.plot(sma(c,100),'-.',label='100-SMA')
	plt.plot(sma(c,50),'-.',label='50-SMA')
	plt.plot(ema(c,10),'--',label='10-EMA')
	plt.plot(dema(c,10),'--',label='10-DEMA')
	plt.legend()
	
	plt.figure(1)
	plt.title('Rates of Change (Daily) for '+ticker)
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(roc(c,12),label='ROC(12)')
	plt.plot(roc(c,25),label='ROC(25)')
	plt.legend()

	plt.figure(2)
	plt.title('Finite-Difference Approximation of 1st Derivative for '+ticker)
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(approxDeriv(c,3),label='Slope using ROC(3)')
	plt.plot(approxDeriv(c,5),label='Slope using ROC(5)')
	plt.legend()
	
	plt.show()