import plotly.express as px
from process import ProcessedData

class VisualisedData(ProcessedData):

    def __init__(self):
        super().__init__()

# bar chart of average price by county (OUR DATA)
# from 2010 - 2019
visualised = VisualisedData()
df = visualised.cleaned_data
year = 2010
new = True # Change to False to get second hand values
data = []
'''
if new:
    desc = "New"
    suffix = ""
    file_desc = "new"
else:
    desc = "Second"
    suffix = "Hand"
    file_desc = "old"

for place in visualised.places_no_national:

    our_averages_df = df[
        (df['Year'] == year) & (df['County'] == place) & (df['Description'] == desc)
    ]
    data.append([place, round(our_averages_df['Price'].mean())])

our_average = visualised.pd.DataFrame(data, columns=['Place', 'Average Price (€)'])
graph = px.bar(our_average, x="Place", y="Average Price (€)", color="Place", title=f"Our calculated averages for each county in {year} ({desc} {suffix})")
graph.write_html(f"average_{year}_{file_desc}.html", full_html=False, include_plotlyjs=False)
#graph.show()
'''


# bar chart of average price in specified year (GOV DATA)
# 1976 - 2016
year = 1980
new = True # Change to False to get second hand values
if new:
    df = visualised.new_avg
else:
    df = visualised.old_avg
data = []

if new:
    desc = "New"
    suffix = ""
    file_desc = "new"
else:
    desc = "Second"
    suffix = "Hand"
    file_desc = "old"

for place in visualised.places:

    gov_average = df.loc[year, place]
    data.append([place, round(gov_average)])

our_average = visualised.pd.DataFrame(data, columns=['Place', 'Average Price (€)'])
graph = px.bar(our_average, x="Place", y="Average Price (€)", color="Place", title=f"Government averages in {year} ({desc} {suffix})")
graph.write_html(f"gov_average_{year}_{file_desc}.html", full_html=False, include_plotlyjs=False)
#graph.show()
