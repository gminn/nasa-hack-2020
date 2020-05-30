from Data import Data

def main():
    print("Parsing time_series_covid_confirmed_US.csv into dictionary...")
    filename = "time_series_covid_confirmed_US.csv"
    filepath = input('Enter filepath to project: ')
    covid_parsed = Data(filepath,filename)

if __name__ == "__main__":
    main()