from alpha_vantage.cryptocurrencies import CryptoCurrencies
from analysis import *
from config import *
import matplotlib.pyplot as plt
import pandas as pd

def formatCryptoData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	return df.T.drop_duplicates().T
	
if __name__ == '__main__':
	api = CryptoCurrencies(AV_API_KEY,output_format='pandas')
	bData = api.get_digital_currency_daily(symbol='BTC',market='USD')[0]
	tData = api.get_digital_currency_daily(symbol='XTZ',market='USD')[0]
	btc = formatCryptoData(bData)
	xtz = formatCryptoData(tData)
	bAverage = averagePrice(btc['open'],btc['high'],btc['low'],btc['close'])
	tAverage = averagePrice(xtz['open'],xtz['high'],xtz['low'],xtz['close'])
	ratio = bAverage/tAverage
	
	plt.figure(0)
	plt.title('Bitcoin/Tezos Daily (USD-Derived)')
	plt.xlabel('Date')
	plt.ylabel('Ratio')
	plt.grid()
	plt.plot(ratio,label='BTC/XTZ')
	plt.plot(sma(ratio,100),'--',label='100-SMA')
	plt.legend()
	plt.show()