import csv
import os
from collections import namedtuple
import xlrd

LatLon = namedtuple("LatLon", "latitude longitude")
Counties = namedtuple("Counties", "countyName state")

class Data:
# constructor
    def __init__(self, filename): # add other parameters
        self.theData = {}
        self.countyLatLon = {}
        CountyNamesTemp = []
        self.PopulationByCounty = {}
        projectpath = input('Enter the complete filepath of the nasa-hackathon-2020 folder (ex. .../nasa-hackathon-2020')

        with open (os.path.join(projectpath, "/covid-parse", filename)) as csv_file:
            #print(os.path.join("/Users/catherinephilpott/Catherines Folder/Michigan/nasa-hackathon-2020/covid-parse", filename))
            self.reader = csv.reader(csv_file, delimiter = ',')
            line = 0
            
            for row in self.reader:
                rowData = []
                if line != 0:
                    
                    if row[6] == "Florida" or row[6] == "South Carolina" or row[6] == "Alabama" or row[6] == "Georgia":
                        #print(row[6])
                        thisCounty = Counties(countyName=row[5], state=row[6])
                        CountyNamesTemp.append(thisCounty)
                        temp = 5
                        for x in range (11, 140):
                            
                            rowData.append(row[x])
                            
                        thisCountyLatLong = LatLon(latitude=row[8], longitude=row[9])
                        self.countyLatLon[row[10]] = thisCountyLatLong
                    
                        self.theData[row[10]] = rowData
                
                line = line + 1

        self.countyNames = CountyNamesTemp

        # parse spreadsheets
        alabama = xlrd.open_workbook('Alabama_Population.xlsx')
        alabamaData = alabama.sheet_by_index(0)
        
           
        self._parseData(5,72,'Alabama_Population.xlsx',"Alabama")
        self._parseData(5, 164, 'Georgia-Population.xlsx',"Georgia")
        self._parseData(5,51, 'SC_Population.xlsx', "South Carolina")
        self._parseData(5, 72, 'Florida_Population.xlsx', "Florida")

        


    def _parseData(self,startRow, endRow, SpreadSheetName, stateName):
        spreadsheet = xlrd.open_workbook(SpreadSheetName)
        data = spreadsheet.sheet_by_index(0)
        
        for i in range(startRow, endRow):
            countyFullName = data.cell(i,0)
            fullName = countyFullName.value

            fullName = fullName.replace('.','',1)
            fullNameList = fullName.split(' ')
            countyName = fullNameList[0]
            countyFullName = countyName + ", " + stateName + ", US"

            populationCell = data.cell(i,12)
            populationCell = populationCell.value
            self.PopulationByCounty[countyFullName] = populationCell
           



    