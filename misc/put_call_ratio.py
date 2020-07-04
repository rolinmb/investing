from bs4 import BeautifulSoup
import requests
import sys

if __name__ == '__main__':
	url = 'https://ycharts.com/indicators/cboe_equity_put_call_ratio'
	resp = requests.get(url)
	html = resp.text
	soup = BeautifulSoup(html,'html.parser')
	div = soup.find(id='pgNameVal')
	content = [c for c in div.contents[0]]
	string = content[0]+content[1]+content[2]+content[3]
	ratio = float(string)
	print(ratio)
	