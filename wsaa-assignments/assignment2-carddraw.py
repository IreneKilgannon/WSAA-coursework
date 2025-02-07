# Write a program that 'deals' i.e. prints out 5 cards from this API, https://deckofcardsapi.com/
# First you need to shuffle and get the deck_id
# With the deck_id you can get the cards
# Author: Irene Kilgannon

import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

response = requests.get(url)

# Check the response. How do I access the output in the response?
print(response.text)

# Using real python to get understanding of requests module
print(response.status_code)

# Response is serialized JSON content. Use .json(), according to realpython. Research this.
response_dict = response.json()


print('Deck ID:', response_dict['deck_id'])

# print("Drawn cards:")
# References:
# https://www.w3schools.com/python/module_requests.asp
# https://realpython.com/python-requests/