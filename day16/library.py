import ccxt

while True:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USD')
    current_price = ticker['last']
    print(f"현재 가격: {current_price}")
    if prev_price - current_price > 0:
        print("돔황챠")
    else:
        print("한강뷰 가즈아")
    prev_price = current_price
    print(f"BTC/USD의 현재 가격: {current_price}")

    # if current_price - 1:
    #     print("돔황챠")
    # elif current_price + 1:
    #     print("가즈ㅏ아")

# 1달러 오르면 한강뷰 가즈아
# 1달러 떨어지면 돔황챠
