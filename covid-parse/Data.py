import csv
import os

class Data:
# constructor
    def __init__(self, filename): # add other parameters
        self.theData = {}
        with open (os.path.join("/Users/catherinephilpott/Catherines Folder/Michigan/nasa-hackathon-2020/covid-parse", filename)) as csv_file:
            self.reader = csv.reader(csv_file, delimiter = ',')
            line = 0
            
            for row in self.reader:
                rowData = []
                if line != 0:
                    
                    if row[6] == "Florida" or row[6] == "South Carolina" or row[6] == "Alabama" or row[6] == "Georgia":
                        #print(row[6])
                        for x in range (11, 140):
                            
                            rowData.append(row[x])
                            
                            
                    
                    self.theData[row[10]] = rowData
                
                line = line + 1
    def writeRows(self):
        file = open("/Users/catherinephilpott/Catherines Folder/Michigan/nasa-hackathon-2020/covid-parse/writeData.txt","r+")
        vector_orange =self.theData["Orange, Florida, US"]
        for x in vector_orange:
            file.write(x)
            file.write(",")
        #print(vector_orange)
        #print(self.theData["Madison, Florida, US"])

                    

    
