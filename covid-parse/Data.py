import csv
import os
from collections import namedtuple
import xlrd

LatLon = namedtuple("LatLon", "latitude longitude")
Counties = namedtuple("Counties", "countyName state")

class Data:
    # constructor
    def __init__(self, filename): 
        # initialize member variables
        self.theData = {}
        self.countyLatLon = {}
        CountyNamesTemp = []
        self.PopulationByCounty = {}
        
        projectpath = input('Enter the complete filepath of the nasa-hackathon-2020 folder (ex. .../nasa-hackathon-2020')
    
        # Parse COVID-19 cases data:
        with open (os.path.join(projectpath, "/covid-parse", filename)) as csv_file:
            self.reader = csv.reader(csv_file, delimiter = ',')
            line = 0
            #iterate over each row in csv and parse
            for row in self.reader:
                rowData = []
                if line != 0:
                    
                    # only parse data for FL, AL, SC, GA
                    if row[6] == "Florida" or row[6] == "South Carolina" or row[6] == "Alabama" or row[6] == "Georgia":
                        
                        # Create struct for given county and add to county names list
                        thisCounty = Counties(countyName=row[5], state=row[6])
                        CountyNamesTemp.append(thisCounty)
                        
                        # add county's latitude/longitude to hash table
                        thisCountyLatLong = LatLon(latitude=row[8], longitude=row[9])
                        self.countyLatLon[row[10]] = thisCountyLatLong

                        # add number of cases as a vector and add to hash table
                        for x in range (11, 140):
                            rowData.append(row[x])
                            
                        self.theData[row[10]] = rowData
                
                line = line + 1

        # store list of county names as member variable
        self.countyNames = CountyNamesTemp

        # parse spreadsheets
        self._parseData(5,72,'Alabama_Population.xlsx',"Alabama")
        self._parseData(5, 164, 'Georgia-Population.xlsx',"Georgia")
        self._parseData(5,51, 'SC_Population.xlsx', "South Carolina")
        self._parseData(5, 72, 'Florida_Population.xlsx', "Florida")

        


    def _parseData(self,startRow, endRow, SpreadSheetName, stateName):
        #open spreadsheet
        spreadsheet = xlrd.open_workbook(SpreadSheetName)
        data = spreadsheet.sheet_by_index(0)
        
        # add population data to hash table
        for i in range(startRow, endRow):

            # get and format county name
            countyFullName = data.cell(i,0)
            fullName = countyFullName.value

            fullName = fullName.replace('.','',1)
            fullNameList = fullName.split(' ')
            countyName = fullNameList[0]
            countyFullName = countyName + ", " + stateName + ", US"

            # get 2019 population for given county 
            populationCell = data.cell(i,12)
            populationCell = populationCell.value

            # store population data in hash table as a member variable
            self.PopulationByCounty[countyFullName] = populationCell
           



    