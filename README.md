# Investing Projects
<i>This repo contains several ongoing financial market projects implemented Python(Version 3.6.2).</i><br />
Last Updated: <i>7/12/2020</i><br />
<b>NOTES</b>:<ul>
<li>NOT FINANCIAL ADVICE; IF YOU ARE TO USE THESE PROGRAMS TO MAKE FINANCIAL DECISIONS IT WILL BE DONE AT YOUR OWN RISK.</li>
<li>You will only witness stock and forex quotes update during market open hours/days,<br />
this does not apply to cryptocurrency quotes.</li>
<li>You will need your own Alpaca & AlphaVantage API keys. I keep mine in a local 'confing.py/js' files</li><ul>

# /backtesting
<ul><li>This folder contains projects from analyzing various strategies I plan to use on a paper account with Alpaca</li>
<li><b>main.py</b> executes the backtest, 3 arguments needed unless you delete [ticker] in the tData[] list which then allows the program
to iterates through the uncommented tickers in tData. 
	<ul>
		<li>1st argument is the ticker (unless commented)</li>
		<li>2nd argument is the number of shares (shares > 0) NOTE: this is the 1st argument if ticker is disabled</li>
		<li>3rd argument is the initial account balance for each backtest (balance > 0) NOTE: this is the 2nd argument if ticker is disabled</li>
	</ul>
</li>
<li>Example Usage w/ 3 arguments): main.py spy 1 1000 /li>
<li>Example Usage w/ 2 arguments): main.py 1 1000</li>
<li>stragegies.py are the 4 strategies I've implemented a backtest for</li>
<li>analysis.py in this folder is different than the one in the outer/root repo; contains staistics helpers for strategies.py</li>
<li>alpaca_util.py contains several functions that work with alpaca_trade_api.REST accounts</li>
<li>I have a file data.txt where I output the results to as a whitespace-delimited file</li>
<li>Dependencies: Pandas, alpaca_trade_api, alpha_vantage, matplotlib</li></ul>

# alpaca_test.js
<ul>
<li>Simple script which uses Alpaca's JavaScript API wrapper for account information and the ability to trade(paper or live)</li>
<li>Needs a config.js file which contains your API keys and correctly imports them as this is written with Node.js in mind</li>
</ul>

# config.py
<ul><li>Demo configuration file for Alpaca & AlphaVantage API keys</li></ul>

# config.js
<ul><li>Demo configuration file for Alpaca & AlphaVantage api keys</li>
<li>Uses Object.defineProperty to stay within boundaries of Node.js for exporting constants</li></ul>


# analysis.py
<ul><li>A python module of functions used for technical analysis.</li>
<li>Contains: 
	<ul>
		<li>Typial & Average price</li>
		<li>Simple/Exponential/Double-Exponential Moving Averages</li>
		<li>ROC Indicator</li>
		<li>Standard Deviation over time</li>
		<li>True Strength Index</li>
		<li>Commodity Channel Index</li></ul>
</li>
<li>Dependencies: Pandas</li></ul>
<hr>

# stock_quote.py
<ul><li>Fetches single stock/ETF quote via marketwatch.com</li>
<li>1st and only argument is the ticker/symbol of desired stock</li>
<li>Example Usage: "stock_quote.py spy"</li>
<li>Dependencies: BeautifulSoup</li></ul>

# stock_quote_stream.py
<ul><li>Fetches multitude of stock/ETF quotes via marketwatch.com</li>
<li>1st argument is the ticker/symbol of desired stock</li>
<li>2nd argument is the number of quotes</li>
<li>Example Usage: "stock_quote_stream.py spy 100"</li>
<li>Dependencies: BeautifulSoup</li></ul>

# stock_chart.py
<ul><li>Utilizes the alpha_vantage.TimeSeries module to generate a chart for specified ticker/symbol</li>
<li>Constructs daily close price chart with various moving averages for the dedsired stock/ETF</li>
<li>1st and only argument is the ticker/symbol</li>
<li>Example Usage: "stock_chart.py spy"</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>
<hr>

