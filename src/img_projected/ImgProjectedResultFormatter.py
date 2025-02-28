import pandas as pd


class ImgProjectedResultFormatter:
    @staticmethod
    def format_results(results_list, column_to_use):
        df_formatted = pd.DataFrame()
        for column, variable, percentages in results_list:
            if percentages is None:
                continue
            df_temp = pd.DataFrame({
                column_to_use: percentages.index,
                'Normalized Value': percentages.values
            })
            df_temp['Index'] = f"{column} - {variable}"
            df_temp = df_temp.pivot(index='Index', columns=column_to_use, values='Normalized Value')
            df_formatted = pd.concat([df_formatted, df_temp])
        return df_formatted