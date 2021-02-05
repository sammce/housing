from clean import CleanedData
import statistics

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
        return statistics.mode(data_list)

        
    def get_mean(self, data_list):
        return statistics.mean(data_list)
    
    def get_manual_mean(self, data_list):
        return sum(data_list) / len(data_list)










if __name__=='__main__':
    from process import ProcessedData
    
    processed = ProcessedData()

    annual_change = processed.get_annual_change()
    print(annual_change)
