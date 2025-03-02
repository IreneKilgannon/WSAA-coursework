# Coding along with REST API crash course, https://www.youtube.com/watch?v=qbLc5a9jdXo
# Consume the stackoverflow API

import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
        print()
    else:
        print('skipped')
    print()