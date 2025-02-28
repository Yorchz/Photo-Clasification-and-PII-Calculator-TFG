import io

import pandas as pd


class ImgProjectedDataProcessor:
    def __init__(self, data, conditions, selection):
        file_content = data.decode("utf-8")  # Decodificar los bytes a texto
        self.df = pd.read_csv(io.StringIO(file_content))
        self.conditions = conditions
        self.column_to_use = selection
        self.combinations = pd.DataFrame(
            [{'Column': col, 'Variable': var} for col, vars_ in self.conditions.items() for var in vars_])

    def calculate_normalized(self, column, variable):
        filtered_df = self.df[self.df[column].str.contains(variable, case=False, na=False)]
        percentages = filtered_df.groupby(self.column_to_use).size() / self.df.groupby(self.column_to_use).size() * 100
        return percentages.fillna(0).pipe(lambda p: (p - p.min()) / (p.max() - p.min()))

    def process_data(self):
        return [(row['Column'], row['Variable'], self.calculate_normalized(row['Column'], row['Variable'])) for _, row
                in self.combinations.iterrows()]