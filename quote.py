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
	
def getQuote(url):
	resp = requests.get(url)
	html = resp.text
	price = getPrice(html)
	print('\t Current Price: $',price)

def checkTicker(t):
		if not t.isalpha():
			sys.exit('Non-letters entered for ticker/symbol.')
	
if __name__ == '__main__':
	try:
		ticker = sys.argv[1].lower()
	except:
		sys.exit('No ticker/symbol entered.')
	
	stockUrl = 'https://marketwatch.com/investing/stock/'+ticker+'/historical'
	print('Fetching stock quote for '+ticker.upper()+'...')
	getQuote(stockUrl)