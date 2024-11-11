import os
from datetime import datetime
import yaml
from src.config.config import CONFIG

class YamlToTextTransformer:
    def __init__(self, yaml_file_path):
        self.yaml_file_path = yaml_file_path
        self.file_name = "Question_flow"
        self.out_path = CONFIG['data']['out_flow_path']
        self.yaml_data = self._load_yaml()

    def _load_yaml(self):

        with open(self.yaml_file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file).get("question_flow", {})

    def _transform(self):

        formatted_lines = []
        for question_id, details in self.yaml_data.items():
            for condition in details['conditions']:
                condition_value = condition['condition'].split("==")[-1].strip().strip("'")
                skip_questions = " ".join(condition['skip_questions'])
                inherited_skip = "true" if condition['inherited_skip'] else "false"
                formatted_lines.append(f"{question_id}={condition_value}: {skip_questions} | es_global={inherited_skip}")
        return formatted_lines

    def save_to_txt(self):

        formatted_lines = self._transform()

        full_path = os.path.join(self.out_path, f"{self.file_name}_{datetime.now().strftime('%Y%m%d')}.txt")
        print(f"Este es el phat donde se descargara la info {full_path}")

        with open(full_path, 'w', encoding='utf-8') as file:
            file.write("\n".join(formatted_lines))

        print(f"Archivo guardado en: {full_path}")
        return formatted_lines
