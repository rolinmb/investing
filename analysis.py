import pandas as pd

def holdStatistics(data):
	print('\n\t\t<- FINAL STRATEGY STATS ->')
	print('\t\t-> Hold Strategy Initial Balance: '+str(data[0]))
	print('\t\t-> Hold Strategy Final Balance: '+str(round(data[1],2)))
	print('\t\t-> Dataset Size: '+str(data[2]))
	print('\t\t-> Profit/Loss from Hold Strategy: '+str(data[3]))
	print('\t\t-> Percent Return from Hold Strategy: '+str(data[4])+'%')

def smaStatistics(initBalance,cash,size,inTrade,data):
	change = round(cash-initBalance,2)
	percent = round((100*(cash/initBalance))-100,2)
	print('\n\t\t<- GENERAL STATS ->')
	print('\t\t-> Dataset Size: '+str(size))
	print('\t\t-> Most recent Cross Date: '+data[0][0])
	print('\t\t-> Most recent Cross Direction: '+data[0][1])
	print('\t\t-> Most recent SMA Signal: '+data[0][2])
	print('\n\t\t<- CROSSING STATS ->')
	print('\t\t-> # of Upward/Bullish Crosses:',data[1][0])
	print('\t\t-> # of Downward/Bearish Crosses:',data[1][1])
	print('\t\t-> # of Neutral Crossings:',data[1][2])
	print('\t\t-> Upward/Downward Crossing Ratio:',round((data[1][0]/data[1][1]),2))
	print('\t\t-> Average Days Between Crossings:',round((data[1][3]/data[1][4]),2))
	print('\n\t\t<- SMA STATS ->')
	print('\t\t-> Bull SMA Days:',data[2][0])
	print('\t\t-> Bear SMA Days:',data[2][1])
	print('\t\t-> Neutral SMA Days:',data[2][2])
	print('\t\t-> % of SMA Days Bullish:',round(100*(data[2][0]/size),2))
	print('\t\t-> % of SMA Days Bearish:',round(100*(data[2][1]/size),2))
	print('\t\t-> % of SMA Days Neutral:',round(100*(data[2][2]/size),2))
	print('\n\t\t<- FINAL STRATEGY STATS ->')
	print('\t\t-> Holding stock at end? '+str(inTrade))
	print('\t\t-> SMA Strategy Initial Balance: '+str(initBalance))
	print('\t\t-> SMA Strategy Final Balance: '+str(round(cash,2)))
	print('\t\t-> Profit/Loss from SMA Strategy: '+str(change))
	print('\t\t-> Percent Return from SMA Strategy: '+str(percent)+'%')
	
def emaStatistics(initBalance,cash,size,inTrade,data):
	change = round(cash-initBalance,2)
	percent = round((100*(cash/initBalance))-100,2)
	print('\n\t\t<- GENERAL STATS ->')
	print('\t\t-> Dataset Size: '+str(size))
	print('\t\t-> Most recent Cross Date: '+data[0][0])
	print('\t\t-> Most recent Cross Direction: '+data[0][1])
	print('\t\t-> Most recent EMA Signal: '+data[0][2])
	print('\n\t\t<- CROSSING STATS ->')
	print('\t\t-> # of Upward/Bullish Crosses:',data[1][0])
	print('\t\t-> # of Downward/Bearish Crosses:',data[1][1])
	print('\t\t-> # of Neutral Crossings:',data[1][2])
	print('\t\t-> Upward/Downward Crossing Ratio:',round((data[1][0]/data[1][1]),2))
	print('\t\t-> Average Days Between Crossings:',round((data[1][3]/data[1][4]),2))
	print('\n\t\t<- EMA STATS ->')
	print('\t\t-> Bull EMA Days:',data[2][0])
	print('\t\t-> Bear EMA Days:',data[2][1])
	print('\t\t-> Neutral EMA Days:',data[2][2])
	print('\t\t-> % of EMA Days Bullish:',round(100*(data[2][0]/size),2))
	print('\t\t-> % of EMA Days Bearish:',round(100*(data[2][1]/size),2))
	print('\t\t-> % of EMA Days Neutral:',round(100*(data[2][2]/size),2))
	print('\n\t\t<- FINAL STRATEGY STATS ->')
	print('\t\t-> Holding stock at end? '+str(inTrade))
	print('\t\t-> EMA Strategy Initial Balance: '+str(initBalance))
	print('\t\t-> EMA Strategy Final Balance: '+str(round(cash,2)))
	print('\t\t-> Profit/Loss from EMA Strategy: '+str(change))
	print('\t\t-> Percent Return from EMA Strategy: '+str(percent)+'%')
	
