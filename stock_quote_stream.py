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

def checkArgs(t,n):
	if not t.isalpha():
		sys.exit('Non-letters entered for ticker/symbol.')
	if n <= 0:
		sys.exit('Zero or negative entered for quote count.')

def checkExist(url):
	resp = requests.get(url)
	html = resp.text
	try:
		p = getPrice(html) 
	except ValueError:
		sys.exit('Invalid ticker entered.')

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
		sys.exit('Invalid entry for quote count.')
	
	checkArgs(ticker,count)
	stockUrl = 'https://marketwatch.com/investing/stock/'+ticker+'/historical'
	checkExist(stockUrl)
	print('Fetching '+str(count)+' quotes for '+ticker.upper()+'...')
	start = time.time()
	streamQuotes(stockUrl,count)
	end = time.time()
	print('Query Time: '+str(round(float(end-start),3))+'s')