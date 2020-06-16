# Investing Projects
This repo contains miscellanious financial market projects implemented Python.
 
# stock_quote.py
<ul>
<li>Fetches single stock/ETF quote via marketwatch.com</li>
<li>1st and only argument is the ticker/symbol to fetch</li>
<li>Example Usage: 'quote.py spy'</li>
<li>NOTE: Will only update correctly during market open hours/days, otherwise will return same price</li>
<li>Dependencies: BeautifulSoup</li></ul>

# stock_quote_stream.py
<ul>
<li>Fetches multitude of stock/ETF quotes via marketwatch.com</li>
<li>1st argument is the ticker, 2nd argument is the number of quotes</li>
<li>Example Usage: 'quote_stream.py spy 100'</li>
<li>NOTE: Will only update correctly during market open hours/days, otherwise will return same price</li>
<li>Dependencies: BeautifulSoup</li></ul>

# stock_chart.py
<ul>
<li>Utilizes the alpha_vantage.TimeSeries module to generate a chart for specified ticker/symbol</li>
<li>Constructs daily close price chart with various moving averages for the dedsired stock/ETF</li>
<li>Contains functions for Simple/Exponential/Double-Exponential Moving Averages</li>
<li>1st and only argument is the ticker/symbol</li>
<li>Example Usage: 'stock_chart.py spy'</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# crypto_chart.py
<ul>
<li>Utilizes the alpha_vantage.CryptoCurrencies module to genereate a chart for specified coin and currency</li>
<li>Constructs daily close price chart with various moving averages for desired cryptocurrency</li>
<li>Contains functions for Simple/Exponential/Double-Exponential Moving Averages</li>
<li>1st argument is the symbol of desired cryptocurrency, 2nd argument is the domestic currency desired</li>
<li>Example Usage: 'crypto_chart.py btc usd'</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# forex_quote.py
<ul>
<li>Fetches single foreign exchange quote via alpha_vantage.ForeignExchange module</li>
<li>1st and only argument is the ticker/symbol to fetch</li>
<li>Example Usage: 'forex_quote.py eur usd'</li>
<li>NOTE: Will only update correctly during market open hours/days, otherwise will return same price</li>
<li>Dependencies: alpha_vantage</li></ul>

# forex_chart.py
<ul>
<li>Utilizes the alpha_vantage.ForeignExchange module to generate a chart for specified forex pair</li>
<li>Constructs daily close price chart with various moving averages for the desired currency crossing</li>
<li>Contains functions for Simple/Exponential/Double-Exponential Moving Averages</li>
<li>1st argument is the foreign currency symbol, 2nd argument is the domestic currency symbol</li>
<li>Example Usage: 'forex_chart.py eur usd'</li>
<li>NOTE: Will only update correctly during market open hours/days, otherwise will return same rate</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>
<br />
Developed by Rolin Blake
