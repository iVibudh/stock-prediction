import pandas as pd
import yfinance as yf
import datetime
import re

# msft = yf.Ticker("MSFT")
# # get stock info
# for x,y in msft.info.items():
#     print(x,y)
# print(msft.info["sector"])

def getCompanyInfo2(symbols):
    infoDL = []
    for symbol in symbols:
        print("Getting Data for ", symbol)
        try:
            Tick = yf.Ticker(symbol)
            infoD = Tick.info
            infoDL.append(infoD)
        except:
            print("Cound NOT get")

    return infoDL


def getCompanyInfoShort(symbols):
    #info
    fail = []
    tickerName = []
    shortName = []
    sector = []
    #Stock Matters
    ask = [] #Market closing value
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
            shortName.append(infoD["shortName"])
            sector.append(infoD["sector"])
            ask.append(infoD["ask"])  # Market closing value
            previousClose.append(infoD["previousClose"])
            open.append(infoD["open"])
            currency.append(infoD["currency"])
            trailingPE.append(infoD["trailingPE"])
            forwardPE.append(infoD["forwardPE"])

        except:
            print("scrape failed")
            fail.append(symbol)

    df_data = pd.DataFrame({'tickerName' : tickerName,
                            'shortName' : shortName,
                            'sector' : sector,
                            'ask' : ask,
                            'previousClose' : previousClose,
                            'open' : open,
                            'currency' : currency,
                            'trailingPE' : trailingPE,
                            'forwardPE' : forwardPE})
    return df_data





def getCompanyInfo(symbols):
    #info
    shortName = []
    sector = []
    industry = []
    dividentRate = []

    #Stock Matters
    ask = [] #Market closing value
    previousClose = []
    open = []
    currency = []
    time = [] #pd.to_datetime('today')
    regularMarketOpen = []
    beta = []
    revenueQuaterlyGrowth = []
    beta = []
    trailingPE = []
    forwardPE = []

    regularMarketDayLow = []
    regularMarketDayHigh = []
    fiftyDayAverage = []
    twoHundredDayAverage = []
    dayHigh = []
    dayLow = []
    payoutRatio = []
    trailingAnnualDivident = []
    fiftyTwoWeekHigh = []
    profitMargins = []
    netIncomeToCommon = []
    trailingEPS = []
    nextFiscalYearEnd = []
    mostRecentQuarter = []
    shortRatio = []

    for symbol in symbols:
        print("Getting Data for ", symbol)
        Tick = yf.Ticker("symbol")
        infoD = Tick.info

        # info
        shortName.append(infoD["shortName"])
        sector.append(infoD["sector"])
        industry.append(infoD["industry"])
        dividentRate.append(infoD["dividentRate"])

        # Stock Matters
        ask.append(infoD["ask"])  # Market closing value
        previousClose.append(infoD["previousClose"])
        open.append(infoD["open"])
        currency.append(infoD["currency"])
        time.append(infoD["time"])  # pd.to_datetime('today')
        regularMarketOpen.append(infoD["regularMarketOpen"])
        beta.append(infoD["beta"])
        revenueQuaterlyGrowth.append(infoD["revenueQuaterlyGrowth"])
        beta.append(infoD["beta"])
        trailingPE.append(infoD["trailingPE"])
        forwardPE.append(infoD["forwardPE"])

        regularMarketDayLow.append(infoD["regularMarketDayLow"])
        regularMarketDayHigh.append(infoD["regularMarketDayHigh"])
        fiftyDayAverage.append(infoD["fiftyDayAverage"])
        twoHundredDayAverage.append(infoD["twoHundredDayAverage"])
        dayHigh.append(infoD["dayHigh"])
        dayLow.append(infoD["dayLow"])
        payoutRatio.append(infoD["payoutRatio"])
        trailingAnnualDivident.append(infoD["trailingAnnualDivident"])
        fiftyTwoWeekHigh.append(infoD["fiftyTwoWeekHigh"])
        profitMargins.append(infoD["profitMargins"])
        netIncomeToCommon.append(infoD["netIncomeToCommon"])
        trailingEPS.append(infoD["trailingEPS"])
        nextFiscalYearEnd.append(infoD["nextFiscalYearEnd"])
        mostRecentQuarter.append(infoD["mostRecentQuarter"])
        shortRatio.append(infoD["shortRatio"])






