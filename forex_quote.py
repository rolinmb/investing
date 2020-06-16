from alpha_vantage.foreignexchange import ForeignExchange
import sys

def checkArgs(f,d):
	if not f.isalpha():
		sys.exit('Non-letters entered for foreign currency symbol.')
	if not d.isalpha():
		sys.exit('Non-letters entered for domestic currency symbol.')

def checkPair(f,d,fx):
	try:
		data = fx.get_currency_exchange_rate(from_currency=f,to_currency=d)[0]
	except ValueError:
		sys.exit('The currency pair: '+f+'/'+d+' does not exist.')
		
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
	forex = ForeignExchange(key)
	checkPair(foreign,domestic,forex)
	print('Fetching quote for: '+foreign+'/'+domestic)
	data = forex.get_currency_exchange_rate(from_currency=foreign,to_currency=domestic)[0]
	rate = float(data['5. Exchange Rate'])
	print('Current Rate: ',rate)