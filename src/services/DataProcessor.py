import pandas as pd
import os


class DataProcessor:
    """Handles data processing tasks like prompt generation and CSV operations."""

    def __init__(self, config):
        self.csv_path = config['csv_path']
        self.headers = config['headers']
        self.initialize_csv()

    def initialize_csv(self):
        if not os.path.exists(self.csv_path):
            os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)
            df = pd.DataFrame(columns=self.headers)
            df.to_csv(self.csv_path, index=False)
            print(f"CSV initialized at {self.csv_path}")

    def generate_prompts(self, subjects, activities):
        prompts = [f"Question: {subject}? Answer:" for subject in subjects]
        prompts += [f"Question: {activity}? Answer:" for activity in activities]
        return prompts

    def save_to_csv(self, label, answers):
        data = [label] + answers
        df = pd.DataFrame([data], columns=self.headers)
        if os.path.exists(self.csv_path):
            df_existing = pd.read_csv(self.csv_path)
            df_combined = pd.concat([df_existing, df], ignore_index=True)
        else:
            df_combined = df
        df_combined.to_csv(self.csv_path, index=False)
        print(f"Data saved to {self.csv_path}")
