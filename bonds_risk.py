import requests
import time
seconds = time.time()
current_date = time.localtime(seconds);
month = ((current_date.tm_mon - 2) % 12) + 1
year = current_date.tm_year
if(month == 12):
    year -= 1
data = requests.get(f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates?filter=record_date:gt:{year}-{month}-00").json()['data']
#names = []
# for i in range(0, len(data)):
#     names.append(data[i]['security_desc'])
# names = names[0:6] + names[8:len(names)-2]
# print(names)
def get_interest(name):
    for i in range(0, len(data)):
        if(data[i]['security_desc'] == name):
            return data[i]['avg_interest_rate_amt']

