
class YamlTextParser:

    def __init__(self, file_content):
        self.file_content = file_content.decode("utf-8")
        print(f"Contenido ya en el back del codigo {self.file_content}")

    def parse(self):
        data = {}
        lines = self.file_content.splitlines()

        for line in lines:
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
