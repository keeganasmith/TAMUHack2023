import yfinance as yf

import pandas as pd
import numpy as np




def get_Avg_Yearly_Growth(tickerSymbol, time_period = "10y"):

    msft = yf.Ticker(tickerSymbol)

    # get historical market data
    hist = msft.history(period=time_period,interval= "3mo")

    n = 0
    total_growth = 0
    thing = hist.to_records()
    
    for i in range(len(thing)-4):
        start_price = thing[i][3]
        end_price = thing[i+4][3]
        growth = (end_price-start_price)/start_price
        total_growth += growth
        n += 1

    average_growth = total_growth/n
    return average_growth


def get_Total_Avg_Yearly_Growth(ticker_list, money_list):
    #calculate percentage for each stock based on total

    percentage_list = list(range(len(ticker_list)))

    total_money = 0
    for i in money_list:
        total_money += i

    j = 0
    for i in money_list:
        percentage_list[j] = i/total_money
        j += 1
    
    total_growth = 0

    print(len(percentage_list))
    print(len(ticker_list))

    for i in range(len(ticker_list)):
        total_growth += get_Avg_Yearly_Growth(ticker_list[i])*percentage_list[i]

    return total_growth

stock_list = ["AAPL","MSFT"]
money_amount = [200, 300]
print(get_Total_Avg_Yearly_Growth(stock_list,money_amount))