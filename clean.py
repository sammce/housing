from formatter import Formatter
class CleanedData(Formatter):

    # Create dictionary to house cleaned DataFrames
    frames = {}

    def __init__(self):
        '''
        Reads in data from specific excel files and stores it in 
        various variables.
        '''
        # We import programmatically for uniformity across children classes
        # EG ProccessedData, VisualisedData

        # These classes will not need to import anything in their respective files
        from importlib import import_module
        self.np = import_module('numpy')
        self.pd = import_module('pandas')
        self.os = import_module('os')
        self.sys = import_module('sys')

        # Makes ANSI codes work for formatting
        self.os.system("")

        # Initialise raw DataFrames
        self.new_house_data = self.pd.read_excel('pricing-by-area-new.xlsx')
        self.second_house_data = self.pd.read_excel('pricing-by-area-second.xlsx')

        # Column headings used to traverse raw DataFrame
        self.new_headings = self.np.array(self.new_house_data.columns[1:8])
        self.second_headings = self.np.array(self.second_house_data.columns[1:8])

        # List of all years and places from Data
        # used as row and column identifiers respectively
        self.years = self.np.array([], dtype=int)
        self.places = self.np.array(self.new_house_data.iloc[0][1:8].tolist())
        # END OF AVERAGE PRICES PARSING
        

        # START OF RAW PRICES PARSING
        self.raw_data = self.pd.read_csv("with_outliers.csv")
        self.cleaned_data = self.pd.read_csv("cleaned.csv")

        outlier_dict = {
            'min': {
                'Dublin': 150000,
                'Cork': 125000,
                'Galway': 135000,
                'Limerick': 110000,
                'Waterford': 100000,
                'Other Areas': 80000
            },
            'max': {
                'Dublin': 570000,
                'Cork': 500000,
                'Galway': 520000,
                'Limerick': 440000,
                'Waterford': 460000,
                'Other Areas': 400000,
            },
            'new': 8,
        }

        self.clean_averages()
        # self.clean_raw_prices(outlier_dict)
    
    def clean_averages(self):
        # Clean new listings excel sheet
        # also adds each year to an array (CleanedData.years)

        # Create temp dictionary to house data
        data = {}
        for index, row in self.new_house_data.iterrows():
            if index < 7:
                continue
            
            year = row['YEAR']
            self.years = self.np.append(self.years, [year])

            # Shorthand for looping through row and rounding each value
            data[year] = list(map(lambda x: round(x), row[self.new_headings].tolist()))
            if index == 47:
                break
        
        self.new_avg = self.pd.DataFrame.from_dict(data, orient='index', columns=self.places)
        
        # reset data dict
        data = {}

        # clean old listings excel sheet
        for index, row in self.second_house_data.iterrows():
            if index < 7:
                continue
            
            year = row['YEAR']

            data[year] = list(map(lambda x: round(x), row[self.second_headings].tolist()))
            if index == 47:
                break
        
        self.old_avg = self.pd.DataFrame.from_dict(data, orient='index', columns=self.places)

    def clean_raw_prices(self, outlier_dict):
        # self.raw_final_new = []

        self.cleaned_prices = self.cleaned_prices.drop(columns=["Unnamed: 0.1"])
        # self.raw_price = self.raw_price.rename(columns={
        #     "Date of Sale (dd/mm/yyyy)":"Year",
        #     "Price (€)":"Price",
        #     "Description of Property":"Description",
        # })

        for index, row in self.raw_data.iterrows():
            # removes first character (€), any separating commas and turns to int
            price = row['Price']
            place = row['County']

            # if price < outlier_dict['min'][place] or price > outlier_dict['max'][place]:
                # self.raw_price = self.raw_price.drop([index])
        #     row_place = self.raw_price.loc[index, 'County']
        #     row_desc = self.raw_price.loc[index, 'Description']

        #     if not row_place in self.places:
        #         self.raw_price.loc[index, 'County'] = "Other Areas"
        #         row_place = "Other Areas"
            
        #     self.raw_price.loc[index, 'Year'] = int(row['Year'].split('/')[-1])

        #     if 'New' in row_desc:
        #         self.raw_price.loc[index, 'Description'] = "New"
        #         row_price = round((row_price / 100) * outlier_dict['new'])
        #     else:
        #         self.raw_price.loc[index, 'Description'] = "Second"

        #     # outlier dictionary is passed where min and max values are defined
            if price < outlier_dict['min'][place] or price > outlier_dict['max'][place]:
                self.cleaned_prices = self.cleaned_prices.drop([index])

        self.cleaned_prices.to_csv("cleaned.csv", index=False)
        print("Success!")
        
    def get_every_nyears(self, df, n=1):
        '''
        Gets a row from a given DataFrame every n rows.\n
        Returns a DataFrame.
        '''
        # returns one row every *years* rows

        # let n = 5
        # let year in row = 2006
        
        # check would be (year - 1976) % n == 0
        #                      30      % 5 == 0
        # This returns True, so this row would be included in the returned DataFrame
        return df.iloc[[self.years.tolist().index(x) for x in self.years if (x - 1976) % n == 0]]

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
        return df[location.title()]

    def get_year(self, df, year):
        '''
        Gets the row of the passed year.\n
        Returns a DataFrame or int (if passed DataFrame only has 1 column).
        '''
        return df.loc[int(year)]

    def get_at_index(self, df, index):
        return df.iloc[index]

    def search(self, df, location, year):
        '''
        Gets the int value for the given location from the given year.\n
        Returns an int, or prints an error message if no results are found.
        '''
        return df.loc[int(year), location.title()]
        
if __name__=='__main__':
    cleaned = CleanedData()
    dublin_houses = cleaned.cleaned_data.loc[cleaned.cleaned_data['County'] == 'Dublin']
    houses_2015 = dublin_houses.loc[dublin_houses['Year'] == 2015]
    mean_2015 = houses_2015['Price'].mean()
    print(mean_2015)
    # print(cleaned.raw_price)  
#     print(cleaned.search('2004', 'dublin'))
