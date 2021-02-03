from clean import CleanedData 

class ProcessedData(CleanedData):

    def __init__(self):
        # create cleaned object
        super().__init__()
        print(self.years)

    def percentage(self):
        pass

processed = ProcessedData()