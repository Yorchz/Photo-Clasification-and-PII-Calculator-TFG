
class TextFileParser:
    """Parses text files containing questions."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.parse_file()

    def parse_file(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        title = self.file_path.split('\\')[-1].replace('.txt', '')
        questions = {}
        for line in lines:
            if line.strip():
                question_number, question_text = line.split('-', 1)
                questions[question_number.strip()] = question_text.strip()

        return {
            "title": title,
            "questions": [{key: value} for key, value in questions.items()]
        }

    def get_data(self):
        return self.data
