from alpha_vantage.cryptocurrencies import CryptoCurrencies
import sys

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