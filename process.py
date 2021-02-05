from clean import CleanedData

class ProcessedData(CleanedData):

    def __init__(self):
        # create cleaned object
        super().__init__()

        '''
        Algorithm to calculate numerical and percentage increase in average pricing between a number of years specified in the period keywoird argument
        Returns a dictionary
        '''
        self.change_frames = self.np.array([])
        
        for index, frame in enumerate([self.new, self.old]):
            data = {}
            for year in self.years:
                if year == 1976:
                    continue
                row = self.get_year(frame, year)
                prev_row = self.get_year(frame, year - 1)
                row_values = []

                for place in self.places:
                    place_value = self.get_location(row, place)
                    prev_place_value = self.get_location(prev_row, place)

                    difference = place_value - prev_place_value
                    percentage = round((difference / prev_place_value) * 100, 2)

                    row_values.append({'num':difference, 'percent':percentage})
                data[year] = row_values
 
            # appends the DataFrame remade with the calculated percentages dict above to self.change_frames
            if index == 0:
                self.new_change = self.pd.DataFrame.from_dict(data, orient="index", columns=self.places)
            else:
                self.old_change = self.pd.DataFrame.from_dict(data, orient="index", columns=self.places)

    def get_median(self, data_list):
        return data_list[len(data_list) // 2] 

    def get_mode(self, data_list):
        return self.statistics.mode(data_list)

if __name__=='__main__':
    processed = ProcessedData()
    
    change_dict = processed.search(processed.new_change, 'dublin', 2004)
    print(change_dict['num'])