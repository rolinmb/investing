from alpha_vantage.foreignexchange import ForeignExchange
from analysis import *
from config import *
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
	try:
		foreign = sys.argv[1].upper()
	except IndexError:
		sys.exit('No foreign currency symbol entered.')
	try:
		domestic = sys.argv[2].upper() 
	except IndexError:
		sys.exit('No domestic currency symbol entered.')
	checkArgs(foreign,domestic)
	forex = ForeignExchange(AV_API_KEY,output_format='pandas')
	print('Fetching data for '+foreign+'/'+domestic+':')
	try:
		data = forex.get_currency_exchange_daily(from_symbol=foreign,to_symbol=domestic,outputsize='full')[0]
	except ValueError:
		sys.exit('Invalid currency symbol entered. Please look at symbols used.')
	data = formatData(data)
	c = data['close']
	#o = data['open']
	#h = data['high']
	#l = data['low']
	print('Generating Charts:')
	plt.figure(0)
	plt.title(foreign+'/'+domestic+' Daily Exchange Rate Close')
	plt.xlabel('Date')
	plt.ylabel('Rate')
	plt.grid()
	plt.plot(c,label='Close')
	plt.plot(sma(c,200),'--',label='200-SMA')
	plt.plot(sma(c,100),'--',label='100-SMA')
	plt.plot(ema(c,15),'-.',label='15-EMA')
	plt.plot(dema(c,15),'-.',label='15-DEMA')
	plt.legend()
	
	plt.figure(1)
	plt.title(foreign+'/'+domestic+' Rates of Change (Daily)')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(roc(c,14),label='ROC(14)')
	plt.plot(roc(c,35),label='ROC(35)')
	plt.legend()
	
	plt.figure(2)
	plt.title(foreign+'/'+domestic+' Finite-Difference Approximation for 1st Derivative')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(approxDeriv(c,3),label='Slope using ROC(3)')
	plt.legend()
	
	plt.figure(3)
	plt.title(foreign+'/'+domestic+' Standard Deviation over time')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(standardDeviations(c),label='Rolling Standard Deviations')
	plt.plot(sma(standardDeviations(c),200),label='SMA-200 of Std. Devs')
	plt.legend()
	
	plt.figure(4)
	plt.title(foreign+'/'+domestic+' True Strength Index')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(tsi(c,26,12))
	
	plt.show()