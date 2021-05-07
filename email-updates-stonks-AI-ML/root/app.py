import yagmail
import pandas as pd
from pandas_datareader import data
import datetime

#path1 = "C:\\Users\\singvibu\\Desktop\\AI.ML.Stocks.Pwd.txt"
path1 = "C:\\Users\\T1Vibudh\\Desktop\\AI.ML.Stocks.Pwd.txt"
f = open(path1, "r")
passw = f.read()
f.close()