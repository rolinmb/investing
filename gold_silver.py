from alpha_vantage.timeseries import TimeSeries
from analysis import *
from config import *
import matplotlib.pylab as plt
import pandas as pd

def formatStockData(data):
	df = pd.DataFrame(data)
	cols = [i.split(' ')[1] for i in df.columns]
	df.columns = cols
	return df
	
if __name__ == '__main__':
	api = TimeSeries(AV_API_KEY,output_format='pandas')
	gData = api.get_daily(symbol='GLDM',outputsize='full')[0]
	sData = api.get_daily(symbol='SLV',outputsize='full')[0]
	gld = formatStockData(gData)
	slv = formatStockData(sData)
	gAverage = averagePrice(gld['open'],gld['high'],gld['low'],gld['close'])
	sAverage = averagePrice(slv['open'],slv['high'],slv['low'],slv['close'])
	ratio = gAverage/sAverage
	
	plt.figure(0)
	plt.title('GLDM/SLV Daily')
	plt.xlabel('Date')
	plt.ylabel('Ratio')
	plt.grid()
	plt.plot(ratio,label='GLDM/SLV')
	plt.plot(sma(ratio,100),label='100-SMA')
	plt.legend()
	plt.show()