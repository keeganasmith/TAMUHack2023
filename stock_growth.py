import yfinance as yf
import risk_evaluation as ur 
import interest_rates as ir
ticker = yf.Ticker('^GSPC')
history = ticker.history(period = '6mo', interval = '1mo')
arr = history.to_records()
#print(arr)
sp_growth = (arr[len(arr)-1][4] - arr[0][4])/(arr[0][4]) * 2
#print(sp_growth)
def bruh(sharpe):
    return sp_growth + sharpe/100 - (ir.interest_rate_risk_factor() - 1.0)/15 - (ur.unemployment_risk() - 1.0)/10
#print(bruh(2))