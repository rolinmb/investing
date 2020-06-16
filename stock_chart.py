from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import sys

def sma(data,t):   # Simple Moving Average
	return data.rolling(t).mean()
	
def ema(data,t):   # Exponential Moving Average
	return data.ewm(span=t,adjust=False).mean()
	
def dema(data,t):  # Double-Exponential Moving Average
	e = ema(data,t)
	de = ema(e,t)
	return (2.0*e)-de

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
	print('Fetching data for ticker/symbol: '+ticker)
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
	print('Generating Chart: ')
	plt.grid()
	plt.plot(c,label='Close')
	plt.plot(sma(c,100),'-.',label='100-SMA')
	plt.plot(sma(c,50),'-.',label='50-SMA')
	plt.plot(ema(c,10),'--',label='10-EMA')
	plt.plot(dema(c,10),'--',label='10-DEMA')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title(ticker+' Datiy Close Price')
	plt.legend()
	plt.show()