import requests

import keys

api_url = 'https://api.api-ninjas.com/v1/country?name=United States'
response = requests.get(api_url, headers={'X-Api-Key': keys.ninja_api_key_will}).json()

unemployment_rate = response[0]['unemployment']/100
#unemployment_rate = .08
def unemployment_risk():
    if(unemployment_rate > .06):
        return ((unemployment_rate - .06)*100) **1.5 * .25 + 1.0
    return 1.0
