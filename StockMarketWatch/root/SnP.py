import pandas as pd
from StockFunctions import *
from datetime import datetime

#Get the list of SnP Companies
df = pd.read_excel ('SnPCompanies.xlsx', sheet_name='SnP')
dfSnP = pd.DataFrame()
dfSnP[['Symbol', 'Name', 'SnP500', 'SnP100']] = df[['Symbol', 'Name', 'SnP500', 'SnP100.SnP100']]
#dfSnP = dfSnP[5:15]

# a = getCompanyInfo2(list(dfSnP['Symbol']))
# print(a)

# a = getCompanyInfoShort(list(dfSnP['Symbol']))
# print(a)
#

symbols = list(dfSnP['Symbol'])
fail = []
tickerName = []
shortName = []
sector = []
# Stock Matters
ask = []  # Market closing value
previousClose = []
open = []
currency = []
trailingPE = []
forwardPE = []

for symbol in symbols:
    print("Getting Data for ", symbol)
    try:
        Tick = yf.Ticker(symbol)
        infoD = Tick.info
        if infoD.get("shortName"):
            shortName.append(infoD["shortName"])
        else:
            shortName.append('0')
        if infoD.get("sector"):
            sector.append(infoD["sector"])
        else:
            sector.append(0)
        if infoD.get("ask"):
            ask.append(infoD["ask"])
        else:
            ask.append(0)# Market closing value
        if infoD.get("previousClose"):
            previousClose.append(infoD["previousClose"])
        else:
            previousClose.append(0)
        if infoD.get("open"):
            open.append(infoD["open"])
        else:
            open.append(0)
        if infoD.get("currency"):
            currency.append(infoD["currency"])
        else:
            currency.append(0)
        if infoD.get("trailingPE"):
            trailingPE.append(infoD["trailingPE"])
        else:
            trailingPE.append(0)
        if infoD.get("forwardPE"):
            forwardPE.append(infoD["forwardPE"])
        else:
            forwardPE.append(0)
        tickerName.append(symbol)

    except:
        print("scrape failed")
        fail.append(symbol)

print(len(tickerName))
print(len(shortName))
print(len(sector))
print(len(ask))
print(len(trailingPE))
print(len(forwardPE))

df_data = pd.DataFrame({'tickerName': tickerName,
                        'shortName': shortName,
                        'sector': sector,
                        'ask': ask,
                        'previousClose': previousClose,
                        'open': open,
                        'currency': currency,
                        'trailingPE': trailingPE,
                        'forwardPE': forwardPE})


now = datetime.now()  # current date and time
timestamp = datetime.timestamp(now)
new_file = str(now.strftime("%Y")) + "." + str(now.strftime("%m")) + "." + str(now.strftime("%d")) + "." + str(timestamp)
#a.to_csv(new_file+".csv")
df_data.to_csv(new_file+".csv")