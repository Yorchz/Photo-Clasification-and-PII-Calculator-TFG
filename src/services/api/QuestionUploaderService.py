from src.config.config import CONFIG
from src.controllers.QuestionController import QuestionController


class QuestionUploaderService:

    @staticmethod
    def upload(file, selection):
        question_controller = QuestionController(CONFIG['mongodb'])
        try:
            question_controller.upload_questions(file, selection)
            return True
        except Exception as e:
            print(f"Error al cargar las preguntas: {e}")
            return False

