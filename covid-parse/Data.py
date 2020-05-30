import csv
import numpy as np
import os
from numpy import array
class Data:
# constructor
    def __init__(self, filename): # add other parameters
        self.theData = {}
        with open (os.path.join("/Users/catherinephilpott/Catherine's Folder/Michigan/nasa-hackathon-2020/covid-parse", filename)) as csv_file:
            self.reader = csv.reader(csv_file, delimiter = ',')
            line = 0
            rowData = np.array([])
            for row in self.reader:
                if(line != 0):
                    if row[6] == "Florida" or row[6] == "South Carolina" or row[6] == "Alabama" or row[6] == "Georgia":
                        for x in range (11, 139):
                            np.append(rowData, row[x])
                    self.theData[row[10]] = rowData
                line = line + 1
    def printRows(self):
        vector_orange =self.theData["Orange, Florida, US"]
        for x in vector_orange:
            print(x)
        #print(vector_orange)
        print(self.theData["Madison, Florida, US"])

                    

    
