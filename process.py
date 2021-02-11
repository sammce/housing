from clean import CleanedData

class ProcessedData(CleanedData):

    def __init__(self, new=False):
        # create cleaned object
        super().__init__()

        self.raw_data = self.pd.read_csv("with_outliers.csv")
        self.cleaned_data = self.pd.read_csv("cleaned.csv")

        self.outlier_dict = {
            'min': {
                'Dublin': 218000,
                'Cork': 145000,
                'Galway': 90000,
                'Limerick': 120000,
                'Waterford': 100000,
                'Other Areas': 110000
            },
            'max': {
                'Dublin': 645000,
                'Cork': 550000,
                'Galway': 520000,
                'Limerick': 490000,
                'Waterford': 550000,
                'Other Areas': 600000,
            },
            'new': {
                'Dublin': -0.1,
                'Cork': 0,
                'Galway': 0.55,
                'Limerick': 0.38,
                'Waterford': 0.63,
                'Other Areas': 0.26,
            }
        }

        self.get_change()
        if new:
            self.clean_raw_prices(self.outlier_dict)
            self.test_averages()

    def get_median(self, df, column_label):
        return df.loc[:, column_label].median()

    def get_mode(self, df, column_label):
        return df.loc[:, column_label].mode()

    def get_mean(self, df, column_label):
        return df.loc[:, column_label].mean()

    def get_frequency(self, data_list):
        data = self.pd.Series(data_list)
        data.value_counts()
        data.value_counts(sort=False)
        return data.value_counts()

    def get_min_max(self, data_list):
        return min(data_list), max(data_list)

    def get_change(self):
        for index, frame in enumerate([self.new_avg, self.old_avg]):
            data = {}
            for year in self.years:
                if year == 1976:
                    continue
                row = self.get_year(frame, year)
                prev_row = self.get_year(frame, year - 1)
                row_values = []

                for place in self.places:
                    place_value = self.get_location(row, place)
                    prev_place_value = self.get_location(prev_row, place)

                    difference = place_value - prev_place_value
                    percentage = round((difference / prev_place_value) * 100, 2)

                    row_values.append({'numerical':difference, 'percent':percentage})
                data[year] = row_values

            # appends the DataFrame remade with the calculated percentages dict above to self.change_frames
            if index == 0:
                self.new_change = self.pd.DataFrame.from_dict(data, orient="index", columns=self.places)
            else:
                self.old_change = self.pd.DataFrame.from_dict(data, orient="index", columns=self.places)

    def clean_raw_prices(self, outlier_dict):
        df = self.raw_data
        dataframes = []
        for place in self.places_no_national:
            old_df = df[
                (df['County'] == place) & (df['Description'] == 'Second') & 
                (df['Price'] < outlier_dict['max'][place]) & 
                (df['Price'] > outlier_dict['min'][place])
            ]
            new_df = df[
                (df['County'] == place) & (df['Description'] == 'New') & 
                (df['Price'] < outlier_dict['max'][place] + outlier_dict['max'][place]*outlier_dict['new'][place]) & 
                (df['Price'] > outlier_dict['min'][place] + outlier_dict['min'][place]*outlier_dict['new'][place])
            ]
            dataframes.append(old_df)
            dataframes.append(new_df)
        df = self.pd.concat(dataframes)
        df.to_csv('cleaned.csv')
        print(self.success("Data cleaned!"))
        print(self.bold("359,629"), end=" ")
        print(self.success("rows became"), end=" ")
        print(self.bold(f"{self.tidy_comma_number(len(df.index))}"), end="\n\n")

    def test_averages(self):
        year = 2015
        new = False

        if new:
            gov_df = self.new_avg
            our_df = self.cleaned_data[self.cleaned_data['Description'] == 'New']
        else: 
            gov_df = self.old_avg
            our_df = self.cleaned_data[self.cleaned_data['Description'] == 'Second']

        for place in self.places_no_national:
            gov_avg = gov_df.loc[year, place]
            our_mean = our_df[(our_df['Year'] == year) & (our_df['County'] == place)]['Price'].mean()
            

            if new:
                our_avg = round(our_mean + (our_mean * self.new_change.loc[year, place]["percent"]*0.01 ))
            else: 
                our_avg = round(our_mean + (our_mean * self.old_change.loc[year, place]["percent"]*0.01 ))
            
            print(self.success('Place: ') + self.bold(place))
            print(self.nice('Government average: ') + self.bold(str(gov_avg)))
            print(self.nice('Our computed average: ') + self.bold(str(our_avg)))
            print(self.nice('Difference: ') + self.bold(str(our_avg - gov_avg)), end="\n\n")





if __name__ == '__main__':
    import plotly.express as px
    processed = ProcessedData()
    df = processed.cleaned_data
    data = []
    for year in processed.years_from_2010:
        for place in processed.places:
            if place == 'National':
                continue

            new_df = df[
                (df['Year'] == year) & (df['County'] == place) & (df['Description']== 'New')
            ]
            
            data.append([place, round(new_df['Price'].mean()), year])

    our_average_2012 = processed.pd.DataFrame(data, columns=['Place', 'Price', 'Year'])
    graph = px.scatter_3d(our_average_2012, x="Place", y="Price", z="Year", color="Place")
    # graph.write_html("2012_new.html", full_html=False, include_plotlyjs=False)
    graph.show()
    