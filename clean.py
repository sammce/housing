from formatter import Formatter

class CleanedData(Formatter):

    # Create dictionary to house cleaned DataFrames
    frames = {}

    def __init__(self):
        '''
        Reads in data from specific excel files and tidies it.
        '''
        # We import programmatically for uniformity across children classes
        # EG ProccessedData, VisualisedData

        # These classes will not need to import anything in their respective files
        from importlib import import_module
        self.np = import_module('numpy')
        self.pd = import_module('pandas')
        self.statistics = import_module('statistics')
        self.os = import_module('os')
        self.sys = import_module('sys')

        # Makes ANSI codes work for formatting
        self.os.system("")

        # Initialise raw DataFrames
        new_house_data = self.pd.read_excel('pricing-by-area-new.xlsx')
        second_house_data = self.pd.read_excel('pricing-by-area-second.xlsx')

        # Column headings used to traverse raw DataFrame
        self.new_headings = self.np.array(new_house_data.columns[1:8])
        self.second_headings = self.np.array(second_house_data.columns[1:8])

        # List of all years and places from Data
        # used as row and column identifiers respectively
        self.years = self.np.array([], dtype=int)
        self.places = self.np.array(new_house_data.iloc[0][1:8].tolist())

        # Create temp dictionary to house data
        data = {}

        # Clean new listings excel sheet
        # also adds each year to an array (CleanedData.years)
        for index, row in new_house_data.iterrows():
            if index < 7:
                continue
            
            year = row['YEAR']
            self.years = self.np.append(self.years, [year])

            # Shorthand for looping through row and rounding each value
            data[year] = list(map(lambda x: round(x), row[self.new_headings].tolist()))
            if index == 47:
                break
        
        self.new = self.pd.DataFrame.from_dict(data, orient='index', columns=self.places)
        
        # reset data dict
        data = {}

        # clean old listings excel sheet
        for index, row in second_house_data.iterrows():
            if index < 7:
                continue
            
            year = row['YEAR']

            data[year] = list(map(lambda x: round(x), row[self.second_headings].tolist()))
            if index == 47:
                break
        
        self.old = self.pd.DataFrame.from_dict(data, orient='index', columns=self.places)
        
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
        if n > 40:
            print(
                self.warn("There is only "),
                self.bold("40 "),
                self.warn("years in data"),
                self.bold("n"),
                self.warn("must be <= "),
                self.bold("40")
            )
            print(
                self.warn("You entered"),
                self.bold(str(n))
            )
            return
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
        try:
            search_result = df.loc[int(year), location.title()]
        except KeyError as e:
            print(
                self.warn("Year key "),
                self.bold(str(e.args[0])),
            )
            if type(e.args[0]) == int:
                print(
                    self.warn(f" yielded no results in DataFrame search.\nYears in data range from "),
                    self.bold('1976 - 2016')
                ) 
            else:
                print(
                    self.warn(f" yielded no results in DataFrame search.\nPlaces in data are "),
                    self.bold(', '.join(self.places))
                )
            return 
        return search_result
        
if __name__=='__main__':
    cleaned = CleanedData()
    new_df = cleaned.get_every_nyears(cleaned.new, 50)
    print(new_df)
#     print(cleaned.search('2004', 'dublin'))