def demaStatistics(initBalance,cash,size,inTrade,data):
	change = round(cash-initBalance,2)
	percent = round((100*(cash/initBalance))-100,2)
	print('\n\t\t<- GENERAL STATS ->')
	print('\t\t-> Dataset Size: '+str(size))
	print('\t\t-> Most recent Cross Date: '+data[0][0])
	print('\t\t-> Most recent Cross Direction: '+data[0][1])
	print('\t\t-> Most recent DEMA Signal: '+data[0][2])
	print('\n\t\t<- CROSSING STATS ->')
	print('\t\t-> # of Upward/Bullish Crosses:',data[1][0])
	print('\t\t-> # of Downward/Bearish Crosses:',data[1][1])
	print('\t\t-> # of Neutral Crossings:',data[1][2])
	print('\t\t-> Upward/Downward Crossing Ratio:',round((data[1][0]/data[1][1]),2))
	print('\t\t-> Average Days Between Crossings:',round((data[1][3]/data[1][4]),2))
	print('\n\t\t<- DEMA STATS ->')
	print('\t\t-> Bull DEMA Days:',data[2][0])
	print('\t\t-> Bear DEMA Days:',data[2][1])
	print('\t\t-> Neutral DEMA Days:',data[2][2])
	print('\t\t-> % of DEMA Days Bullish:',round(100*(data[2][0]/size),2))
	print('\t\t-> % of DEMA Days Bearish:',round(100*(data[2][1]/size),2))
	print('\t\t-> % of DEMA Days Neutral:',round(100*(data[2][2]/size),2))
	print('\n\t\t<- FINAL STRATEGY STATS ->')
	print('\t\t-> Holding stock at end? '+str(inTrade))
	print('\t\t-> DEMA Strategy Initial Balance: '+str(initBalance))
	print('\t\t-> DEMA Strategy Final Balance: '+str(round(cash,2)))
	print('\t\t-> Profit/Loss from DEMA Strategy: '+str(change))
	print('\t\t-> Percent Return from DEMA Strategy: '+str(percent)+'%')
	
def rocStatistics(initBalance,cash,size,inTrade,data):
	change = round(cash-10000.00,2)
	percent = round((100*(cash/10000.00))-100,2)
	print('\n\t\t<- GENERAL STATS ->')
	print('\t\t-> Dataset Size: '+str(size))
	print('\t\t-> Most recent Cross Date: '+data[0][0])
	print('\t\t-> Most recent Cross Direction: '+data[0][1])
	print('\t\t-> Most recent ROC Signal: '+data[0][2])
	print('\n\t\t<- CROSSING STATS ->')
	print('\t\t-> # of Upward/Bullish Crosses:',data[1][0])
	print('\t\t-> # of Downward/Bearish Crosses:',data[1][1])
	print('\t\t-> # of Neutral Crossings:',data[1][2])
	print('\t\t-> Upward/Downward Crossing Ratio:',round((data[1][0]/data[1][1]),2))
	print('\t\t-> Average Days Between Crossings:',round((data[1][3]/data[1][4]),2))
	print('\n\t\t<- ROC STATS ->')
	print('\t\t-> Bull ROC Days:',data[2][0])
	print('\t\t-> Bear ROC Days:',data[2][1])
	print('\t\t-> Neutral ROC Days:',data[2][2])
	print('\t\t-> % of ROC Days Bullish:',round(100*(data[2][0]/size),2))
	print('\t\t-> % of ROC Days Bearish:',round(100*(data[2][1]/size),2))
	print('\t\t-> % of ROC Days Neutral:',round(100*(data[2][2]/size),2))
	print('\n\t\t<- FINAL STRATEGY STATS ->')
	print('\t\t-> Holding stock at end? '+str(inTrade))
	print('\t\t-> ROC Strategy Initial Balance: '+str(initBalance))
	print('\t\t-> ROC Strategy Final Balance: '+str(round(cash,2)))
	print('\t\t-> Profit/Loss from ROC Strategy: '+str(change))
	print('\t\t-> Percent Return from ROC Strategy: '+str(percent)+'%')
	
