import yfinance as yf

import pandas as pd
import numpy as np




def get_Avg_Yearly_Growth(tickerSymbol, time_period):

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



print(get_Avg_Yearly_Growth("^GSPC","10y"))