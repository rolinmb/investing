import alpaca_trade_api
import sys

def getAlpacaQuote(api,t):
	print('Alpaca quote for '+t+':\n')
	try:
		q = api.get_last_quote(t)
	except Exception:
		sys.exit('\t*Error: ticker/symbol '+t+' does not exist')
	print(str(q))
			
def getPositions(api):
	print('\n\t(Alpaca Order List:)\n')
	for o in api.list_orders():
		print('\t'+str(o)+'\n')	
	print('Alpaca Positions List:\n')
	for p in api.list_positions():
		print('\t'+str(p)+'\n')
	
def accountInfo(api):
	print('\n(Getting Alpaca account information)')
	account = api.get_account()
	print('\t*Alpaca Buying-Power: $'+account.buying_power)
	print('\t*Alpaca Cash Balance: $'+account.cash)
	getPositions(api)
			
def cancelOrders(api):
	print('\n(Closing all orders queued on Alpaca)')
	api.cancel_all_orders()
	print('\t*All orders on Alpaca have been closed')
	
def closePositions(api):
	print('\n(Exiting all positions on Alpaca)')
	api.close_all_positions()
	print('/t*All positions on Alpaca have been exited')
	
def marketOrder(api,t,qty):
	print('(Submitting '+t+'Market Order for '+str(qty)+' shares)')
	api.submit_order(
		symbol=t,
		qty=str(qty),
		side='buy',
		type='market',
		time_in_force='gtc'
	)
	# time_in_force usually set to 'day' or 'gtc' good till cancelled
	print('\t*Order for '+str(qty)+' '+t+' shares sucessfully submitted')