# Modify the program to print out the train latitudes.
# Write to a csv file

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

page = requests.get(url)
doc = parseString(page.content)

with open("train_latitudes.csv", mode = 'w', newline = '') as fp:
    train_writer = csv.writer(fp, quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

    for objTrainPositionsNode in objTrainPositionsNodes:
        trainLatitudeNode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
        train_latitude = trainLatitudeNode.firstChild.nodeValue.strip()

        dataList = []
        dataList.append(train_latitude)
        train_writer.writerow(dataList)
