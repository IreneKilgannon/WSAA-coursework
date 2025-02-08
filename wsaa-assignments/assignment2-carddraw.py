# Write a program that 'deals' i.e. prints out 5 cards from this API, https://deckofcardsapi.com/
# First shuffle and get the deck_id
# With the deck_id you can get the cards
# Author: Irene Kilgannon

import requests
import json

shuffle_cards_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

response = requests.get(shuffle_cards_url)

# JSON string is parsed as Python dictionary
response_dict = response.json()

# View keys in response_dict
#for key in response_dict:
#    print(key, ":", response_dict[key])

print('Deck ID:', response_dict['deck_id'])

# 
deck_id =  response_dict['deck_id']

# Deal five cards
deal_cards_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"

# 
response2 = requests.get(deal_cards_url)

deal_cards = response2.json()
#print(deal_cards)

for card in deal_cards['cards']:
    print(f"{card['value']} of {card['suit']}")
    

## References:
# https://stackoverflow.com/questions/18810777/how-do-i-read-a-response-from-python-request
# https://www.geeksforgeeks.org/response-json-python-requests/
# https://www.w3schools.com/python/module_requests.asp
# https://realpython.com/python-requests/
# https://stackoverflow.com/questions/6521892/how-to-access-a-dictionary-key-value-present-inside-a-list
# Accessing nested dictionaries in a list https://www.geeksforgeeks.org/accessing-value-inside-python-nested-dictionaries/