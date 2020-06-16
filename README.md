# Investing Projects
This repo contains miscellanious financial market projects implemented Python.
 
# quote.py
<ul>
<li>Fetches single stock/ETF quote via marketwatch.com</li>
<li>First and only argument is the ticker/symbol to fetch</li>
<li>Dependencies: BeautifulSoup</li></ul>

# quote_stream.py
<ul>
<li>Fetches multitude of stock/ETF quotes via marketwatch.com</li>
<li>1st argument is the ticker, 2nd argument is the number of quotes</li>
<li>Dependencies: BeautifulSoup</li></ul>

# stock_chart.py
<ul>
<li>Utilizes the AlphaVantage.TimeSeries module to generate a chart for specified ticker/symbol</li>
<li>Constructs daily close price chart with various moving averages for the dedsired stock/ETF</li>
<li>Contains functions for Simple/Exponential/Double-Exponential Moving Averages</li>
<li>1st and only argument is the ticker/symbol</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# crypto_chart.py
<ul>
<li>Utilizes the AlphaVantage.CryptoCurrencies module to genereate a chart for specified coin and currency</li>
<li>Constructs daily close price chart with various moving averages for desired cryptocurrency</li>
<li>Contains functions for Simple/Exponential/Double-Exponential Moving Averages</li>
<li>1st argument is the symbol of desired cryptocurrency, 2nd argument is the domestic currency desired</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# forex_chart.py
<ul>
<li>Utilizes the AlphaVantage.ForeignExchange module to generate a chart for specified forex pair</li>
<li>Constructs daily close price chart with various moving averages for the desired currency crossing</li>
<li>1st argument is the foreign currency symbol, 2nd argument is the domestic currency symbol</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>
<br />
Developed by Rolin Blake
