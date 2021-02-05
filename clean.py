import pandas as pd
import numpy as np

# makes color ANSI codes work properly
from os import system
system("")

from formatter import Formatter

class CleanedData(Formatter):

    years = []
    old_data = {}
    new_data = {}

    def __init__(self):
        '''
        Reads in data from specific excel files and tidies it.
        '''
        # Initialise raw DataFrames
        new_house_data = pd.read_excel('pricing-by-area-new.xlsx')
        second_house_data = pd.read_excel('pricing-by-area-second.xlsx')

        # Column headings used to traverse raw DataFrame
        self.new_headings = np.array(new_house_data.columns[1:8])
        self.second_headings = np.array(second_house_data.columns[1:8])

        # List of all places from Data
        # Column headings used to traverse cleaned data
        self.places = np.array(new_house_data.iloc[0][1:8].tolist())

        data = {}

        # new housing listings
        # also adds each year to a list (CleanedData.years)
        for index, row in new_house_data.iterrows():
            if index < 7:
                continue
            
            year = row['YEAR']
            self.years.append(year)

            # Shorthand for looping through row and rounding each value
            data[year] = list(map(lambda x: round(x), row[self.new_headings].tolist()))
            if index == 47:
                break
        
        self.new = pd.DataFrame.from_dict(data, orient='index', columns=self.places)
        data = {}
        # old listings
        for index, row in second_house_data.iterrows():
            if index < 7:
                continue
            
            year = row['YEAR']

            data[year] = list(map(lambda x: round(x), row[self.second_headings].tolist()))
            if index == 47:
                break
        
        self.old = pd.DataFrame.from_dict(data, orient='index', columns=self.places)
        
    def get_every_nyears(self, df, n=1):
        '''
        Gets a row from a given DataFrame every n rows.\n
        Returns a DataFrame.
        '''
        # returns one row every *years* rows

        # let years = 5
        # let year in row = 2006

        # check would be (2006 - 1976) % 5 == 0
        #                      30      % 5 == 0
        # This returns True, so this row would be included in the returned DataFrame
        return df.iloc[[self.years.index(x) for x in self.years if (x - 1976) % n == 0]]

    def get_between(self, df, year1, year2):
        '''
        Gets the rows starting with YEAR = year1, and ending with YEAR = year2. (Both inclusive).\n
        Returns a DataFrame.
        '''
        return df.loc[year1 : year2]

    def get_location(self, df, location):
        '''
        Gets the column of values associated with a location from CleanedData.places.\n
        Returns a DataFrame or int (if passed DataFrame only has 1 row).
        '''
        return df[[location.capitalize()]]

    def get_year(self, df, year):
        '''
        Gets the row of the passed year.\n
        Returns a DataFrame or int (if passed DataFrame only has 1 column).
        '''
        return df.loc[[int(year)]]

    def search(self, df, location, year):
        '''
        Gets the int value for the given location from the given year.\n
        Returns an int.
        '''
        return df.loc[int(year), location.capitalize()]
        
if __name__=='__main__':
    cleaned = CleanedData()
    print(type(cleaned.search(cleaned.new, 'dublin', 2004)))

#     print(cleaned.search('2004', 'dublin'))
