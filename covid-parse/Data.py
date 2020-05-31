import csv
import os
from collections import namedtuple

LatLon = namedtuple("LatLon", "latitude longitude")

class Data:
# constructor
    def __init__(self, filename): # add other parameters
        self.theData = {}
        self.countyLatLon = {}

        with open (os.path.join("/Users/catherinephilpott/Catherines Folder/Michigan/nasa-hackathon-2020/covid-parse", filename)) as csv_file:
            print(os.path.join("/Users/catherinephilpott/Catherines Folder/Michigan/nasa-hackathon-2020/covid-parse", filename))
            self.reader = csv.reader(csv_file, delimiter = ',')
            line = 0
            
            for row in self.reader:
                rowData = []
                if line != 0:
                    
                    if row[6] == "Florida" or row[6] == "South Carolina" or row[6] == "Alabama" or row[6] == "Georgia":
                        #print(row[6])
                        for x in range (11, 140):
                            
                            rowData.append(row[x])
                            
                        thisCountyLatLong = LatLon(latitude=row[8], longitude=row[9])
                        self.countyLatLon[row[10]] = thisCountyLatLong
                    
                        self.theData[row[10]] = rowData
                
                line = line + 1

    def getCovidDate(self, countyName)
        return self.theData[countyname]

    def getCountyLatLon(self, countyName)
        return self.countyLatLon[countyName]

    def writeRows(self):
        file = open("/Users/catherinephilpott/Catherines Folder/Michigan/nasa-hackathon-2020/covid-parse/writeData.txt","r+")
        vector_orange =self.theData["Orange, Florida, US"]
        for x in vector_orange:
            file.write(x)
            file.write(",")
        #print(vector_orange)
        #print(self.theData["Madison, Florida, US"])

                    

    