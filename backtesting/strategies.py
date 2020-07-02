import pandas as pd
from analysis import *

def holdStrategyTest(data,t,initBalance,shareQty,displayStats):
	print('\n\t(Starting '+t+' Individual Buy & Hold Test)')
	cash = initBalance
	cash -= (data.iloc[0]*shareQty)
	cash += (data.iloc[-1]*shareQty)
	print('\n\t(Finished '+t+' Individual Buy & Hold Test)')
	if(displayStats):
		data = [initBalance,cash,data.size,round(cash-initBalance,2),round((100*(cash/initBalance))-100,2)]
		holdStatistics(data)
	return round(cash,2),data.size
	
def emaStrategyTest(data,t,initBalance,shareQty,displayStats):
	print('\n\t(Starting '+t+' Individual EMA-Test)')
	cash = initBalance
	bearCount = bullCount = neutralCount = 0
	crossCount = crossSum = sinceCross = 0
	upCrosses = downCrosses = neutCrosses = 0
	signals = []
	crossDir = []
	crossDates = []
	crossLens = []
	inTrade = False
	ema7 = ema(data,7)
	ema25 = ema(data,25)
	prev = data.index.values[0]
	for i in range(0,ema7.size):
		date = str(data.index.values[i])[:10]
		price = data.iloc[i]
		if(ema7.iloc[i]<ema25.iloc[i]):   # EMA(25) > EMA(7)
			signals.append('Bearish')
			bearCount += 1
		elif(ema7.iloc[i]>ema25.iloc[i]): # EMA(7) > EMA(25)
			signals.append('Bullish')
			bullCount += 1
		else:                             # EMA(7) = EMA(25)
			signals.append('Neutral')
			neutralCount += 1
		if((i>0)and(signals[i]!=signals[i-1])): # Handle EMA Crossover
			crossLens.append(sinceCross)
			crossDates.append(date)
			crossSum += sinceCross
			crossCount += 1
			sinceCross = 0
			tradeVal = round(price*shareQty,2)
			if(((signals[i-1]=='Bearish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bullish')):
				crossDir.append('Upward')  # Enter Trade
				upCrosses += 1
				if(not inTrade):
					inTrade = True
					cash -= tradeVal
			elif(((signals[i-1]=='Bullish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bearish')):
				crossDir.append('Downward') # Exit Trade
				downCrosses += 1
				if(inTrade):
					inTrade = False
					cash += tradeVal	
			else:
				crossDir.append('Neutral')
				neutCrosses += 1
		prev = date
		sinceCross += 1
	if(inTrade):
		cash += (data.iloc[-1]*shareQty)
	if(displayStats):
		statData = [[crossDates[-1],crossDir[-1],signals[-1]],
					[upCrosses,downCrosses,neutCrosses,crossSum,crossCount],
					[bullCount,bearCount,neutralCount]]
		emaStatistics(initBalance,cash,ema7.size,inTrade,statData)
	print('\n\t(Finished '+t+' Individual EMA Test)')
	return round(cash,2),ema7.size

def demaStrategyTest(data,t,initBalance,shareQty,displayStats):
	print('\n\t(Starting '+t+' Individual DEMA Test)')
	cash = initBalance
	bearCount = bullCount = neutralCount = 0
	crossCount = crossSum = sinceCross = 0
	upCrosses = downCrosses = neutCrosses = 0
	signals = []
	crossDir = []
	crossDates = []
	crossLens = []
	inTrade = False
	ema21 = ema(data,21)
	dema7 = dema(data,7) 
	prev = data.index.values[0]
	for i in range(0,dema7.size):
		date = str(data.index.values[i])[:10]
		price = data.iloc[i]
		if(dema7.iloc[i]<ema21.iloc[i]):   # EMA(21) > DEMA(7)
			signals.append('Bearish')
			bearCount += 1
		elif(dema7.iloc[i]>ema21.iloc[i]): # EMA(21) < DEMA(7)
			signals.append('Bullish')
			bullCount += 1
		else:                             # EMA(21) = DEMA(7)
			signals.append('Neutral')
			neutralCount += 1
		if((i>0)and(signals[i]!=signals[i-1])): # Catch Crossover
			crossLens.append(sinceCross)
			crossDates.append(date)
			crossSum += sinceCross
			crossCount += 1
			sinceCross = 0
			tradeVal = round(price*shareQty,2)
			if(((signals[i-1]=='Bearish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bullish')):
				crossDir.append('Upward')  # Enter Trade
				upCrosses += 1
				if(not inTrade):
					inTrade = True
					cash -= tradeVal
			elif(((signals[i-1]=='Bullish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bearish')):
				crossDir.append('Downward') # Exit Trade
				downCrosses += 1
				if(inTrade):
					inTrade = False
					cash += tradeVal
			else:
				crossDir.append('Neutral')
				neutCrosses += 1
		prev = date
		sinceCross += 1
	if(inTrade):
		cash += (data.iloc[-1]*shareQty)
	if(displayStats):
		statData = [[crossDates[-1],crossDir[-1],signals[-1]],
					[upCrosses,downCrosses,neutCrosses,crossSum,crossCount],
					[bullCount,bearCount,neutralCount]]
		demaStatistics(initBalance,cash,ema7.size,inTrade,statData)
	print('\n\t(Finished '+t+' Individual DEMA Test)')
	return round(cash,2),dema7.size
	
def rocStrategyTest(data,t,initBalance,shareQty,displayStats):
	print('\n\t(Starting '+t+' Individual ROC Test)')
	cash = initBalance 
	bearCount = bullCount = neutralCount = 0
	crossCount = crossSum = sinceCross = 0
	upCrosses = downCrosses = neutCrosses = 0
	signals = []
	crossDir = []
	crossDates = []
	crossLens = []
	inTrade = False
	roc7 = roc(ema(data,7),12)
	roc25 = roc(ema(data,25),12)
	offset = data.size-roc25.size
	prev = data.index.values[0+offset]
	for i in range (0,roc25.size):
		date = str(data.index.values[i])[:10]
		price = data.iloc[i+offset]
		if(roc7.iloc[i]<roc25.iloc[i] ):  # ROC12(EMA(25)) > ROC12(EMA(7))
			signals.append('Bearish')
			bearCount += 1
		elif(roc7.iloc[i]>roc25.iloc[i]): # ROC12(EMA(7)) > ROC12(EMA(25))
			signals.append('Bullish')
			bullCount += 1
		else:
			signals.append('Neutral')     # ROC12(EMA(7)) = ROC12(EMA(25))
			neutralCount += 1
		if((i>0)and(signals[i]!=signals[i-1])): # Handle ROC Crossover
			tradeVal = price*shareQty
			crossLens.append(sinceCross)
			crossDates.append(date)
			crossSum += sinceCross
			crossCount += 1
			sinceCross = 0
			if(((signals[i-1]=='Bearish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bullish')):
				crossDir.append('Upward')  # Enter Trade
				upCrosses += 1
				if(not inTrade):
					inTrade = True
					cash -= tradeVal
			elif(((signals[i-1]=='Bullish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bearish')):
				crossDir.append('Downward') # Exit Trade
				downCrosses += 1
				if(inTrade):
					inTrade = False
					cash += tradeVal
			else:
				crossDir.append('Neutral')
				neutCrosses += 1
		prev = date
		sinceCross += 1
	if(inTrade):
		cash += (data.iloc[-1]*shareQty)
	if(displayStats):
		statData = [[crossDates[-1],crossDir[-1],signals[-1]],
					[upCrosses,downCrosses,neutCrosses,crossSum,crossCount],
					[bullCount,bearCount,neutralCount]]
		rocStatistics(initBalance,cash,roc25.size,inTrade,statData)
	print('\n\t(Finished '+t+' Individual ROC Test)')
	return round(cash,2),roc25.size
	
def tsiStrategyTest(data,t,initBalance,shareQty,displayStats):
	print('\n\t(Starting '+t+' Individual TSI Test)')
	cash = initBalance
	bearCount = bullCount = neutralCount = 0
	crossCount = crossSum = sinceCross = 0
	upCrosses = downCrosses = neutCrosses = 0
	signals = []
	crossDir = []
	crossDates = []
	crossLens = []
	inTrade = False
	trueStrength = tsi(data,26,12)
	offset = data.size-trueStrength.size
	prev = data.index.values[0+offset]
	for i in range(0,trueStrength.size):
		date = str(data.index.values[i])[:10]
		price = data.iloc[i+offset]
		if(trueStrength[i]<0.0):
			signals.append('Bearish')  # TSI < 0
			bearCount += 1
		elif(trueStrength[i]>0.0):
			signals.append('Bullish')  # TSI > 0
			bullCount += 1
		else:
			signals.append('Neutral')  # TSI = 0
			neutralCount += 1
		if((i>0)and(signals[i]!=signals[i-1])):
			tradeVal = price*shareQty
			crossLens.append(sinceCross)
			crossDates.append(date)
			crossSum += sinceCross
			crossCount += 1
			sinceCross = 0
			if(((signals[i-1]=='Bearish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bullish')):
				crossDir.append('Upward')  # Enter Trade
				upCrosses += 1
				if(not inTrade):
					inTrade = True
					cash -= tradeVal
			elif(((signals[i-1]=='Bullish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bearish')):
				crossDir.append('Downward') # Exit Trade
				downCrosses += 1
				if(inTrade):
					inTrade = False
					cash += tradeVal
			else:
				crossDir.append('Neutral')
				neutCrosses += 1
		prev = date
		sinceCross += 1
	if(inTrade):
		cash += (data.iloc[-1]*shareQty)
	if(displayStats):
		statData = [[crossDates[-1],crossDir[-1],signals[-1]],
					[upCrosses,downCrosses,neutCrosses,crossSum,crossCount],
					[bullCount,bearCount,neutralCount]]
		tsiStatistics(initBalance,cash,tsi.size,inTrade,statData)
	print('\n\t(Finished '+t+' Individual TSI Test)')
	return round(cash,2),trueStrength.size