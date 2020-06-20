from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
import sys

def sma(data,t):   # Simple Moving Average
	return data.rolling(t).mean()
	
def ema(data,t):   # Exponential Moving Average
	return data.ewm(span=t,adjust=False).mean()
	
def dema(data,t):  # Double-Exponential Moving Average
	e = ema(data,t)
	de = ema(e,t)
	return (2.0*e)-de

def roc(data,n):
	rates = []
	dates = data.index.values[n-1:]
	for i in range(n-1,data.size):
		rate = (data.iloc[i]-data.iloc[i-n])/data.iloc[i-n]
		rates.append(rate)
	
	return pd.Series(rates,index=data.index.values[n-1:])

def approxDeriv(data,n):
	approx = []
	rates = roc(data,n)
	for i in range(1,rates.size):
		if(i == rates.size-1):
			next = round(data.iloc[-1]+rates.iloc[-1],2)
			approx.append((next-data.iloc[-2])/2)
		else:
			deriv = (data.iloc[i+1]-data.iloc[i-1])/2
			approx.append(deriv)
			
	return pd.Series(approx,index=rates.index.values[1:])
	
	
def formatData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	return df

def checkTicker(t):
	if not t.isalpha():
		sys.exit('Non-letters entered for ticker/symbol.')

if __name__ == '__main__':
	# Anyone can use this key, AlphaVantage gives them out for free w/ no limits.
	key = 'K2CQV5DF42ONO1EY' 
	try:
		ticker = sys.argv[1].upper()
	except IndexError:
		sys.exit('No ticker/symbol entered.')
		
	checkTicker(ticker)
	ts = TimeSeries(key,output_format='pandas')
	print('Fetching data for ticker/symbol: '+ticker)
	try:
		data = ts.get_daily(symbol=ticker,outputsize='full')[0]
	except ValueError:
		sys.exit('Ticker is invalid/non-existant.')
	
	data = formatData(data)
	c = data['close']
	#o = data['open']
	#h = data['high']
	#l = data['low']
	#v = data['volume']
	print('Generating Charts:')
	
	plt.figure(0)
	plt.title(ticker+' Daily Close Price')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.grid()
	plt.plot(c,label='Close')
	plt.plot(sma(c,100),'-.',label='100-SMA')
	plt.plot(sma(c,50),'-.',label='50-SMA')
	plt.plot(ema(c,10),'--',label='10-EMA')
	plt.plot(dema(c,10),'--',label='10-DEMA')
	plt.legend()
	
	plt.figure(1)
	plt.title('Rates of Change for '+ticker)
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(roc(c,12),label='ROC(12)')
	plt.plot(roc(c,25),label='ROC(25)')
	plt.legend()

	plt.figure(2)
	plt.title('Finite-Difference approximation of derivative for '+ticker)
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.grid()
	plt.plot(approxDeriv(c,12),label='using f\' = ROC(12)')
	plt.plot(approxDeriv(c,25),label='using f\' = ROC(25)')
	plt.legend()
	
	plt.show()