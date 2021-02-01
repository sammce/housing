import pandas as pd
import numpy as np

#   Dictionary Layout : 
#  
#       Year: {
#           Location: Price
#       }
#
#   Example:
#       
#       area_data['2003']['Dublin']  <---  MUST BE CAPITALISED AND TYPE STR
#
#       This will return the average cost of housing that year in INT form
#       We will use this to compare our findings from kaggle price register data


#       We will find an algorithm to calculate average price increase from 2010 - 2016 using excel sheet
#       Then use that algorithm to predict 2017 - 2020 increase and perhaps even further
#       We could collect our own data from property listings to use as more recent data

class DataCleaner():

    def __init__(self):
        '''
        Reads in data from specific excel files 
        '''
        new_house_data = pd.read_excel('pricing-by-area-new.xlsx')

        area_data = {}
        headings = new_house_data.columns[1:8]
        places = new_house_data.iloc[0][1:8]
        
        for index, row in new_house_data.iterrows():
            # first year (1969/1970) has no data for most places
            # top row includes place names so we dont include it
            if index > 1:
                year = str(row['YEAR'])
                values = row[headings]

                area_data[year] = {}
                for pindex, place in enumerate(places):
                    # append Location: Value to year dictionary
                    # for each place in data
                    area_data[year].update({
                        place: round(values[pindex])
                    })
                
                if index == 47:
                    break
        self.existing_area_average_data = area_data
        
        print(area_data['2003']['Dublin'])
        
    def dictify(self):
        pass


x = DataCleaner()

