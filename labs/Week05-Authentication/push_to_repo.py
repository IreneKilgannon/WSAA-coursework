# Write a file that will make a change to your repository

# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#update-a-repository

# https://www.youtube.com/watch?v=jrtSUceudek - To update the repository using postman

import requests
import json
from config import apikeys as cfg

# Delete a file, blahblahblah.py

url = "https://api.github.com/repos/IreneKilgannon/PythonPractice/contents"
##
#myobj = myobj = {'somekey': 'somevalue'}

apikey = cfg['githubkey']

response = requests.get(url,auth= ('token', apikey))


print(response.status_code)
print(response.json())