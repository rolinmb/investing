from bs4 import BeautifulSoup
import requests
import time
import sys

def parseRate(html):
	soup = BeautifulSoup(html,'html.parser')
	valStr = soup.find_all('p',class_='data bgLast')
	content = [c.text for c in valStr]
	return float(''.join(content))

def streamQuotes(url,num):
	sesh = requests.session()
	for n in range(0,num):
		resp = sesh.get(url)
		html = resp.text
		rate = parseRate(html)
		print('\t('+str(n+1)+') Current Rate: ',rate)
	sesh.close()

def checkArgs(f,d,n):
	if not f.isalpha():
		sys.exit('Non-letters entered for foreign currency symbol.')
	if not d.isalpha():
		sys.exit('Non-letters entered for domestic currency symbol.')
	if n <= 0:
		sys.exit('Zero or negative number of quotes entered.')

def checkPair(url):
	resp = requests.get(url)
	html = resp.text
	try:
		r = parseRate(html)
	except ValueError:
		sys.exit('The currency pair: '+f+'/'+d+' does not exist.')
		
if __name__ == '__main__':
	# Anyone can use this key, AlphaVantage gives them out for free w/ no limits.
	key = 'K2CQV5DF42ONO1EY'
	try:
		f = sys.argv[1].upper()
	except IndexError:
		sys.exit('No foreign currency symbol entered.')
	try:
		d = sys.argv[2].upper() 
	except IndexError:
		sys.exit('No domestic currency symbol entered.')
	try:		
		count = int(sys.argv[3])
	except IndexError:
		sys.exit('Number of desired quotes not entered.')
	except ValueError:
		sys.exit('Decimal entered for number of quotes.')
	
	checkArgs(f,d,count)
	fxUrl = 'https://marketwatch.com/investing/currency/'+f.lower()+d.lower()+'/historical'
	checkPair(fxUrl)
	print('Fetching '+str(count)+' quotes for '+f+'/'+d+':')
	start = time.time()
	streamQuotes(fxUrl,count)
	end = time.time()
	print('Query Time: '+str(round(float(end-start),3))+'s')	