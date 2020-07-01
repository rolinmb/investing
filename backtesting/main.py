from alpha_vantage.timeseries import TimeSeries
#from config import *
from analysis import *
from strategies import *
from alpaca_util import *
import alpaca_trade_api as alpaca
import matplotlib.pyplot as plt
import pandas as pd
import time
import sys
import re

def genCharts(data,t):
	print('\n(Generating charts)')
	plt.figure(0)
	plt.title(t+' Daily Close Price')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.grid()
	plt.plot(data,label='Close')
	plt.plot(ema(data,7),label='7-EMA')
	plt.plot(ema(data,25),label='25-EMA')
	plt.legend()
	plt.figure(1)
	plt.title('Rates of Change')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(roc(data,12),label='ROC(12):Close')
	plt.plot(roc(ema(data,7),12),label='ROC(12):7-EMA')
	plt.plot(roc(ema(data,25),12),label='ROC(12):25-EMA')
	plt.legend()
	print('\t*Displaying charts')
	plt.show()
	
def formatData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	return df
	
def fetchData(ts,t,charts):	
	fetchStart = time.time()
	print('\n(Fetching AlphaVantage data for '+t+')')
	try:
		d = ts.get_daily(symbol=t,outputsize='full')[0]
		#d = ts.get_weekly(symbol=t)[0]	
	except ValueError:
		sys.exit('\t*Error: ticker/symbol '+t+' does not exist')
	print('\t*'+t+' Data obtained sucessfully in '+str(round(time.time()-fetchStart,2))+' seconds')
	df = formatData(d)
	if(charts):
		genCharts(df['close'],t)
	return df		

def writeData(file,t,funcName,shareCount,iBalance,fBalance,profit,percent):
	file.write(t+' '+funcName+' '+str(shareCount)+' '+str(iBalance)+' '+str(fBalance)+' '+str(profit)+' '+str(percent)+'\n')

def backtest(key,tickers,initialBalance,shareCount,strategyTest):
	stratName = str(strategyTest.__name__)
	backStart = time.time()
	ts = TimeSeries(key,output_format='pandas')
	print('\n(Backtesting strategy using '+str(shareCount)+' share(s) over '+str(len(tickers)*len(tickers[0]))+' Stock(s)/ETF(s))')
	print('\t*Writing to \'data.txt\'')
	f = open('data.txt','a')
	for i in range(0,len(tickers)):
		testBlockStart = time.time()
		for t in tickers[i]:
			testStart = time.time()
			print('\n\t<-- Backtesting '+t+' w/ '+stratName+' -->')
			data = fetchData(ts,t,False)
			finalBalance,batchSize = strategyTest(data['close'],t,initialBalance,shareCount,False)
			profit = round(finalBalance-initialBalance,2)
			percent = round((100*(finalBalance/initialBalance))-100,2)
			writeData(f,t,stratName,shareCount,initialBalance,finalBalance,profit,percent)
			print('\n\t\t-> Individual Test Duration: '+str(round(time.time()-testStart,2))+' seconds')
			print('\t\t-> Test Batch Size: '+str(batchSize)+' days')
			print('\t\t-> Starting Account Balance: '+str(initialBalance))
			print('\t\t-> Final Account Balance: '+str(finalBalance))
			print('\t\t-> Profit: '+str(profit))
			print('\t\t-> Account Percent Change: '+str(percent)+'%')
		print('\n\t(Testing Block '+str(i+1)+' Time-Duration: '
			  +str(round(time.time()-testBlockStart,2))+' seconds)')
		if(i<(len(tickers)-1)): # Don't sleep after finishing last sublist
			print('\n(Sleeping 45 Seconds between test batches)')
			time.sleep(45)
	print('\t*Test Results written to \'data.txt\'')
	f.close()
	print('\t*Backtest Time-Duration: '+str(round(time.time()-backStart,2))+' seconds')

def sleeper(name,length):
	print('\n(NOTICE: Sleeping '+str(length)+' seconds after '+name+' backtest)')
	time.sleep(length)
	
if __name__ == '__main__':
	mainStart = time.time()
	print('(Initializing)')
	print('\t*Clearing \'data.txt\'')
	f = open('data.txt','w').close()
	testBalance = 5000.0 # $5,000.00 
	shares = 2.0
	#try:
	#	ticker = sys.argv[1].upper()
	#except:
	#	sys.exit('\t*Error: No ticker/symbol entered.')
	#if not ticker.isalpha():
	#	sys.exit('\t*Error: Non-letters entered for ticker/symbol/')
	# Moultiple Ticker Setup, up to 500 Calls per day, 5 calls per minute
	# Current Size = 12x5 = 60 
	tData = [
			 ['DIA','QQQ','SPY','IWM','VTI']
			 #['XLF','XLV','XLE','XLU','XLI'],
			 #['XLK','XLB','XLP','XLY','KBE'],
			 #['XME','XRT','XHB','KRE','XTL'],
			 #['XOM','URA','CANE','CPER','X'],
			 #['JNK','BND','LQD','HYG','TLT'],
			 #['VNQ','UAL','JETS','LUV','DAL'],
			 #['NFLX','BABA','FDX','DIS','PG'],
			 #['VALE','RIO','KALU','WPM','GOLD'],
			 #['GLD','SLV','PPLT','PALL','GLTR'],
			 #['FB','MSFT','AAPL','ADBE','NVDA'],
			 #['AMZN','GOOGL','TSLA','CMG','SHOP']
	]
	print('\t*Getting Alpaca API')
	api = alpaca.REST(AP_API_KEY,AP_API_SECRET,'https://paper-api.alpaca.markets',api_version='v2')
	#cancelOrders(api)
	#closePositions(api)
	#accountInfo(api)
	#getAlpacaQuote(api,tData[0][2]) # Bid/Ask Quote
	#marketOrder(api,ticker,shares)
	#backtest(AV_API_KEY,tData,testBalance,shares,holdStrategyTest)
	#sleeper('Hold',5)
	#backtest(AV_API_KEY,tData,testBalance,shares,emaStrategyTest)
	#sleeper('EMA',5)
	#backtest(AV_API_KEY,tData,testBalance,shares,demaStrategyTest)
	#sleeper('DEMA',5)
	backtest(AV_API_KEY,tData,testBalance,shares,rocStrategyTest)
	print('\n(\'main.py\' Execution Time: '+str(round(time.time()-mainStart,2))+' seconds)')