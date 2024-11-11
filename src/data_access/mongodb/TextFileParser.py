import os
from datetime import datetime

from src.config.config import CONFIG


class TextFileParser:
    """Parses text files containing questions."""

    def __init__(self, file_content = None, selection = None, questions = None):
        self.file_content = file_content
        self.selection = selection
        self.questions = questions
        self.out_phat = CONFIG['data']['out_flow_path']
        print(f"Ruta de descarga {self.out_phat}\n")
        print(f"Contenido de preguntas {self.questions}\n")

    def json_parse_content(self):
        print(f"\n Cpntenido decodificado {self.file_content}, selección {self.selection}\n")
        lines = self.file_content.decode('utf-8').splitlines()
        questions = {}
        for line in lines:
            if line.strip():
                question_number, question_text = line.split('-', 1)
                questions[question_number.strip()] = question_text.strip()

        return {
            "title": self.selection,
            "questions": [{key: value} for key, value in questions.items()]
        }

    def txt_parse_content(self):
        formatted_questions = []

        for idx, (key, question_text) in enumerate(self.questions.__dict__.items(), start=1):
            formatted_questions.append(f"question{idx} - {question_text}")

        print(formatted_questions)

        with open(os.path.join(self.out_phat, f"{self.selection}_{datetime.now().strftime('%Y%m%d')}.txt"),
                  'w', encoding='utf-8') as file:
            file.write("\n".join(formatted_questions))

        print(f"Preguntas guardadas en {self.out_phat}")
        return formatted_questions

