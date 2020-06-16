from bs4 import BeautifulSoup
import requests
import time
import sys
import re

def stripCommas(s):
	return re.sub(',(?!\s+\d$)','',s)

def getPrice(html):
	soup = BeautifulSoup(html,'html.parser')
	val = soup.find_all('p',class_='data bgLast')
	content = [c.text for c in val]
	return float(stripCommas(''.join(content)))

def streamQuotes(url,num):
	sesh = requests.session()
	for n in range(0,num):
		resp = sesh.get(url)
		html = resp.text
		price = getPrice(html)
		print('\t('+str(n+1)+') Current Price: $',price)
	sesh.close()

def checkTicker(t):
	if not t.isalpha():
		sys.exit('Non-letters entered for ticker/symbol.')
	
def checkCount(n):
	if n <= 0:
		sys.exit('Zero or negative entered for quote count.')
	
if __name__ == '__main__':
	try:
		ticker = sys.argv[1].lower()
	except IndexError:
		sys.exit('No ticker/symbol entered.')
	try:
		count = int(sys.argv[2])
	except IndexError:
		sys.exit('No quote count entered.')
	except ValueError:
		sys.exit('Decimal entered as quote count.')
	
	checkTicker(ticker)
	checkCount(count)
	stockUrl = 'https://marketwatch.com/investing/stock/'+ticker+'/historical'
	print('Fetching '+str(count)+' quoted for '+ticker.upper()+'...')
	streamQuotes(stockUrl,count)
	end = time.time()
	print('Query Time: '+str(round(float(end-start),3))+'s')