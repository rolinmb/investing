from bs4 import BeautifulSoup
import requests
import time
import sys
import re

def stripCommas(s):
	return re.sub(',(?!\s+\d$)','',s)
	
def parseRate(html):
	soup = BeautifulSoup(html,'html.parser')
	valStr = soup.find_all('p',class_='data bgLast')
	content = [c.text for c in valStr]
	return float(stripCommas(''.join(content)))
	
def streamQuotes(url,num):
	sesh = requests.session()
	for n in range(0,num):
		resp = sesh.get(url)
		html = resp.text
		rate = parseRate(html)
		print('\t('+str(n+1)+') Current Rate: ',rate)
		time.sleep(0.5)
	sesh.close()
	
def checkArgs(c,m,n):
	if not c.isalpha():
		sys.exit('Non-letters entered for coin symbol.')
	if not m.isalpha():
		sys.exit('Non-letters entered for currency type.')
	if n <= 0:
		sys.exit('Zero or negative entered for quote count.')
		
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
		sys.exit('No cryptocurrency currency symbol entered.')
	try:
		mkt = sys.argv[2].upper() 
	except IndexError:
		sys.exit('No domestic currency symbol entered.')
	try:		
		count = int(sys.argv[3])
	except IndexError:
		sys.exit('Number of desired quotes not entered.')
	except ValueError:
		sys.exit('Decimal entered for number of quotes.')
		
	checkArgs(coin,mkt,count)
	cryptoUrl = 'https://marketwatch.com/investing/cryptocurrency/'+coin+mkt+'/historical'
	checkPair(cryptoUrl)
	print('Fetching '+str(count)+' quotes for '+coin+'/'+mkt+':')
	start = time.time()
	streamQuotes(cryptoUrl,count)
	end = time.time()
	print('Query Time: '+str(round(float(end-start),3))+'s')
	