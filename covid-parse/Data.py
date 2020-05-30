import csv
class Data:
# constructor
    def __init__(self, filename): # add other parameters
        with open (filename) as csv_file:
            self.reader = csv.reader(csv_file, delimiter = ',')
            line = 0
            for row in self.reader:
                if(line != 0):
                    if row[6] == "Florida" or row[6] == "South Carolina" or row[6] == "Alabama" or row[6] == "Georgia"
                        self.theData[row[10]] = 



    

