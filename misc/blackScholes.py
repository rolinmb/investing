from scipy.stats import norm
import numpy as np
	
def cdf(x): # N(x)
	return norm.cdf(x,0.0,1.0)
	
def pdf(x): # N'(x)
	return norm.pdf(x,0.0,1.0)
	
def ln(x):
	return np.log(x)
	
def e(x):
	return np.exp(x)
	
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
	T = 0.1     	# Time to maturity/expiry (years)
	r = 0.05  		# Risk-Free Interest Rate
	sigma = 0.25    # Volatility/Standard Deviation
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
	print('\t-> Put Rho:',putRho(S,K,T,r,sigma))