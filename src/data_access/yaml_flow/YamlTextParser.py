# src/parser.py
class YamlTextParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def parse(self):
        data = {}
        with open(self.filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                condition, questions = line.split(":")
                condition = condition.strip()
                questions, es_global = questions.split("|")
                questions_list = questions.strip().split()
                es_global = es_global.strip().split("=")[-1].lower() == "true"
                data[condition] = {
                    "skip_questions": questions_list,
                    "inherited_skip": es_global
                }
        return data
