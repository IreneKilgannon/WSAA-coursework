# Modify the program to print out the train codes

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

page = requests.get(url)
doc = parseString(page.content)

with open("train_codes.csv", mode = 'w', newline = '') as fp:
    train_writer = csv.writer(fp, delimiter = "\t", quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

    for objTrainPositionsNode in objTrainPositionsNodes:
        trainCodeNode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = trainCodeNode.firstChild.nodeValue.strip()
        #print(traincode)

        dataList = []
        dataList.append(traincode)
        train_writer.writerow(dataList)