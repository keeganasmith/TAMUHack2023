import time
import requests
import csv
import heapq as hq
import symbols
import risk
import stock_growth
seconds = time.time()
current_date = time.localtime(seconds);
month = ((current_date.tm_mon - 2) % 12) + 1
year = current_date.tm_year
if(month == 12):
    year -= 1
data = requests.get(f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates?filter=record_date:gt:{year}-{month}-00").json()['data']

def get_max_bond():
    max_interest = 0
    max_name = ""
    for i in range(0, len(data)):
        if(float(data[i]['avg_interest_rate_amt']) > max_interest):
            max_interest = float(data[i]['avg_interest_rate_amt']);
            max_name = data[i]['security_desc']
    return [max_name, max_interest]
# with open('nasdaq_screener_1675002051544.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             symbols.append(row[0])

def get_best_portfolio(number = 5, num_stocks = 50):
    stocks = symbols.symbol;

    new_stocks = []
    joe = []
    i = 0;
    while(i < len(stocks)):
        new_stocks.append(stocks[i])
        i += len(stocks)//50
    stocks = new_stocks
    for stock in stocks:
        try:
            sharpe = risk.sharpe([[stock, 10]], '3mo')[0]
        except:
            continue
        growth = stock_growth.bruh(sharpe)
        if(len(joe) < number):
            hq.heappush(joe, (growth, stock));
            continue;
        if(growth > joe[0][0]):
            hq.heappop(joe)
            hq.heappush(joe, (growth, stock))
    output = []
    for tup in joe:
        output.append([tup[1], 10])
    return [output, stock_growth.bruh(risk.sharpe(output)[0])]



#print(get_best_portfolio())