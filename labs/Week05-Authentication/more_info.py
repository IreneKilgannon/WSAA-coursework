# Write a script to get more information from your repository
# View the contents

import requests
import json
from config import apikeys as cfg

filename = "python-practice-contents.json"

url = "https://api.github.com/repos/IreneKilgannon/PythonPractice/contents"

apikey = cfg['githubkey']

response = requests.get(url, auth= ('token', apikey))

print(response.status_code)

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)


