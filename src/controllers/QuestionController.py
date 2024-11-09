from src.orchestrators.QuestionDataOrchestrator import QuestionDataOrchestrator
from src.services.internal.MongoDBService import MongoDBService


class QuestionController:
    """Controller to handle question data operations."""

    def __init__(self, config):
        self.mongodb_service = MongoDBService(config)

    def upload_questions(self, file_contents, selection):
        orchestrator = QuestionDataOrchestrator(self.mongodb_service)
        print(f"En el cuestionControler estan {file_contents} y tambien la seleccion {selection} \n")
        try:
            orchestrator.update_questions_from_text(file_contents, selection)
            print("All questions have been uploaded.")
        finally:
            self.mongodb_service.close()

    def load_questions(self, category):
        orchestrator = QuestionDataOrchestrator(self.mongodb_service)

        orchestrator.load_data(category)
        question_instance = orchestrator.initialize_data()
        questions = [value for key, value in vars(question_instance).items() if value]
        return questions

