import yfinance as yf
import pandas
import numpy as np
PERIOD_1 = "5y"
def standard_deviation(list, average):
    sum = 0.0
    for i in range(0, len(list)):
        sum += (list[i] - average)**2
    sum /= len(list);
    return sum ** .5
def average(list):
    sum = 0.0;
    for val in list:
        sum += val
    return sum / len(list)
def day_to_day_change_list(list):
    result = [0] * len(list)
    for i in range(1, len(list)):
        result[i] = (list[i] - list[i-1])/list[i-1]
    return result;
def day_to_day_change(stock):
    ticker = yf.Ticker(stock)
    history = ticker.history(period = PERIOD_1)
    history_arr = history.to_records()
    result = [0]*len(history_arr)
    prev = history_arr[0][4];
    first = True
    i = 0
    for val in history_arr:
        if(first):
            first = False
            continue
        result[i] = (val[4] - prev)/prev
        i += 1
        prev = val[4]
    return result

def get_total(portfolio):
    result = [0]*len(yf.Ticker(portfolio[0][0]).history(period = PERIOD_1).to_records() )
    total_amount = 0.0;
    for val in portfolio:
        total_amount += val[1]
    for stock in portfolio:
        ticker = yf.Ticker(stock[0])
        history = ticker.history(period = PERIOD_1)
        history_arr = history.to_records()
        i = 0
        percent = float(stock[1])/total_amount;
        for val in history_arr:
            result[i] += percent * val[4]
            i += 1;
    return result
#difference, a - b
def excess_returns(a, b):
    returns = [0] * len(a)
    for i in range(0, len(a)):
        returns[i] = a[i] - b[i];
    return returns
#Takes an array of pairs, [stock name, amount]
#returns the sharpe value relative to the S&P 500
def sharpe(portfolio, period = '5y'):
    PERIOD_1 = period
    sp_day_to_day = day_to_day_change('^GSPC')
    # print(average(result))
    portfolio_totals = get_total(portfolio)
    portfolio_day_to_day = day_to_day_change_list(portfolio_totals)
    # print(portfolio_day_to_day)
    # print(average(portfolio_day_to_day))
    
    excess_return_list = excess_returns(portfolio_day_to_day, sp_day_to_day)
    average_excess_returns = average(excess_return_list)
    excess_returns_sd = standard_deviation(excess_return_list, average_excess_returns)
    #print(f"average excess returns: {average_excess_returns}")
    #print(f"excess return sd: {excess_returns_sd}")
    sharpe_ratio = average_excess_returns/excess_returns_sd * (len(excess_return_list)) ** .5;
    return sharpe_ratio
#sharpe(['aapl'])
portfolio1 = [
    ['aapl', 500],
    ['^GSPC', 700],
    ['msft', 200],
    ['tsla', 100]
    ]
sharpe(portfolio1)
#ticker = yf.Ticker('aapl')
