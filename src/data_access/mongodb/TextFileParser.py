
class TextFileParser:
    """Parses text files containing questions."""

    def __init__(self, file_content, selection):
        self.file_content = file_content.decode('utf-8')
        self.selection = selection
        self.data = self.parse_content()

    def parse_content(self):
        print(f"\n Cpntenido decodificado {self.file_content}, selección {self.selection}\n")
        lines = self.file_content.splitlines()
        questions = {}
        for line in lines:
            if line.strip():
                question_number, question_text = line.split('-', 1)
                questions[question_number.strip()] = question_text.strip()

        return {
            "title": self.selection,
            "questions": [{key: value} for key, value in questions.items()]
        }

    def get_data(self):
        return self.data
