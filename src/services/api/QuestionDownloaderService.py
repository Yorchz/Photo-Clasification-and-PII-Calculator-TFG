from sympy.physics.quantum.gate import normalized

from src.config.config import CONFIG
from src.controllers.QuestionController import QuestionController


class QuestionDownloaderService:

    @staticmethod
    def download(selection):
        question_controller = QuestionController(CONFIG['mongodb'])

        normalized_data = question_controller.normalization_questions(selection)
        return normalized_data


