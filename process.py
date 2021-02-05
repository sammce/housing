from clean import CleanedData

class ProcessedData(CleanedData):

    def __init__(self):
        # create cleaned object
        super().__init__()

    def get_annual_change(self, period=1):
        '''
        Algorithm to calculate numerical and percentage increase in average pricing between a number of years specified in the period keywoird argument
        Returns a dictionary
        '''
        pass

    
    
    
    
    
    

    def get_median(self, data_list):
        median = data_list[len(data_list) // 2]
        return median 

    def get_mode(self, data_list):
        return self.np.mode(data_list)

        
    def get_mean(self, data_list):
        return self.np.mean(data_list)
    
    def get_manual_mean(self, data_list):
        return sum(data_list) / len(data_list)


    def get_frequency(self, data_list):
        data = self.pd.Series(data_list)
        data.value_counts()
        data.value_counts(sort=false)
        return data.value_counts()

    def get_min_max(self, data_list):
        return min(data_list), max(data_list)





if __name__=='__main__':
    from process import ProcessedData
    
    processed = ProcessedData()

    annual_change = processed.get_annual_change()
    print(annual_change)
