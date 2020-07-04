from alpha_vantage.timeseries import TimeSeries
from config import *
from analysis import *
from strategies import *
from alpaca_util import *
import alpaca_trade_api as alpaca
import matplotlib.pyplot as plt
import pandas as pd
import time
import sys
	
def formatData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	return df
	
def fetchData(ts,t):	
	fetchStart = time.time()
	print('\n(Fetching AlphaVantage data for '+t+')')
	try:
		d = ts.get_daily(symbol=t,outputsize='full')[0]
		#d = ts.get_weekly(symbol=t)[0]	
	except ValueError:
		sys.exit('\t*Error: ticker/symbol '+t+' does not exist')
	print('\t*'+t+' Data obtained sucessfully in '+str(round(time.time()-fetchStart,2))+' seconds')
	return formatData(d)		

def writeData(file,t,funcName,shareCount,iBalance,fBalance,profit,percent):
	file.write(t+' '+funcName+' '+str(shareCount)+' '+str(iBalance)+' '+str(fBalance)+' '+str(profit)+' '+str(percent)+'\n')

def backtest(key,tickers,initialBalance,shareCount,strategyTest):
	backStart = time.time()
	getStatistics = False
	stratName = str(strategyTest.__name__)
	ts = TimeSeries(key,output_format='pandas')
	print('\n(Backtesting strategy using '+str(shareCount)+' share(s) over '+str(len(tickers)*len(tickers[0]))+' Stock(s)/ETF(s))')
	print('\t*Writing to \'data.txt\'')
	f = open('data.txt','a')
	for i in range(0,len(tickers)):
		testBlockStart = time.time()
		for t in tickers[i]:
			testStart = time.time()
			print('\n\t<-- Backtesting '+t+' w/ '+stratName+' -->')
			data = fetchData(ts,t)
			finalBalance,batchSize = strategyTest(data,t,initialBalance,shareCount,getStatistics)
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
			print('\n(Sleeping 58 Seconds between test batches)')
			time.sleep(58)
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
	try:
		ticker = sys.argv[1].upper()
	except IndexError:
		sys.exit('\t*Error: No ticker/symbol entered for first argument.')
	if not ticker.isalpha():
		sys.exit('\t*Error: Non-letters entered for ticker/symbol.')
	try:
		shares = float(sys.argv[2])
	except IndexError:
		sys.exit('\t*Error: Quantity of shares not entered for second argument.')
	except ValueError:
		sys.exit('\t*Error: Non-numerical characters entered for share quantity.')
	if(shares<=0.0):
		sys.exit('\t*Error: Negative/Zero share quantity entered.')
	try:
		testBalance = float(sys.argv[3])
	except IndexError:
		sys.exit('\t*Error: Initial Balance not entered for third argument.')
	except ValueError:
		sys.exit('\t*Error: Non-numerical characters entered for share quantity.')
	if(testBalance<=0.0):
		sys.exit('\t*Error: Negative/Zero initial balance entered.')
	# AlphaVantage API limits: 500/day, 5 calls/min
	tData = [[ticker]
			 #['DIA','QQQ','SPY','IWM','VTI']
			 #['XLF','XLV','XLE','XLU','XLI'],
			 #['XLK','XLB','XLP','XLY','KBE'],
			 #['XME','XRT','XHB','KRE','XTL'],
			 #['XOM','URA','CANE','CPER','X'],
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
	# Can only perform 5 single tests or a block of 5 tests before sleeping
	backtest(AV_API_KEY,tData,testBalance,shares,holdStrategyTest)  # Buy & Hold 
	#sleeper('Hold',58)
	backtest(AV_API_KEY,tData,testBalance,shares,smaStrategyTest)   # DEMA-25 & SMA-25
	#sleeper('SMA',58)
	backtest(AV_API_KEY,tData,testBalance,shares,emaStrategyTest)   # EMA-7 & EMA-25
	#sleeper('EMA',58)
	backtest(AV_API_KEY,tData,testBalance,shares,demaStrategyTest)  # EMA-21 & DEMA-7
	#sleeper('DEMA',58)
	backtest(AV_API_KEY,tData,testBalance,shares,rocStrategyTest)  # ROC(12)[EMA-7] & ROC(12)[EMA-25]
	#sleeper('ROC',58)
	#backtest(AV_API_KEY,tData,testBalance,shares,tsiStrategyTest)  # True Strength Index
	#sleeper('TSI',58)
	#backtest(AV_API_KEY,tData,testBalance,shares,cciStrategyTest)  # Commodity Channel Index
	print('\n(\'main.py\' Execution Time: '+str(round(time.time()-mainStart,2))+' seconds)')