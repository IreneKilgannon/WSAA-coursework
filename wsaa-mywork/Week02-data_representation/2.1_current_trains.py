# Write a program that prnts the data for all trains in Ireland to the console
# Use API http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML to retrieve the data
# Then only store trains that have a train code that starts with D

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

page = requests.get(url)
doc = parseString(page.content)

# Prints output to console
print(doc.toprettyxml())

