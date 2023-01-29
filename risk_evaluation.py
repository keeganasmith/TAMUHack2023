import pandas as pd
import requests
import json

api_url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

# API key in config.py which contains: bls_key = 'key'
import keys
key = '?registrationkey={}'.format(keys.unemployment_api_key)


#data = requests.get('https://api.bls.gov/publicAPI/v2/timeseries/data/').json()

#print(data)

#import requests
#import json
data = json.dumps({"seriesid": ['CUUR0000SA0','SUUR0000SA0'],"startyear":"2021", "endyear":"2023"})


p = requests.post(
        '{}{}'.format('https://api.bls.gov/publicAPI/v2/timeseries/data/', key), 
        headers={'Content-type': 'application/json'}, 
        data=data).json()

print(p)
    