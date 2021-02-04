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
        new_house_data = pd.read_excel('pricing-by-area-new.xlsx')
        second_house_data = pd.read_excel('pricing-by-area-second.xlsx')

        self.places = np.array(new_house_data.iloc[0][1:8].tolist())

        self.new_headings = np.array(new_house_data.columns[1:8])
        self.second_headings = np.array(second_house_data.columns[1:8])
        data = {}

        # new housing listings
        for index, row in new_house_data.iterrows():
            if index < 7:
                continue
            
            year = row['YEAR']
            self.years.append(year)

            data[year] = list(map(lambda x: round(x), row[self.new_headings].tolist()))
            if index == 47:
                break
        
        self.new_averages = pd.DataFrame.from_dict(data, orient='index', columns=self.places)
        data = {}
        # old listings
        for index, row in second_house_data.iterrows():
            if index < 7:
                continue
            
            year = row['YEAR']

            data[year] = list(map(lambda x: round(x), row[self.second_headings].tolist()))
            if index == 47:
                break
        
        self.old_averages = pd.DataFrame.from_dict(data, orient='index', columns=self.places)
        
    def get_every_nyears(self, df, n=1):
        '''
        Gets a row from a given DataFrame every n rows.\n
        Returns a Series
        '''
        # returns one row every *years* rows

        # let years = 5
        # let year in row = 2006

        # check would be (2006 - 1976) % 5 == 0
        #                      30      % 5 == 0
        # This returns True, so this row would be included in the returned Series
        return df.iloc[[self.years.index(x) for x in self.years if (x - 1976) % n == 0]]

    def get_between(self, df, year1, year2):
        '''
        Gets the rows starting with YEAR = year1, and ending with YEAR = year2.\n
        Returns a DataFrame
        '''
        return df.loc[year1 : year2]

    def get_location(self, df, location):
        return df[location.capitalize()]
        
if __name__=='__main__':
    cleaned = CleanedData()
    print(cleaned.get_location(cleaned.old_averages, 'dublin'))
    # print(cleaned.new_averages.columns)
#     print(cleaned.search('2004', 'dublin'))
