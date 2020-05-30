import csv
import numpy as np
import os
from numpy import array
class Data:
# constructor
    def __init__(self, filepath, filename): # add other parameters
        projectPath = os.path.dirname(filepath)

        with open (os.path.join("/mnt/c/", filepath, filename)) as csv_file:
            self.reader = csv.reader(csv_file, delimiter = ',')
            line = 0
            rowData = np.array([])
            for row in self.reader:
                if(line != 0):
                    if row[6] == "Florida" or row[6] == "South Carolina" or row[6] == "Alabama" or row[6] == "Georgia":
                        for x in range (11, 139):
                            np.append(rowData, row[x])

                    line = line + 1

    

