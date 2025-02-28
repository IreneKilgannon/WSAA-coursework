# Go to html2pdf.com, create an account and copy the API key
# Write a script that will convert the  Wikipedia website into a pdf


import requests
import urllib.parse
from config import apikeys as cfg

targetUrl = "https://en.wikipedia.org"


apikey = cfg["htmltopdfkey"]

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'html': targetUrl,'apiKey': apikey}

parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result = response.content

with open("document.pdf", "wb") as f:
    f.write(result)