from alpha_vantage.foreignexchange import ForeignExchange
import matplotlib.pyplot as plt
import pandas as pd
import sys

def formatData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	return df

def checkArgs(f,d):
	if not f.isalpha():
		sys.exit('Non-letters entered for foreign currency symbol.')
	if not d.isalpha():
		sys.exit('Non-letters entered for domestic currency symbol.')

if __name__ == '__main__':
	# Anyone can use this key, AlphaVantage gives them out for free w/ no limits.
	key = 'K2CQV5DF42ONO1EY' 
	try:
		foreign = sys.argv[1].upper()
	except IndexError:
		sys.exit('No foreign currency symbol entered.')
	try:
		domestic = sys.argv[2].upper() 
	except IndexError:
		sys.exit('No domestic currency symbol entered.')
	
	checkArgs(foreign,domestic)
	forex = ForeignExchange(key,output_format='pandas')
	print('Fetching data for: '+foreign+'/'+domestic)
	try:
		data = forex.get_currency_exchange_daily(from_symbol=foreign,to_symbol=domestic,outputsize='full')[0]
	except ValueError:
		sys.exit('Invalid currency symbol entered. Please look at symbols used.')
	
	data = formatData(data)
	c = data['close']
	#o = data['open']
	#h = data['high']
	#l = data['low']
	print('Generating Chart:')
	plt.grid()
	plt.plot(c,label='Close')
	plt.xlabel('Date')
	plt.ylabel('Exchange Rate')
	plt.title(foreign+'/'+domestic+' Daily Close Price')
	plt.legend()
	plt.show()