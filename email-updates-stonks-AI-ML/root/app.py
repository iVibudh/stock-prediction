import yagmail
import pandas as pd
from pandas_datareader import data
import datetime

#path1 = "C:\\Users\\singvibu\\Desktop\\AI.ML.Stocks.Pwd.txt"
path1 = "C:\\Users\\T1Vibudh\\Desktop\\AI.ML.Stocks.Pwd.txt"
f = open(path1, "r")
passw = f.read()
f.close()

now = datetime.datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

t = 'SQ'
marketCap = data.get_quote_yahoo(t)['marketCap']


receiver = "ivibudh@gmail.com"
sender = "ai.ml.stocks@gmail.com"

body = """Hello there from AI-ML-Stocks
Update Date-Time: """ + date_time + """ 
Market Cap of """ + t + " is $" + str(marketCap).split()[1] + "."

yag = yagmail.SMTP("ai.ml.stocks@gmail.com", passw)
yag.send(
    to = receiver,
    subject ="Yagmail test emsil",
    contents = body,)