from clean import CleanedData 

class ProcessedData(CleanedData):

    def __init__(self):
        # create cleaned object
        super().__init__()

    def get_annual_change(self, period=1):
        '''
        Algorithm to calculate numerical and percentage increase in average pricing from 1 year to the next
        '''
        self.annual_data = {}
        count = 0

        for index, year in enumerate(self.years):
            if index == 0 or index % period != 0:
                continue

            self.annual_data[year] = {}

            for place in self.places:

                self.annual_data[year][place] = {}

                for time in ('New', 'Old'):
                    self.annual_data[year][place][time] = {}
                    count += 1

                    # get values using search method for each combination 
                    # of data (for that year and the year previous)
                    value = self.search(year, place, time)
                    previous_value = self.search(self.years[index - 1], place, time)
                    if type(value) == dict or type(previous_value) == dict:
                        continue

                    # calculate difference and percentage change
                    difference = value - previous_value
                    percentage = (difference / previous_value) * 100

                    # store processed data in dict
                    self.annual_data[year][place][time].update({
                        "Percentage": round(percentage, 2),
                        "Numerical": round(difference)
                    })

        self.nice("\nSearched area data", end=" ")
        self.bold(str(count), end=" ")
        self.nice("times")

        return self.annual_data

if __name__=='__main__':
    processed = ProcessedData()

    annual_change = processed.get_annual_change(period=10)
    print(annual_change)
    print(processed.search('1986', 'National', data=annual_change))
