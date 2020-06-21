from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt
import pandas as pd
from analysis import *
import sys

def formatData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	df = df.T.drop_duplicates().T
	return df

def checkArgs(s,m):
	if not s.isalpha():
		sys.exit('Non-letters entered for coin symbol.')
	if not m.isalpha():
		sys.exit('Non-letters entered for currency type.')
	
if __name__ == '__main__':
	# Anyone can use this key, AlphaVantage gives them out for free w/ no limits.
	key = 'K2CQV5DF42ONO1EY' 
	try:
		coin = sys.argv[1].upper()
	except IndexError:
		sys.exit('No coin/symbol entered.')
	try:
		mkt = sys.argv[2].upper()
	except IndexError:
		sys.exit('No currency type entered.')
	
	checkArgs(coin,mkt)
	crypt = CryptoCurrencies(key,output_format='pandas')
	print('Fetching data for '+coin+'/'+mkt+':')
	try:
		data = crypt.get_digital_currency_daily(symbol=coin,market=mkt)[0]
	except ValueError:
		sys.exit('Invalid coin or currency symbol entered.')
	
	data = formatData(data)
	o = data['open']
	h = data['high']
	l = data['low']
	c = data['close']
	#v = data['volume']
	
	print('Generating Charts:')
	plt.figure(0)
	plt.title(coin+'/'+mkt+' Daily Close Price')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.grid()
	plt.plot(c,label='Close')
	plt.plot(sma(c,200),'--',label='200-SMA')
	plt.plot(sma(c,105),'--',label='105-SMA')
	plt.plot(ema(c,14),'-.',label='14-EMA')
	plt.plot(dema(c,14),'-.',label='14-DEMA')
	plt.legend()
	
	plt.figure(1)
	plt.title(coin+'/'+mkt+' Rates of Change (Daily)')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.plot(roc(c,14),label='ROC(14)')
	plt.plot(roc(c,35),label='ROC(35)')
	plt.grid()
	plt.legend()
	
	plt.figure(2)
	plt.title(coin+'/'+mkt+' Finite-Difference Approximation for 1st Derivative')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(approxDeriv(c,3),label='Slope using ROC(3)')
	plt.legend()
	
	plt.figure(3)
	plt.title(coin+'/'+mkt+' Standard Deviation over time')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(standardDeviations(c),label='Rolling Standard Deviation')
	plt.plot(sma(standardDeviations(c),200),label='SMA-200 of Std. Devs')
	plt.legend()
	
	plt.show()