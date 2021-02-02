from clean import CleanedData 

class ProcessedData(CleanedData):

    def __init__(self):
        # create cleaned object
        super().__init__()
        print(self.years)

    def percentage(self):
        # percentage change from year to year
        # percentage change decade to decade
        # percentage change overall
        pass