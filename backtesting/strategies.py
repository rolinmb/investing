import pandas as pd
from analysis import *

def holdStrategyTest(data,t,initBalance,shareQty,displayStats):
	print('\n\t(Starting '+t+' Individual Buy & Hold Test)')
	cash = initBalance
	cash -= (data['close'].iloc[0]*shareQty)
	cash += (data['close'].iloc[-1]*shareQty)
	print('\n\t(Finished '+t+' Individual Buy & Hold Test)')
	if(displayStats):
		holdData = [initBalance,cash,data.size,round(cash-initBalance,2),round((100*(cash/initBalance))-100,2)]
		holdStatistics(holdData)
	return round(cash,2),data['close'].size
	
def smaStrategyTest(data,t,initBalance,shareQty,displayStats):
	print('\n\tStarting '+t+' Individual SMA-Test')
	cash = initBalance
	bearCount = bullCount = neutralCount = 0
	crossCount = crossSum = sinceCross = 0
	upCrosses = downCrosses = neutCrosses = 0
	signals = []
	crossDir = []
	crossDates = []
	crossLens = []
	inTrade = False
	sma25 = sma(data['close'],25)
	dema25 = dema(data['close'],25)
	prev = data['close'].index.values[0]
	for i in range(sma25.size):
		date = str(data['close'].index.values[i])[:10]
		price = data['close'].iloc[i]
		if(dema25.iloc[i]<sma25.iloc[i]):   # DEMA(25) < SMA(25)
			signals.append('Bearish')
			bearCount += 1
		elif(dema25.iloc[i]>sma25.iloc[i]): # DEMA(25) > SMA(25)
			signals.append('Bullish')
			bullCount += 1
		else:                               # DEMA(25) = SMA(25)
			signals.append('Neutral')
			neutralCount += 1
		if((i>0)and(signals[i]!=signals[i-1])):
			crossLens.append(sinceCross)
			crossDates.append(date)
			crossSum += sinceCross
			crossCount += 1
			sinceCross = 0
			tradeVal = round(price*shareQty,2)
			if(((signals[i-1]=='Bearish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bullish')):
				crossDir.append('Upward')     # Enter Trade
				upCrosses += 1
				if(not inTrade):
					inTrade = True
					cash -= tradeVal
			elif(((signals[i-1]=='Bullish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bearish')):
				crossDir.append('Downward')   # Exit Trade
				downCrosses += 1
				if(inTrade):
					inTrade = False
					cash+= tradeVal
			else:
				crossDir.append('Neutral')
				neutCrosses += 1
		prev = date
		sinceCross += 1
	if(inTrade):
		cash += (data['close'].iloc[-1]*shareQty)
	if(displayStats):
		statData = [[crossDates[-1],crossDir[-1],signals[-1]],
					[upCrosses,downCrosses,neutCrosses,crossSum,crossCount],
					[bullCount,bearCount,neutralCount]]
		smaStatistics(initBalance,cash,ema7.size,inTrade,statData)
	print('\n\t(Finished '+t+' Individual EMA Test)')
	return round(cash,2),sma25.size
	
	
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
	ema7 = ema(data['close'],7)
	ema25 = ema(data['close'],25)
	prev = data['close'].index.values[0]
	for i in range(ema7.size):
		date = str(data['close'].index.values[i])[:10]
		price = data['close'].iloc[i]
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
		cash += (data['close'].iloc[-1]*shareQty)
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
	ema21 = ema(data['close'],21)
	dema7 = dema(data['close'],7) 
	prev = data['close'].index.values[0]
	for i in range(dema7.size):
		date = str(data['close'].index.values[i])[:10]
		price = data['close'].iloc[i]
		if(dema7.iloc[i]<ema21.iloc[i]):   # EMA(21) > DEMA(7)
			signals.append('Bearish')
			bearCount += 1
		elif(dema7.iloc[i]>ema21.iloc[i]): # EMA(21) < DEMA(7)
			signals.append('Bullish')
			bullCount += 1
		else:                              # EMA(21) = DEMA(7)
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
				crossDir.append('Upward')   # Enter Trade
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
		cash += (data['close'].iloc[-1]*shareQty)
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
	roc7 = roc(ema(data['close'],7),12)
	roc25 = roc(ema(data['close'],25),12)
	offset = data['close'].size-roc25.size
	prev = data['close'].index.values[0+offset]
	for i in range (roc25.size):
		date = str(data['close'].index.values[i])[:10]
		price = data['close'].iloc[i+offset]
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
				crossDir.append('Upward')    # Enter Trade
				upCrosses += 1
				if(not inTrade):
					inTrade = True
					cash -= tradeVal
			elif(((signals[i-1]=='Bullish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bearish')):
				crossDir.append('Downward')  # Exit Trade
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
		cash += (data['close'].iloc[-1]*shareQty)
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
	trueStrength = tsi(data['close'],26,12)
	offset = data['close'].size-trueStrength.size
	prev = data['close'].index.values[0+offset]
	for i in range(trueStrength.size):
		date = str(data['close'].index.values[i])[:10]
		price = data['close'].iloc[i+offset]
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
		cash += (data['close'].iloc[-1]*shareQty)
	if(displayStats):
		statData = [[crossDates[-1],crossDir[-1],signals[-1]],
					[upCrosses,downCrosses,neutCrosses,crossSum,crossCount],
					[bullCount,bearCount,neutralCount]]
		tsiStatistics(initBalance,cash,tsi.size,inTrade,statData)
	print('\n\t(Finished '+t+' Individual TSI Test)')
	return round(cash,2),trueStrength.size
	
def cciStrategyTest(data,t,initBalance,shareQty,displayStats):
	print('\n\t(Starting '+t+' Individual CCI Test)')
	cash = initBalance
	bearCount = bullCount = neutralCount = 0
	crossCount = crossSum = sinceCross = 0
	upCrosses = downCrosses = neutCrosses = 0
	signals = []
	crossDir = []
	crossDates = []
	crossLens = []
	inTrade = False
	comChannel = cci(data['high'],data['low'],data['close'],20)
	ema18 = ema(comChannel,18)
	sma200 = sma(comChannel,200)
	prev = data['close'].index.values[0]
	for i in range(comChannel.size):
		date = str(data['close'].index.values[i])[:10]
		price = data['close'].iloc[i]
		if(ema18.iloc[i]<sma200.iloc[i]):   # EMA < SMA
			signals.append('Bearish')
			bearCount += 1
		elif(ema18.iloc[i]>sma200.iloc[i]): # EMA > SMA
			signals.append('Bullish')
			bullCount += 1
		else:								# EMA = SMA
			signals.append('Neutral')
			neutralCount += 1	
		if((i>0)and(signals[i]!=signals[i-1])): # Detect CCI MA Crossover
			tradeVal = price*shareQty
			crossLens.append(sinceCross)
			crossDates.append(date)
			crossSum += sinceCross
			crossCount += 1
			sinceCross = 0
			if(((signals[i-1]=='Bearish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bullish')):
				crossDir.append('Upward')     # Enter Trade
				upCrosses += 1
				if(not inTrade):
					inTrade = True
					cash -= tradeVal
			elif(((signals[i-1]=='Bullish')or(signals[i-1]=='Neutral'))and(signals[i]=='Bearish')):
				crossDir.append('Downward')   # Exit Trade
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
		cash += (data['close'].iloc[-1]*shareQty)
	if(displayStats):
		statData = [[crossDates[-1],crossDir[-1],signals[-1]],
					[upCrosses,downCrosses,neutCrosses,crossSum,crossCount],
					[bullCount,bearCount,neutralCount]]
		cciStatistics(initBalance,cash,tsi.size,inTrade,statData)
	print('\n\t(Finished '+t+' Individual CCI Test)')
	return round(cash,2),comChannel.size