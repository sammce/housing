from visual import VisualisedData
import plotly.express as px
visualised = VisualisedData()

# Getting 3d scatter of county, price and year (OUR DATA)
# from 2010 - 2019
df = visualised.cleaned_data
data = []
for year in visualised.years_from_2010:
    for place in visualised.places_no_national:

        our_averages_df = df[
            (df['Year'] == year) & (df['County'] == place) & (df['Description']== 'New')
        ]
        
        data.append([place, round(our_averages_df['Price'].mean()), year])

our_average = visualised.pd.DataFrame(data, columns=['Place', 'Average Price (€)', 'Year'])
graph = px.scatter_3d(our_average, x="Place", y="Average Price (€)", z="Year", color="Place", title="Our computed averages for each county and year")
# graph.write_html("3d_scatter_per_year.html", full_html=False, include_plotlyjs=False)
# graph.show()




# bar chart of average price by county (OUR DATA)
# from 2010 - 2019
df = visualised.cleaned_data
year = 2010
new = False # Change to False to get second hand values
data = []

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
# graph.write_html(f"average_{year}_{file_desc}.html", full_html=False, include_plotlyjs=False)
# graph.show()




# bar chart of percentage increases in a specified year (GOV DATA)
# from 1976 - 2016
year = 2006
new = True # Change True to False to get second hand values
data = []

if new:
    df = visualised.new_change
    desc = "New"
    suffix = ""
else:
    df = visualised.old_change
    desc = "Second"
    suffix = " Hand"

for place in visualised.places:

    change_dict = df.loc[year, place] # this returns a dictionary
    percentage, numerical = change_dict['percent'], change_dict['numerical']
    data.append([place, numerical])

our_average = visualised.pd.DataFrame(data, columns=['Place', 'Change (%)'])
graph = px.bar(our_average, x="Place", y="Change (%)", color="Place", title=f"Numerical change from {year-1} - {year} ({desc} {suffix})")
# graph.write_html(f"percentage_{year}.html", full_html=False, include_plotlyjs=False)
# graph.show()




# bar chart of average price in specified year (GOV DATA)
# 1976 - 2016
year = 2008
new = False # Change to False to get second hand values
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
# graph.write_html(f"gov_average_{year}_{file_desc}.html", full_html=False, include_plotlyjs=False)
# graph.show()




# long bar chart of average price in specified year (OURS & GOV DATA)
# 2010 - 2019
year = 2010
new = False # Change to False to get second hand values
our_df = visualised.cleaned_data
if new:
    gov_df = visualised.new_avg
else:
    gov_df = visualised.old_avg
data = []

if new:
    desc = "New"
    suffix = ""
    file_desc = "new"
else:
    desc = "Second"
    suffix = "Hand"
    file_desc = "old"

for place in visualised.places_no_national:

    our_averages_df = our_df[
        (our_df['Year'] == year) & (our_df['County'] == place) & (our_df['Description'] == desc)
    ]

    gov_avg = df.loc[year, place]
    data.append([place, round(gov_avg), round(our_averages_df['Price'].mean())])

average = visualised.pd.DataFrame(data, columns=['Place', 'Our Average Price (€)', "Government Average (€)"])
graph = px.bar(average, x="Place", y=["Our Average Price (€)", "Government Average (€)"], title=f"Government and our averages in {year} ({desc} {suffix})", barmode="group")
# graph.write_html(f"gov_average_{year}_{file_desc}.html", full_html=False, include_plotlyjs=False)
# graph.show()




if __name__ == '__main__':
    pass
    # processed = ProcessedData(new=True)