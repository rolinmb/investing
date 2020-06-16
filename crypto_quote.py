from bs4 import BeautifulSoup
import requests
import sys
import re

def stripCommas(s):
	return re.sub(',(?!\s+\d$)','',s)

def parseRate(html):
	soup = BeautifulSoup(html,'html.parser')
	valStr = soup.find_all('p',class_='data bgLast')
	content = [c.text for c in valStr]
	return float(stripCommas(''.join(content)))

def getQuote(url):
	resp = requests.get(url)
	html = resp.text
	rate = parseRate(html)
	print('\t Current Rate: ',rate)

def checkArgs(c,m):
	if not c.isalpha():
		sys.exit('Non-letters entered for coin symbol.')
	if not m.isalpha():
		sys.exit('Non-letters entered for currency type.')

def checkPair(url):
	resp = requests.get(url)
	html = resp.text
	try:
		r = parseRate(html)
	except ValueError:
		sys.exit('Cryptocurrency or pair entered does not exist.')
		
if __name__ == '__main__':
	try:
		coin = sys.argv[1].upper()
	except IndexError:
		sys.exit('No coin/symbol entered.')
	try:
		mkt = sys.argv[2].upper()
	except IndexError:
		sys.exit('No relative currency entered.')
	
	checkArgs(coin,mkt)
	cryptoUrl = 'https://marketwatch.com/investing/cryptocurrency/'+coin+mkt+'/historical'
	checkPair(cryptoUrl)
	print('Fetching quote for '+coin+'/'+mkt+':')
	getQuote(cryptoUrl)