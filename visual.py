from process import ProcessedData
import plotly.express as px
import pandas as pd

class VisualisedData(ProcessedData):

    def __init__(self):
        super().__init__()

'''
if __name__=='__main__':
    visualised = VisualisedData()
    df = visualised.cleaned_data
    houses_2011 = df[
        df['Year'] == 2011
    ]
    dublin_houses_2011 = houses_2011[
        houses_2011['County'] == 'Dublin'
    ]
    print(round(dublin_houses_2011['Price'].mean()))
'''

if __name__ == '__main__':
    visualised = VisualisedData()
    df = visualised.cleaned_data
    data = []
    for place in visualised.places:
        if place == 'National':
            continue

        new_df = df[
            (df['Year'] == 2012) & (df['County'] == place) & (df['Description']== 'New')
        ]
        data.append([place, round(new_df['Price'].mean())])

    our_average_2012 = visualised.pd.DataFrame(data, columns=['Place', 'Price'])
    print(our_average_2012)
    graph = px.scatter(our_average_2012, x="Place", y="Price")
    graph.write_html("2012_new.html", full_html=False, include_plotlyjs=False)


'''
df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='lifeExp')
fig.show()
'''
