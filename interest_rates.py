import requests
import time
import keys

data = requests.get(f"https://api.api-ninjas.com/v1/interestrate?name=American FED", headers = {'X-Api-Key': keys.api_ninjas_key }).json()
print(data)
def interest_rate_risk_factor():
    interest_rate = data['central_bank_rates'][0]['rate_pct']
    if(interest_rate > 4.0):
        return (interest_rate - 4.0)**2 * 1.1 + 1.1 
    return 1.0
#print(interest_rate_risk_factor())
