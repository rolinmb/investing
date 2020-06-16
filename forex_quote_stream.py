from alpha_vantage.foreignexchange import ForeignExchange
import time
import sys

def checkArgs(f,d,n):
	if not f.isalpha():
		sys.exit('Non-letters entered for foreign currency symbol.')
	if not d.isalpha():
		sys.exit('Non-letters entered for domestic currency symbol.')
	if n <= 0:
		sys.exit('Zero or negative number of quotes entered.')

def checkPair(f,d,fx):
	try:
		data = fx.get_currency_exchange_rate(from_currency=f,to_currency=d)[0]
	except ValueError:
		sys.exit('The currency pair'+f+'/'+d+' does not exist.')
		
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
	try:		
		count = int(sys.argv[3])
	except IndexError:
		sys.exit('Number of desired quotes not entered.')
	except ValueError:
		sys.exit('Decimal entered for number of quotes.')
	
	checkArgs(foreign,domestic,count)
	forex = ForeignExchange(key)
	checkPair(foreign,domestic,forex)
	print('Fetching '+str(count)+' quotes for '+foreign+'/'+domestic+':')
	start = time.time()
	for n in range(0,count):
		data = forex.get_currency_exchange_rate(from_currency=foreign,to_currency=domestic)[0]
		rate = float(data['5. Exchange Rate'])
		print('('+str(n+1)+') Current Rate: ',rate)
		
	end = time.time()
	print('Query Time: '+str(round(float(end-start),3))+'s')	