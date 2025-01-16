import yaml

class YamlGenerator:
    def __init__(self, transformed_data, output_filepath):
        self.transformed_data = transformed_data
        self.output_filepath = output_filepath

    def generate(self):
        with open(self.output_filepath, 'w') as file:
            yaml.dump({"question_flow": self.transformed_data}, file, default_flow_style=False, sort_keys=False)
