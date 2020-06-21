import pandas as pd

def sma(data,t):
	return data.rolling(t).mean()
	
def ema(data,t):
	return data.ewm(span=t,adjust=False).mean()

def dema(data,t):
	e = ema(data,t)
	de = ema(e,t)
	return (2.0*e)-de
	
def roc(data,t):
	rates = []
	for i in range(t-1,data.size):
		rate = (data.iloc[i]-data.iloc[i-t])/data.iloc[i-t]
		rates.append(rate)
		
	return pd.Series(rates,index=data.index.values[t-1:])
	
def approxDeriv(data,t):
	approx = []
	rates = roc(data,t)
	for i in range(1,rates.size):
		if(i == rates.size-1):
			next = round(data.iloc[-1]+rates.iloc[-1],2)
			approx.append((next-data.iloc[-2])/2)
		else:
			deriv = (data.iloc[i+1]-data.iloc[i-1])/2
			approx.append((data.iloc[i+1]-data.iloc[i-1])/2)
	
	return pd.Series(approx,index=rates.index.values[1:])