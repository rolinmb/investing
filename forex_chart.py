from alpha_vantage.foreignexchange import ForeignExchange
import matplotlib.pyplot as plt
import pandas as pd
import sys

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
		data = forex.fs_daily(from_symbol=foreign,to_symbol=domestic)
	except ValueError:
		sys.exit('Invalid currency symbol entered. Please look at symbols used.')
	print(data)