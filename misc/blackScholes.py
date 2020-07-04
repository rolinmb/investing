from scipy.stats import norm
import matplotlib.pylab as plt
import numpy as np
# Cuumulative Distribution Formula
def cdf(x): # N(x)
	return norm.cdf(x,0.0,1.0)
	
def ln(x):
	return np.log(x)
	
def e(x):
	return np.exp(x)
# Probablility Density Function
def pdf(x): # N'(x)
	return norm.pdf(x,0.0,1.0)
	#return (1/np.sqrt(2*np.pi))*e(-((x**2)/2))
	
def pv(K,T,r):
	return K*e(-r*T)
	
def getParams(S,K,T,r,s):
	d1 = (ln(S/K)+(r+(0.5*(s**2))))/(s*np.sqrt(T))
	d2 = (ln(S/K)+(r-(0.5*(s**2))))/(s*np.sqrt(T))
	return d1,d2
	
def callOption(S,K,T,r,s):
	d1,d2 = getParams(S,K,T,r,s)
	return round((S*cdf(d1))-(pv(K,T,r)*cdf(d2)),3)

def putOption(S,K,T,r,s):
	d1,d2 = getParams(S,K,T,r,s)
	return round((pv(K,T,r)*cdf(-d2))-(S*cdf(-d2)),3)
		
def callDelta(S,K,T,r,s):
	d1 = getParams(S,K,T,r,s)[0]
	return round(cdf(d1),3)

def putDelta(S,K,T,r,s):
	return round(callDelta(S,K,T,r,s)-1.0,3)

def callGamma(S,K,T,r,s):
	d1 = getParams(S,K,T,r,s)[0]
	nPrime = pdf(d1)
	denom = S*(s*np.sqrt(T))
	return round(nPrime/denom,3)
	
def putGamma(S,K,T,r,s):
	return callGamma(S,K,T,r,s)
	
def callVega(S,K,T,r,s):
	d1 = getParams(S,K,T,r,s)[0]
	nPrime = pdf(d1)
	return round(S*(nPrime*np.sqrt(T)),3)

def putVega(S,K,T,r,s):
	return callVega(S,K,T,r,s)
	
def callTheta(S,K,T,r,s):
	d1,d2 = getParams(S,K,T,r,s)
	n = cdf(d2)
	nPrime = pdf(d1)
	lhs = ((-S*(nPrime*s))/(2.0*np.sqrt(T)))
	rhs = r*(pv(K,T,r)*n)
	return round(lhs-rhs,3)
	
def putTheta(S,K,T,r,s):
	d1,d2 = getParams(S,K,T,r,s)
	n = cdf(-d2)
	nPrime = pdf(d1)
	lhs = ((-S*(nPrime*s))/(2.0*np.sqrt(T)))
	rhs = r*(pv(K,T,r)*n)
	return round(lhs+rhs,3)
	
def callRho(S,K,T,r,s):
	d2 = getParams(S,K,T,r,s)[1]
	n = cdf(d2)
	return round((T*(pv(K,T,r)*n)),3)
	
def putRho(S,K,T,r,s):
	d2 = getParams(S,K,T,r,s)[1]
	n = cdf(-d2)
	return round((-T*(pv(K,T,r)*n)),3)
	
if __name__ == '__main__':
	S = 75    		# Spot Price
	K = 75   		# Strike Price
	T = 1     		# Time to maturity/expiry (yrs) (T>0)
	r = 0.05  		# Risk-Free Interest Rate
	sigma = 0.25    # Volatility/Standard Deviation
	putValsA = []
	putValsB = []
	putValsC = []
	callValsA = []
	callValsB = []
	callValsC = []
	iter = [i for i in range(1,366)]
	time = [n/365 for n in iter[::-1]] # Value over a year, starting at 1.0 yrs
	priceUp = 70.0
	priceDown = 80.0
	for t in time:
		# Options which the underlying stays at $75
		putValsA.append(putOption(S,K,t,r,sigma))
		callValsA.append(callOption(S,K,t,r,sigma))
		# Options which the underlying moves $70 -> $80
		putValsB.append(putOption(priceUp,K,t,r,sigma))
		callValsB.append(callOption(priceUp,K,t,r,sigma))
		# Options which the underlying moves $80 -> $70
		putValsC.append(putOption(priceDown,K,t,r,sigma))
		callValsC.append(callOption(priceDown,K,t,r,sigma))
		priceUp += 0.02739
		priceDown -= 0.02739
	
	plt.figure(0)
	plt.title('75 Strike Options')
	plt.xlabel('Days til Expiration')
	plt.xlim(366,0)
	plt.ylabel('Value of Contract')
	plt.grid()
	plt.plot(iter[::-1],putValsA,label='Put ATM->ATM')
	plt.plot(iter[::-1],putValsB,label='Put ITM->OTM')
	plt.plot(iter[::-1],putValsC,label='Put OTM->ITM')
	plt.plot(iter[::-1],callValsA,label='Call ATM->ATM')
	plt.plot(iter[::-1],callValsB,label='Call OTM->ITM')
	plt.plot(iter[::-1],callValsC,label='Call ITM->OTM')
	plt.legend()
	plt.show()
	'''
	print('\nCall Value:',callOption(S,K,T,r,sigma))
	print('\t-> Call Delta:',callDelta(S,K,T,r,sigma))
	print('\t-> Call Gamma:',callGamma(S,K,T,r,sigma))
	print('\t-> Call Vega:',callVega(S,K,T,r,sigma))
	print('\t-> Call Theta:',callTheta(S,K,T,r,sigma))
	print('\t-> Call Rho:',callRho(S,K,T,r,sigma))
	print('Put Value:',putOption(S,K,T,r,sigma))
	print('\t-> Put Delta:',putDelta(S,K,T,r,sigma))
	print('\t-> Put Gamma:',putGamma(S,K,T,r,sigma))
	print('\t-> Put Vega:',putVega(S,K,T,r,sigma))
	print('\t-> Put Theta:',putTheta(S,K,T,r,sigma))
	print('\t-> Put Rho:',putRho(S,K,T,r,sigma))'''