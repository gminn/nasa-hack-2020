from Data import Data

def main():
    print("Parsing time_series_covid_confirmed_US.csv into dictionary...")
    filename = "time_series_covid19_confirmed_US.csv"
    covid_parsed = Data(filename)
    #covid_parsed.printRows()
    covid_parsed.writeRows()

if __name__ == "__main__":
    main()
