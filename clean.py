from pandas import read_excel, isna

#   Dictionary Layout : 
#  
#       Year: {
#           Location: Price
#       }
#
#   Example:
#       
#       area_price_new['2003']['Dublin']  <---  MUST BE CAPITALISED AND TYPE STR
#
#       This will return the average cost of housing that year in INT form
#       We will use this to compare our findings from kaggle price register data


#       We will find an algorithm to calculate average price increase from 2010 - 2016 using excel sheet
#       Then use that algorithm to predict 2017 - 2020 increase and perhaps even further
#       We could collect our own data from property listings to use as more recent data

new_house_data = read_excel('pricing-by-area-new.xlsx')

# column heading needs to be weird because the government don't know how to use excel lol
# we slice 1 through 47 as first item is place name and there is 47 years included in data (48 is not included in slicing logic)
national_data = new_house_data['Annual New Property prices  (includes houses and apartments) €'].tolist()[1:48]

# same as above
dublin_data = new_house_data['Unnamed: 2'].tolist()[1:48]
print(national_data)