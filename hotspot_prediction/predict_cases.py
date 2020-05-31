import covid-parsing # TODO: change to underscore
import tiff-parsing


def main():
    # parse the COVID data into 2 hash tables
    execfile('covid_parsing.py') # TODO: might have to take main from covid-parsing instead
    # parse hurricane data into a hash table
    execfile('tiff_parsing.py') # TODO: might have to take main from tiff-parsing instead
    county_state_US = input("Enter '[County], [State], US'")
    # access the % population increase --- assuming member variable is from Image
    population_increase = light_parsed.nightHash[county_state_US] # TODO: get class instance name
    # access cases over time --- TODO: can be used to get total number of cases up through now
    cases_vector = covid_parsed.theData[county_state_US]
    # take most recent value from the vector
    cases_recent = c_vector[128] # most recent
    county_population = Data.pop[county_state_US] # TODO: get hash table name from Catherine
    percent_with_covid = cases_recent/county_population
    cases_new = county_population * percent_with_covid * population_increase
    # find sum of cases in that county
    sum_cases = 0
    for i in range 128
        sum_cases+=c_vector[i]
    print("The total number of cases before displacement in " + county_state_US + " is " + sum_cases + ".")
    sum_cases + cases_new
    print("The projected number of cases after displacement in " + county_state_US + " is " + sum_cases + ".") # TODO: is this the output that we want?



if __name__ == "__main__":
    main()