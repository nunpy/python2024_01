# import cctx
#
#
# exchange = cctx.binance()
# ticker = exchange.fetch_ticker('BTC/USD')
# current_price = ticker['last']
# print(f"BTC/USD의 현재 가격: {current_price}")

import yfinance

microsoft = yfinance.Ticker("MSFT")
current_price = microsoft.info['currentPrice']
print(f"마이크로소프트 주식의 현재 가격: {current_price}")
