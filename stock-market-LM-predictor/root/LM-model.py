## https://www.youtube.com/watch?v=9Bas8A9npp8

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from yahoofinancials import YahooFinancials
import mpl_finance
import matplotlib.pyplot as plt

stock = "AAPL"

yahoo_financials = YahooFinancials(str(stock))
stats = (yahoo_financials.get_historical_price_data("2020-01-01", "2020-02-01", "daily"))

print(stats)
# i = 0
# for date in stats[str(stock)]["prices"]:
#     if i == 0:
#         i +=1
#         continue
#     highs.append(date['high'])
#     lows.append(date['low'])
#     opend