def tsiStatistics(initBalance,cash,size,inTrade,data):
	change = round(cash-10000.00,2)
	percent = round((100*(cash/10000.00))-100,2)
	print('\n\t\t<- GENERAL STATS ->')
	print('\t\t-> Dataset Size: '+str(size))
	print('\t\t-> Most recent Cross Date: '+data[0][0])
	print('\t\t-> Most recent Cross Direction: '+data[0][1])
	print('\t\t-> Most recent TSI Signal: '+data[0][2])
	print('\n\t\t<- CROSSING STATS ->')
	print('\t\t-> # of Upward/Bullish Crosses:',data[1][0])
	print('\t\t-> # of Downward/Bearish Crosses:',data[1][1])
	print('\t\t-> # of Neutral Crossings:',data[1][2])
	print('\t\t-> Upward/Downward Crossing Ratio:',round((data[1][0]/data[1][1]),2))
	print('\t\t-> Average Days Between Crossings:',round((data[1][3]/data[1][4]),2))
	print('\n\t\t<- TSI STATS ->')
	print('\t\t-> Bull TSI Days:',data[2][0])
	print('\t\t-> Bear TSI Days:',data[2][1])
	print('\t\t-> Neutral TSI Days:',data[2][2])
	print('\t\t-> % of TSI Days Bullish:',round(100*(data[2][0]/size),2))
	print('\t\t-> % of TSI Days Bearish:',round(100*(data[2][1]/size),2))
	print('\t\t-> % of TSI Days Neutral:',round(100*(data[2][2]/size),2))
	print('\n\t\t<- FINAL STRATEGY STATS ->')
	print('\t\t-> Holding stock at end? '+str(inTrade))
	print('\t\t-> TSI Strategy Initial Balance: '+str(initBalance))
	print('\t\t-> TSI Strategy Final Balance: '+str(round(cash,2)))
	print('\t\t-> Profit/Loss from TSI Strategy: '+str(change))
	print('\t\t-> Percent Return from TSI Strategy: '+str(percent)+'%')
	
def cciStatistics(initBalance,cash,size,inTrade,data):
	change = round(cash-10000.00,2)
	percent = round((100*(cash/10000.00))-100,2)
	print('\n\t\t<- GENERAL STATS ->')
	print('\t\t-> Dataset Size: '+str(size))
	print('\t\t-> Most recent Cross Date: '+data[0][0])
	print('\t\t-> Most recent Cross Direction: '+data[0][1])
	print('\t\t-> Most recent CCI Signal: '+data[0][2])
	print('\n\t\t<- CROSSING STATS ->')
	print('\t\t-> # of Upward/Bullish Crosses:',data[1][0])
	print('\t\t-> # of Downward/Bearish Crosses:',data[1][1])
	print('\t\t-> # of Neutral Crossings:',data[1][2])
	print('\t\t-> Upward/Downward Crossing Ratio:',round((data[1][0]/data[1][1]),2))
	print('\t\t-> Average Days Between Crossings:',round((data[1][3]/data[1][4]),2))
	print('\n\t\t<- CCI STATS ->')
	print('\t\t-> Bull CCI Days:',data[2][0])
	print('\t\t-> Bear CCI Days:',data[2][1])
	print('\t\t-> Neutral CCI Days:',data[2][2])
	print('\t\t-> % of CCI Days Bullish:',round(100*(data[2][0]/size),2))
	print('\t\t-> % of CCI Days Bearish:',round(100*(data[2][1]/size),2))
	print('\t\t-> % of CCI Days Neutral:',round(100*(data[2][2]/size),2))
	print('\n\t\t<- FINAL STRATEGY STATS ->')
	print('\t\t-> Holding stock at end? '+str(inTrade))
	print('\t\t-> CCI Strategy Initial Balance: '+str(initBalance))
	print('\t\t-> CCI Strategy Final Balance: '+str(round(cash,2)))
	print('\t\t-> Profit/Loss from CCI Strategy: '+str(change))
	print('\t\t-> Percent Return from CCI Strategy: '+str(percent)+'%')
	
def standardDeviations(data): # Rolling Standard Deviation
	devs = []
	for i in range(0,data.size):
		devs.append(data.iloc[data.size-(i+1):data.size].std())

	return pd.Series(devs,index=data.index.values)

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
	
def tsi(c,r,s):
	mom = []
	for i in range(1,c.size):
		m = c.iloc[i]-c.iloc[i-1]
		mom.append(m)
		
	mom = pd.Series(mom,index=c.index.values[1:])
	ema1 = ema(ema(mom,r),s)
	ema2 = ema(ema(abs(mom),r),s)
	return 100*(ema1/ema2)
	
def cci(h,l,c,n):
	tp = typicalPrice(h,l,c)
	ma = sma(tp,n)
	std = tp.rolling(n).std()
	return pd.Series(((tp-ma)/(.015*std)),index=tp.index.values)