
class YamlDataTransformer:
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data
        print(self.parsed_data)

    def transform(self):
        yaml_data = {}
        for condition, details in self.parsed_data.items():
            question_id, value = condition.split("=")
            value = value.lower()
            if question_id not in yaml_data:
                yaml_data[question_id] = {"conditions": []}
            yaml_data[question_id]["conditions"].append({
                "condition": f"value == '{value}'",
                "skip_questions": details["skip_questions"],
                "inherited_skip": details["inherited_skip"]
            })
        return yaml_data

