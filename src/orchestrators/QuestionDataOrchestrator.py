from src.data_access.mongodb.TextFileParser import TextFileParser
from src.deserializers.Deserializer import Deserializer
from src.deserializers.Factory import Factory
from src.queries.QueryManager import QueryManager


class QuestionDataOrchestrator:
    """Orchestrator to manage question data."""

    def __init__(self, mongodb_service):
        self.query_manager = QueryManager()
        self.loader = mongodb_service.get_loader()
        self.uploader = mongodb_service.get_uploader()
        self.question_data = None
        self.title = None

    def load_data(self, query_key: str):
        query = self.query_manager.get_query(query_key)
        if not query:
            raise ValueError(f"No query found for key: {query_key}")
        self.question_data = self.loader.get_document('categorization_questions', query)
        self.title = self.question_data['title']
        return self

    def initialize_data(self):
        if not self.question_data or not self.title:
            raise ValueError("Data not loaded. Call load_data() before initialize_data().")
        cls = Factory.initialize_class(self.title)
        question_instance = Deserializer.deserialize(self.question_data, cls)
        return question_instance

    def update_questions_from_text(self, text_file_path: str):
        parser = TextFileParser(text_file_path)
        data = parser.get_data()
        self.uploader.upload_data(data)
        print(f"Data from {text_file_path} has been uploaded to MongoDB.")
