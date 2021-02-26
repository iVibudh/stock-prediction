# import pandas as pd
# import datetime
# Key_Stocks = ['DAL','AAL','VOO', 'MRNA', 'AAPL', 'AMZN',
#               'NFLX', 'TSLA', 'XOM', 'NKE', 'DIS', 'COST']
# start = pd.to_datetime('2020-02-04')
# end = pd.to_datetime('today')
# now = datetime.datetime.today()
# print(start)
# print(end)
# print(now)
# # from yahoo_finance import Share
# # yahoo = Share('YHOO')
# # print(yahoo.get_open())
#
# from pandas_datareader import data, wb
# # tesla_df = data.DataReader('AAPL', 'yahoo', start , end)
# # print(tesla_df[-1:])
#
# import yfinance as yf
# # data = yf.download('AAPL',start, end)
# # print(data[-1:])
#
# tesla_df = data.DataReader('AAPL', 'yahoo', start , now)
# print(tesla_df)
#
# data = yf.download('AAPL',start, end)
# print(data[-1:])
#
#
b = []
a = {'key' : "vib", "value" : ""}
print("hey", a.get("value"))
if a.get("value2"):
    print("Not Null")
    b.append(a.get("value2"))
else:
    print("Null verified")
if a.get("value"):
    print("Not Null")
    b.append(a.get("value"))
else:
    print("Null verified")
print(b)