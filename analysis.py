import pandas as pd

def sma(data,t):    # Simple Moving Average
	return data.rolling(t).mean()
	
def ema(data,t):    # Exponential Moving Average
	return data.ewm(span=t,adjust=False).mean()

def dema(data,t):   # Double-Exponential Moving Average
	e = ema(data,t)
	de = ema(e,t)
	return (2.0*e)-de
	
def roc(data,t):    # Rate-of-Change Indicator
	rates = []
	for i in range(t-1,data.size):
		rate = (data.iloc[i]-data.iloc[i-t])/data.iloc[i-t]
		rates.append(rate)
		
	return pd.Series(rates,index=data.index.values[t-1:])
	
def approxDeriv(data,t): # Finite-Difference Approximation of 1st Derivative
	approx = []
	rates = roc(data,t)
	for i in range(1,rates.size):
		if(i == rates.size-1):
			next = round(data.iloc[-1]+rates.iloc[-1],2)
			approx.append((next-data.iloc[-2])/2)
		else:
			approx.append((data.iloc[i+1]-data.iloc[i-1])/2)
	
	return pd.Series(approx,index=rates.index.values[1:])
	
def typicalPrice(h,l,c):  # Typical Price of asset
	return (h+l+c)/3
	
def averagePrice(o,h,l,c): # Average Price of Open, High, Low, Close
	return (o+h+l+c)/4
	
def macd(data):
	ema12 = ema(data,12)
	ema26 = ema(data,26)
	macdLine = ema12-ema26
	signal = ema(macdLine,9)
	return macdLine,signal