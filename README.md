# housing
Analyzed price increase of housing in Ireland to predict the increase in upcoming years


# Usage Guide
main.py has access to an object from clean.py called DataCleaner, which has a few useful properties



# Example Code
from clean import DataCleaner

cleaner = DataCleaner()

print(cleaner.area_data['2004']['Dublin']['New'])      <---- Output: 322628

print(cleaner.places)     <---- Output: ['National', 'Dublin', 'Cork', 'Galway', 'Limerick', 'Waterford', 'Other Areas']

print(cleaner.years)     <---- Output: ['1976', '1977', '1978', '1979', '1980', ... '2013', '2014', '2015', '2016']
