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

if __name__ == '__main__':
	try:
		ticker = sys.argv[1].lower()
		count = int(sys.argv[2])
	except IndexError:
		sys.exit('Argument(s) missing.')