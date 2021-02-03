<<<<<<< HEAD
from clean import CleanedData

class ProcessedData():
    
    def __init__(self):
        
        super().__init__()
        print(self.years)
        pass
    
    def percentage(self):
        pass
  
  
print(cleaned.places)

print(cleaned.years)

for year, data in cleaned.iter_years():
  print(year)
  print(data)

=======
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

processed = ProcessedData()
>>>>>>> 486d65084607c20f52c014c7ac6240bddb9abda0
