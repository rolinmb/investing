from bs4 import BeautifulSoup
import requests
import sys

def parseRate(html):
	soup = BeautifulSoup(html,'html.parser')
	valStr = soup.find_all('p',class_='data bgLast')
	content = [c.text for c in valStr]
	return float(''.join(content))
	
def getQuote(url):
	resp = requests.get(url)
	html = resp.text
	rate = parseRate(html)
	print('\t Current Rate: ',rate)
	
def checkArgs(f,d):
	if not f.isalpha():
		sys.exit('Non-letters entered for foreign currency symbol.')
	if not d.isalpha():
		sys.exit('Non-letters entered for domestic currency symbol.')

def checkPair(url):
	resp = requests.get(url)
	html = resp.text
	try:
		r = parseRate(html)
	except ValueError:
		sys.exit('The currency pair: '+f+'/'+d+' does not exist.')
		
if __name__ == '__main__':
	try:
		f = sys.argv[1].upper()
	except IndexError:
		sys.exit('No foreign currency symbol entered.')
	try:
		d = sys.argv[2].upper() 
	except IndexError:
		sys.exit('No domestic currency symbol entered.')
	
	checkArgs(f,d)
	fxUrl = 'https://marketwatch.com/investing/currency/'+f.lower()+d.lower()+'/historical'
	checkPair(fxUrl)
	print('Fetching quote for: '+f+'/'+d)
	getQuote(fxUrl)