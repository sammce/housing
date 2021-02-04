import pandas as pd
import numpy as np

# makes color ANSI codes work properly
from os import system
system("")

from formatter import Formatter

#   Dictionary Layout : 
#  
#       Year: {
#           Location: Price
#       }
#
#   Example:
#       
#       existing_area_data['2003']['Dublin']['New']  <---  MUST BE CAPITALISED AND TYPE STR
#
#       This will return the average cost of housing that year in INT form
#       We will use this to compare our findings from kaggle price register data


#       We will find an algorithm to calculate average price increase from 2010 - 2016 using excel sheet
#       Then use that algorithm to predict 2017 - 2020 increase and perhaps even further
#       We could collect our own data from property listings to use as more recent data


class CleanedData(Formatter):

    years = []

    def __init__(self):
        '''
        Reads in data from specific excel files and formats it
        '''
        new_house_data = pd.read_excel('pricing-by-area-new.xlsx')
        second_house_data = pd.read_excel('pricing-by-area-second.xlsx')

        self.area_data = {}
        new_headings = new_house_data.columns[1:8]
        second_headings = second_house_data.columns[1:8]
        places = new_house_data.iloc[0][1:8]
        self.places = places.tolist()

        second_row_values = []
        for index, row in second_house_data.iterrows():
            second_row_values.append(row[second_headings])

            if index == 48:
                break
        
        for index, row in new_house_data.iterrows():
            # first year (1969/1970) has no data for most places
            # top row includes place names so we dont include it
            if index > 6:
                year = str(row['YEAR'])
                # setup a list of all years included in data
                self.years.append(year)

                new_values = row[new_headings]
                second_values = second_row_values[index]

                self.area_data[year] = {}
                for pindex, place in enumerate(places):
                    # append values to dictionary
                    # for each place mentioned in data
                    self.area_data[year].update({
                        place: {
                            'New': round(new_values[pindex]),
                            'Old': round(second_values[pindex])
                        }
                    }) 
                if index == 47:
                    break

    def sort_by_place(self):
        for place in self.places:
            locale_dict = {}
            for year in self.years:
                locale_dict.update({place: {
                    year: self.area_data[year][place]
                }})
        return [place, locale_dict]

    def search(self, *args, data={}, iteration=0):

        if type(data) == int:
            self.nice(f'\nTraversed {iteration} dimension(s) deep')
            return data

        if type(args[0]) == tuple and len(args) == 1:
            args = args[0]

        # error check args
        if len(args) == 0:
            self.fatal('No search terms given, try entering a year like "2003"')
            exit()

        if type(data) == dict and len(data) == 0:
            data = self.area_data

        for arg in args:
            try:
                data = data[arg.capitalize()]
                break
            except KeyError:
                continue
        else:
            if iteration != 0:
                self.nice(f'\nTraversed {iteration} dimension(s) deep')
                return data
            else:
                self.warn('\nSobran McFenniott Slimy Search couldn\'t traverse the dictionary with the given search values:')
                for arg in args:
                    self.bold(' ' + arg)
                print('Did you enter the values correctly?')
        return self.search(args, data=data, iteration=iteration+1)

if __name__=='__main__':
    cleaned = CleanedData()
    print(cleaned.search('2004', 'dublin'))
