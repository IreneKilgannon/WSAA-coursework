# Store only the trains whose start with D

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)

# Store XML in a file
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)


with  open('D_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

    for objTrainPositionsNode in objTrainPositionsNodes:

        # Extract the TrainCode and check if it starts with "D"
        trainCodeNode = objTrainPositionsNode.getElementsByTagName('TrainCode').item(0)
        if trainCodeNode and trainCodeNode.firstChild.nodeValue.startswith('D'):

            dataList = []
            for retrieveTag in retrieveTags:
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
        
        # Save as CSV file  
            train_writer.writerow(dataList)



