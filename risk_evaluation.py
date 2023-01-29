import requests

import keys

api_url = 'https://api.api-ninjas.com/v1/country?name=United States'
response = requests.get(api_url, headers={'X-Api-Key': keys.ninja_api_key_will}).json()


print(response[0]['unemployment'])

unemployment_rate = response[0]['unemployment']/100

print(unemployment_rate)
