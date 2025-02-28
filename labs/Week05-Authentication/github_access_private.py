import requests
import json
from config import apikeys as cfg

filename = "python-practice.json"

url = "https://api.github.com/repos/IreneKilgannon/PythonPractice"


apikey = cfg['githubkey']

response = requests.get(url, auth= ('token', apikey))

print(response.status_code)

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
