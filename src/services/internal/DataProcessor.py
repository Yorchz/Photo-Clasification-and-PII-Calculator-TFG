import pandas as pd
import os


class DataProcessor:

    def __init__(self, config, store_name):
        self.csv_path = config['out_info_path'] + "/" + store_name + ".csv"
        self.headers = config['headers']
        self.initialize_csv()

    def initialize_csv(self):
        if not os.path.exists(self.csv_path):
            os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)
            df = pd.DataFrame(columns=self.headers)
            df.to_csv(self.csv_path, index=False)
            print(f"CSV initialized at {self.csv_path}")

    def generate_prompts(self, subjects, activities, contexts):
        categories = {'subject': subjects, 'action': activities, 'context': contexts}
        prompts = {f"{category}{i + 1}": f"Question: {item}? Answer:"
                   for category, items in categories.items()
                   for i, item in enumerate(items)}
        return prompts

    def _clean_answers(self, answers):
        return ['NONE' if answer is None else answer for answer in answers]

    def _build_dataframe(self, label, answers):
        data = [label] + answers
        return pd.DataFrame([data], columns=self.headers)

    def _read_and_combine_csv(self, df):
        if os.path.exists(self.csv_path):
            df_existing = pd.read_csv(self.csv_path)
            return pd.concat([df_existing, df], ignore_index=True)
        else:
            return df

    def save_to_csv(self, label, answers):
        answers = self._clean_answers(answers)

        df = self._build_dataframe(label, answers)
        df_combined = self._read_and_combine_csv(df)

        df_combined.to_csv(self.csv_path, index=False)
        print(f"Data saved to {self.csv_path}")
