import pandas as pd
import numpy as np

# makes color ANSI codes work properly
from os import system
system("")

from formatting import Formatter

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

    def iter_years(self, offset=1):
        data_list = []
        for index, year in enumerate(self.years):
            if index % offset == 0:
                data_list.append(self.area_data[year])
        return [year, data_list]

    def iter_places(self):
        data_list = []
        for place in self.places:
            locale_dict = {}
            for year in self.years:
                locale_dict.update({
                    year: self.area_data[year][place]
                })
            data_list.append(locale_dict)
        return data_list

    def search(self, *args, data={}):
        # error check args
        if len(args) == 0:
            raise Exception('No search terms given, try entering a year like "2003"')
        if len(args) > 3:
            raise Exception(f'Too many search terms given, 3 is the most terms allowed. \n{len(args)} terms given')
        
        if len(data) == 0:
            data = self.area_data

        # parsing search args
        for arg in args:
            if arg.isalpha():
                arg = arg.capitalize()
                
        working_dict = data
        depth_searched = 0
        # narrow down dict depth for each search arg given
        for key in args:
            try:
                working_dict = working_dict[key]
                depth_searched += 1
            except KeyError:
                pass

        if depth_searched != 0:
            self.nice(f'\nTraversed {depth_searched} dimension(s) deep')
            return working_dict
        else:
            self.warn('\nSobran McFenniott Slimy Search couldn\'t traverse the dictionary with the given search values:')
            for arg in args:
                self.bold(' ' + arg)
            print('Did you enter the values correctly?')
            return
        

cleaned = CleanedData()

print(cleaned.search('new', '20006'))





