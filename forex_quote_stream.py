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
		
	