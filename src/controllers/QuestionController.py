from src.orchestrators.QuestionDataOrchestrator import QuestionDataOrchestrator
from src.services.MongoDBService import MongoDBService


class QuestionController:
    """Controller to handle question data operations."""

    def __init__(self, config):
        self.mongodb_service = MongoDBService(config)

    def upload_questions(self, file_paths):
        orchestrator = QuestionDataOrchestrator(self.mongodb_service)
        try:
            for file_path in file_paths:
                orchestrator.update_questions_from_text(file_path)
            print("All questions have been uploaded.")
        finally:
            self.mongodb_service.close()

    def load_questions(self, category):
        orchestrator = QuestionDataOrchestrator(self.mongodb_service)

        orchestrator.load_data(category)
        question_instance = orchestrator.initialize_data()
        questions = [value for key, value in vars(question_instance).items() if value]
        return questions

