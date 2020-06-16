from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt
import pandas as pd
import sys

def sma(data,t):   # Simple Moving Avereage
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
	print('Fetching data for: '+coin+'/'+mkt)
	try:
		data = crypt.get_digital_currency_daily(symbol=coin,market=mkt)[0]
	except ValueError:
		sys.exit('Invalid coin or currency symbol entered.')
	
	data = formatData(data)
	c = data['close']
	#o = data['open']
	#h = data['high']
	#l = data['low']
	#v = data['volume']
	print('Generating Chart: ')
	plt.grid()
	plt.plot(c,label='Close')
	plt.plot(sma(c,105),'--',label='105-SMA')
	plt.plot(ema(c,14),'-.',label='14-EMA')
	plt.plot(dema(c,14),'-.',label='14-DEMA')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title(coin+'/'+mkt+' Daily Close Price')
	plt.legend()
	plt.show()