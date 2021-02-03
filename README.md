# Housing Analysis
Analyzed price increase of housing in Ireland to predict the increase in upcoming years


# Usage Guide
`clean.py` contains a class called `CleanedData`, which has a few useful properties which are outlined below.

Similarly, `process.py` has a class called `ProcessedData`, which is outlined further down.

All classes inherit a `Formatter` class from `formatting.py`, which adds custom print colours to console. This is
also outlined below.


# Example Code


## Cleaner


### Initialising the cleaned data
```python
from clean import CleanedData
cleaned = CleanedData()
```

### Accessing the data


#### Static properties
```python

print(cleaned.places)     
# ['National', 'Dublin', 'Cork', 'Galway', 'Limerick', 'Waterford', 'Other Areas']

print(cleaned.years)    
# ['1976', '1977', '1978', '1979', '1980', ... '2013', '2014', '2015', '2016']
```

#### Search Method
```python

print(cleaned.search('new', '2004', 'dublin')) 
# 322628


# Custom data
dictionary = {
  'key': {
    'nested key': 'nested value'
  }
}
print(cleaned.search('nested key', 'key', data=dictionary))
# nested value 

```
The order of the search keys doesn't matter, the algorithm will search as deep as it can regardless
#### Iteration Methods
```python

for year, data in cleaned.iter_years():
  print(year)
  print(data)
  
# 2016
  
# {
#   'National': {'New': 313483, 'Old': 276272}, 'Dublin': {'New': 397676, 'Old': 351354}, 
#   'Cork': {'New': 293343, 'Old': 240683}, 'Galway': {'New': 262215, 'Old': 214645},
#   'Limerick': {'New': 239024, 'Old': 192721}, 'Waterford': {'New': 239409, 'Old': 179609}, 
#   'Other Areas': {'New': 272290, 'Old': 201272}
# }

# 40 of these would be printed, one for each year in study

for place, data in cleaned.iter_places():
  print(place)
  print(data)
  print(cleaned.search('new', '2016', data=data))
  
# Galway
  
# {'1976': {'New': 17842, 'Old': 16858}, '1977': {'New': 21715, 'Old': 20792}, '1978': {'New': 26244, 'Old': 27862}, 
# '1979': {'New': 30466, 'Old': 29539}, '1980': {'New': 33839, 'Old': 32978}, '1981': {'New': 39729, 'Old': 40333}, 
# '1982': {'New': 45460, 'Old': 42275}, '1983': {'New': 45650, 'Old': 42943}, '1984': {'New': 45774, 'Old': 47385}, 
# '1985': {'New': 49004, 'Old': 48220}, '1986': {'New': 49804, 'Old': 49767}, '1987': {'New': 48162, 'Old': 46427}, 
# '1988': {'New': 52238, 'Old': 54088}, '1989': {'New': 57936, 'Old': 56866}, '1990': {'New': 68019, 'Old': 61413}, 
# '1991': {'New': 66784, 'Old': 62226}, '1992': {'New': 75417, 'Old': 62874}, '1993': {'New': 74761, 'Old': 71298}, 
# '1994': {'New': 77375, 'Old': 69258}, '1995': {'New': 87783, 'Old': 78370}, '1996': {'New': 93050, 'Old': 88020}, 
# '1997': {'New': 109905, 'Old': 100791}, '1998': {'New': 118738, 'Old': 126914}, '1999': {'New': 138928, 'Old': 147152}, 
# '2000': {'New': 163824, 'Old': 166145}, '2001': {'New': 171161, 'Old': 189713}, '2002': {'New': 187607, 'Old': 206571}, 
# '2003': {'New': 223388, 'Old': 249404}, '2004': {'New': 242218, 'Old': 278813}, '2005': {'New': 274905, 'Old': 317811}, 
# '2006': {'New': 286176, 'Old': 336948}, '2007': {'New': 300750, 'Old': 344958}, '2008': {'New': 292777, 'Old': 333778}, 
# '2009': {'New': 236113, 'Old': 259285}, '2010': {'New': 219459, 'Old': 236695}, '2011': {'New': 229558, 'Old': 216748}, 
# '2012': {'New': 219233, 'Old': 205611}, '2013': {'New': 218308, 'Old': 199224}, '2014': {'New': 218016, 'Old': 198869}, 
# '2015': {'New': 241058, 'Old': 201805}, '2016': {'New': 262215, 'Old': 214645}}

# 262215

# This would print 7 times, one for each location
```

## Formatting 

### Inheriting the class
```python
from formatting
```


