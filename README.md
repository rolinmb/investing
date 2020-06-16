# <b>Investing Projects</b>
<i>This repo contains miscellanious financial market projects implemented Python.</i><br />
Last Updated: <i>6/16/2020</i><br />
<b>NOTE</b>: You will only witness stock and forex quotes update during market open hours/days.<br />
This does not apply to cryptocurrency quotes.<br />

# stock_quote.py
<ul>
<li>Fetches single stock/ETF quote via marketwatch.com</li>
<li>1st and only argument is the ticker/symbol to fetch</li>
<li>Example Usage: "quote.py spy"</li>
<li>Dependencies: BeautifulSoup</li></ul>

# stock_quote_stream.py
<ul>
<li>Fetches multitude of stock/ETF quotes via marketwatch.com</li>
<li>1st argument is the ticker</li>
<li>2nd argument is the number of quotes</li>
<li>Example Usage: "quote_stream.py spy 100"</li>
<li>Dependencies: BeautifulSoup</li></ul>

# stock_chart.py
<ul>
<li>Utilizes the alpha_vantage.TimeSeries module to generate a chart for specified ticker/symbol</li>
<li>Constructs daily close price chart with various moving averages for the dedsired stock/ETF</li>
<li>Contains functions for Simple/Exponential/Double-Exponential Moving Averages</li>
<li>1st and only argument is the ticker/symbol</li>
<li>Example Usage: "stock_chart.py spy"</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# crypto_chart.py
<ul>
<li>Utilizes the alpha_vantage.CryptoCurrencies module to genereate a chart for specified coin and currency</li>
<li>Constructs daily close price chart with various moving averages for desired cryptocurrency</li>
<li>Contains functions for Simple/Exponential/Double-Exponential Moving Averages</li>
<li>1st argument is the symbol of desired cryptocurrency</li>
<li>2nd argument is the domestic currency desired</li>
<li>Example Usage: "crypto_chart.py btc usd"</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# forex_quote.py
<ul>
<li>Fetches single foreign exchange quote via alpha_vantage.ForeignExchange module</li>
<li>1st argument is the foreign currency symbol</li>
<li>2nd argument is the domestic currency symbol</li>
<li>Example Usage: "forex_quote.py eur usd"</li>
<li>Dependencies: alpha_vantage</li></ul>

# forex_quote_stream.py
<ul>
<li>Fetches multitude of foreign exchange quotes via alpha_vantage.ForeignExchange module</li>
<li>1st argument is the foreign currency symbol</li>
<li>2nd argument is the domestic currency symbol</li>
<li>3rd argument is the number of quotes</li>
<li>Example Usage: "forex_quote_stream.py eur usd 100"</li>
<li>Dependencies: alpha_vantage</li></ul>
<li><b>NOTE</b>: The standard AlphaVantage API access is 5 calls/min and 500/day;<br/>
				so this script is essentially un-usable with free AlphaVantage.</li></ul>

# forex_chart.py
<ul>
<li>Utilizes the alpha_vantage.ForeignExchange module to generate a chart for specified forex pair</li>
<li>Constructs daily close price chart with various moving averages for the desired currency crossing</li>
<li>Contains functions for Simple/Exponential/Double-Exponential Moving Averages</li>
<li>1st argument is the foreign currency symbol</li>
<li>2nd argument is the domestic currency symbol</li>
<li>Example Usage: "forex_chart.py eur usd"</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li>
<br />
Developed by Rolin Blake  

