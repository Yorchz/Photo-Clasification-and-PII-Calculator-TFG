from sympy.physics.quantum.gate import normalized

from src.config.config import CONFIG
from src.controllers.QuestionController import QuestionController


class QuestionDownloaderService:

    @staticmethod
    def download(selection):
        question_controller = QuestionController(CONFIG['mongodb'])
        try:
            normalized_data = question_controller.normalization_questions(selection)
            return normalized_data
        except Exception as e:
            print(f"Error al cargar las preguntas: {e}")
            return False

