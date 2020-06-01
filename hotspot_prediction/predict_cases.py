from covid_parse.Data import Data # TODO: change to underscore
from nighttime_parse.Image import Image

def parse_covid_data():
    # Inform user time series data is parsing
    print("Parsing time_series_covid_confirmed_US.csv into dictionary...")
    filename = "time_series_covid19_confirmed_US.csv"
    # call Data constructor to create instance of Data
    covid_parsed = Data(filename) # contains 3 hash tables
    # return instance of class to be used in main
    return covid_parsed

def parse_light_data(countyList, latLongHash, preMigrFilepath, postMigrFilepath):
    # call Image constructor to create instance of Image
    light_parsed = Image(countyList, latLongHash, preMigrFilepath, postMigrFilepath)
    return light_parsed # contains percent light change hash table


def main():
    # parse JHU data
    covid_parsed = parse_covid_data()
    # assign parameters to parse light data
    countyList = covid_parsed.countyNames
    latLongHash = covid_parsed.latLongHash
    preMigrFilepath = "snapshot-2018-09-23T00_00_00Z.tif"
    postMigrFilepath = "snapshot-2018-09-23T00_00_00Z.tif"
    # parse hurricane data 
    light_parsed = parse_light_data(countyList, latLongHash, preMigrFilepath, postMigrFilepath)
    # Get location user would like to project for from CL
    county_state_US = input("Enter '[County], [State], US'")
    # access the % population increase
    population_increase = light_parsed.nightHash[county_state_US]
    # access cases over time 
    cases_vector = covid_parsed.theData[county_state_US]
    # take most recent value from the vector
    cases_recent = cases_vector[128] 
    # Get population for each county
    county_population = Data.PopulationByCounty[county_state_US]
    percent_with_covid = cases_recent/county_population
    cases_new = county_population * percent_with_covid * population_increase
    # find sum of cases in that county
    sum_cases = 0
    for i in range (0, 128):
        sum_cases+=cases_vector[i]
    print("The total number of cases before displacement in " + county_state_US + " is " + sum_cases + ".")
    sum_cases + cases_new
    print("The projected number of cases after displacement in " + county_state_US + " is " + sum_cases + ".") # TODO: is this the output that we want?

if __name__ == "__main__":
    main()