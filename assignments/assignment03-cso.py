# Write a program that retrieves the dataset for the "Exchequer Account (Historical Series)" from data.cso.ie
# Store it into a file called "cso.json".
# Author: Irene Kilgannon

import requests
import json

url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'

# Make a HTTP GET request
response = requests.get(url)
data = response.json()

# Save to cso.json
with open("data/cso.json", "w") as f:    
    json.dump(data, f)