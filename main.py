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
# graph.write_html("3d_scatter_per_year_scatter_3d.html", full_html=False, include_plotlyjs=False)
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
# graph.write_html(f"average_{year}_{file_desc}_bar.html", full_html=False, include_plotlyjs=False)
# graph.show()




# bar chart of percentage increases in a specified year (GOV DATA)
# from 1976 - 2016
year = 2008
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
# graph.write_html(f"percentage_{year}_bar.html", full_html=False, include_plotlyjs=False)
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
# graph.write_html(f"gov_average_{year}_{file_desc}_bar.html", full_html=False, include_plotlyjs=False)
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
# graph.write_html(f"gov_average_{year}_{file_desc}_multibar.html", full_html=False, include_plotlyjs=False)
# graph.show()



# bar chart of average price new and old in specified years side by side (BOTH OURS AND GOV DATA)
# 1976 - 2019
year = 2017


df = visualised.cleaned_data
data = []

if year > 2009:
    for place in visualised.places_no_national:

        our_averages_df_new = df[
            (df['Year'] == year) & (df['County'] == place) & (df['Description'] == "New")
        ]
        our_averages_df_old = df[
            (df['Year'] == year) & (df['County'] == place) & (df['Description'] == "Second")
        ]
        data.append([place, round(our_averages_df_new['Price'].mean()), round(our_averages_df_old['Price'].mean())])
else:
    for place in visualised.places:
        gov_average_new = visualised.new_avg.loc[year, place]
        gov_average_old = visualised.old_avg.loc[year, place]

        data.append([place, round(gov_average_new), round(gov_average_old)])

our_average = visualised.pd.DataFrame(data, columns=['Place', 'Average New Price (€)', 'Average Second Hand Price (€)'])
graph = px.bar(our_average, x="Place", y=['Average New Price (€)', 'Average Second Hand Price (€)'], title=f"New and Second Hand average prices for {year}", barmode="group")
# graph.write_html(f"new_and_old_average_{year}_multibar.html", full_html=False, include_plotlyjs=False)
# graph.show()




# scatter for average price in place through the years
place = "Dublin"
new = False # Change to False for second hand

desc = "New" if new else "Second Hand"
file_desc = "new" if new else "old"

our_df = visualised.cleaned_data
gov_df = visualised.new_avg if new else visualised.old_avg
data = []

for year in visualised.all_years:
    if year > 2009:
        our_averages_df = df[
            (df['Year'] == year) & (df['County'] == place) & (df['Description'] == "New")
        ] if new else df[
            (df['Year'] == year) & (df['County'] == place) & (df['Description'] == "Second")
        ]
        data.append([year, round(our_averages_df['Price'].mean())])
    else:
        gov_average = gov_df.loc[year, place]
        data.append([year, gov_average])
        
our_average = visualised.pd.DataFrame(data, columns=['Year', 'Average Price (€)'])
graph = px.line(our_average, x='Year', y='Average Price (€)', title=f"Price of {desc} houses in {place} from 1976 - 2019")
# graph.write_html(f"{place.lower()}_averages_{file_desc}_line.html", full_html=False, include_plotlyjs=False)
# graph.show()




# scatter for average price in every place through the years
new = True # Change to False for second hand

desc = "New" if new else "Second Hand"
file_desc = "new" if new else "old"

our_df = visualised.cleaned_data
gov_df = visualised.new_avg if new else visualised.old_avg
data = []

for year in visualised.all_years:
    if year > 2009:
        for place in visualised.places_no_national:
            our_averages_df = df[
                (df['Year'] == year) & (df['County'] == place) & (df['Description'] == "New")
            ] if new else df[
                (df['Year'] == year) & (df['County'] == place) & (df['Description'] == "Second")
            ]
            data.append([year, place, round(our_averages_df['Price'].mean())])
    else:
        for place in visualised.places_no_national:
            gov_average = gov_df.loc[year, place]
            data.append([year, place, gov_average])
        
our_average = visualised.pd.DataFrame(data, columns=['Year', 'County', 'Average Price (€)'])
graph = px.line(our_average, x='Year', y='Average Price (€)', color="County", title=f"Price of {desc} houses nationwide from 1976 - 2019")
# graph.write_html(f"nationwide_averages_line_{file_desc}.html", full_html=False, include_plotlyjs=False)
# graph.show()
if __name__ == '__main__':
    pass
    # processed = ProcessedData(new=True)