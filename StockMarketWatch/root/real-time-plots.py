# import yfinance
# stock = yfinance.Ticker("AAPL")
# print("stock", stock)
# df = stock.history(period='2y')
# print("stock type", type(stock))
# print("stock name", stock.info['longName'])
# price_list = stock.history(period='5y')['Close'].tolist()
# print("price 5 years", price_list)
# print("len 5 years price", len(price_list))
# price = f'${price_list[-1]:.2f}'
# print("price 5 Years iDK", price)
# price_list = stock.history(period='2y')['Close'].tolist()
# price = f'${price_list[-1]:.5f}'

import yfinance as yf

msft = yf.Ticker("MSFT", proxy="PROXY_SERVER")

# get stock info
for x,y in msft.info.items():
    print(x,y)
print(msft.info["sector"])
