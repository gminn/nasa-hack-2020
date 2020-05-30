from covid-parse import Data

def main():
    print("Parsing time_series_covid_confirmed_US.csv into dictionary...")
    filename = "time_series_covid_confirmed_US.csv"
    covid_parsed = Data(filename)

if __name__ == "__main__":
    main()