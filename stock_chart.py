from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import sys

def checkTicker(t):
	if not t.isalpha():
		sys.exit('Non-letters entered for ticker/symbol.')

if __name__ == '__main__':
	# Anyone can use this key. AlphaVantage gives them out for free w/ no limit
	key = 'K2CQV5DF42ONO1EY' 
	try:
		ticker = sys.argv[1].upper()
	except IndexError:
		sys.exit('No ticker/symbol entered.')
		
	checkTicker(ticker)
	ts = TimeSeries(key,output_format='pandas')
	print('Fetching data for ticker/symbol: '+ticker)
	try:
		data = ts.get_datily(symbol=ticker,outputsize='full')[0]
	except ValueError:
		sys.exit('Ticker is invalid/non-existant.')
	
	data = formatData(data)
	c = data['close']
	print('Generating Chart: ')
	plt.grid()
	plt.plot(c,label='Close')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title(ticker+' Datily Close Price')
	plt.legend()
	plt.show()