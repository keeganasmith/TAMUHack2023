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


def get_Total_Avg_Yearly_Growth(list_items):
    #calculate percentage for each stock based on total

    percentage_list = list(range(len(list_items)))

    total_money = 0
    for i in range(len(list_items)):
        total_money += list_items[i][1]

    for i in range(len(list_items)):
        percentage_list[i] = list_items[i][1]/total_money
    
    total_growth = 0

    for i in range(len(list_items)):
        total_growth += get_Avg_Yearly_Growth(list_items[i][0])*percentage_list[i]

    return total_growth

stock_list = [["AAPL",300],["MSFT",200]]
print(get_Total_Avg_Yearly_Growth(stock_list))