# crypto_quote.py
<ul><li>Fetches single cryptocurrency quote via marketwatch.com</li>
<li>1st argument is the foreign currency symbol</li>
<li>2nd argument is the relative currency for the quote</li>
<li>Example Usage: "crypto_quote.py btc usd"</li>
<li>Dependencies: BeautifulSoup</li></ul>

# crypto_quote_stream.py
<ul><li>Fetches multitude of cryptocurrency quotes via marketwatch.com</li>
<li>1st argument is the symbol of desired cryptocurrency</li>
<li>2nd argument is the relative currency for the quotes</li>
<li>3rd argument is the number of quotes</li>
<li>Example Usage: "crypto_quote_stream.py btc usd 100"</li>
<li>Dependencies: BeautifulSoup</li></ul>

# crypto_chart.py
<ul><li>Utilizes the alpha_vantage.CryptoCurrencies module to genereate a chart for specified coin and currency</li>
<li>Constructs daily close price chart with various moving averages for desired cryptocurrency</li>
<li>1st argument is the symbol of desired cryptocurrency</li>
<li>2nd argument is the relative currency</li>
<li>Example Usage: "crypto_chart.py btc usd"</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>
<hr>

# forex_quote.py
<ul><li>Fetches single foreign exchange cross quote via marketwatch.com</li>
<li>1st argument is the foreign currency symbol</li>
<li>2nd argument is the domestic currency symbol</li>
<li>Example Usage: "forex_quote.py eur usd"</li>
<li>Dependencies: BeautifulSoup</li></ul>

# forex_quote_stream.py
<ul><li>Fetches multitude of foreign exchange quotes via marketwatch.com</li>
<li>1st argument is the foreign currency symbol</li>
<li>2nd argument is the domestic currency symbol</li>
<li>3rd argument is the number of quotes</li>
<li>Example Usage: "forex_quote_stream.py eur usd 100"</li>
<li>Dependencies: BeautifulSoup</li></ul>

# forex_chart.py
<ul><li>Utilizes the alpha_vantage.ForeignExchange module to generate a chart for specified forex pair</li>
<li>Constructs daily close price chart with various moving averages for the desired currency crossing</li>
<li>1st argument is the foreign currency symbol</li>
<li>2nd argument is the domestic currency symbol</li>
<li>Example Usage: "forex_chart.py eur usd"</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>
<hr>

# gold_silver.py
<ul><li>Gold/Silver Ratio (XAU/XAG) using GLDM and SLV ETFs (Short lookback period)</li>
<li>When the XAU/XAG increases, Gold strengthens relative to Silver</li>
<li>When the XAU/XAG decreases, Silver strengthens relative to Gold</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# btc_eth.py
<ul><li>Bitcoin/Ethereum Ratio (BTC/ETH) using BTC/USD and ETH/USD</li>
<li>When BTC/USD increases, Bitcoin strengthens relative to Ethereum</li>
<li>When BTC/USD decreases, Ethereum strengthens relative to Bitcoin and other Altcoins tend to strengthen too.</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# btc_xtz.py
<ul><li>Bitcoin/Tezos Ratio (BTC/XTZ) using BTC/USD and XTZ/USD</li>
<li>Dependencies: Pandas, Matplotlib, alpha_vantage</li></ul>

# blackScholes.py
<ul><li>Rough implementation of the Black-Scholes options pricing model</li>
<li>Also contains implementations for 'greeks' or derivatives of Black-Scholes partial differential equation</li>
<li>Dependencies: Scipy, Numpy, Matplotlib</li></ul>

# put_call_ratio.py
<ul><li>Extracts the CBOE Put/Call Ratio from https://ycharts.com/indicators/cboe_equity_put_call_ratio</li>
<li>Dependencies: BeautifulSoup</li></ul>
