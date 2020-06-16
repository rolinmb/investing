from bs4 import BeautifulSoup
import requests
import sys
import re

def stripCommas(s):
	return re.sub(',(?!\s+\d$)','',s)
	
def parsePrice(html):
	soup = BeautifulSoup(html,'html.parser')
	valStr = soup.find_all('p',class_='data bgLast')
	content = [c.text for c in valStr]
	return float(stripCommas(''.join(content)))
	
def getQuote(url):
	resp = requests.get(url)
	html = resp.text
	price = parsePrice(html)
	print('\t Current Price: $',price)

def checkArg(t):
	if not t.isalpha():
		sys.exit('Non-letters entered for ticker/symbol.')
	
def checkExist(url):
	resp = requests.get(url)
	html = resp.text
	try:
		p = parsePrice(html)
	except ValueError:
		sys.exit('Invalid ticker entered.')
	
if __name__ == '__main__':
	try:
		ticker = sys.argv[1].lower()
	except IndexError:
		sys.exit('No ticker/symbol entered.')

	checkArg(ticker)
	stockUrl = 'https://marketwatch.com/investing/stock/'+ticker+'/historical'
	checkExist(stockUrl)
	print('Fetching stock quote for '+ticker.upper()+'...')
	getQuote(stockUrl)