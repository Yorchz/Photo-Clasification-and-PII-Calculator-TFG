from src.data_access.mongodb.TextFileParser import TextFileParser
from src.deserializers.Deserializer import Deserializer
from src.deserializers.Factory import Factory
from src.queries.QueryManager import QueryManager


class QuestionDataOrchestrator:

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

    def update_questions_from_text(self, file_content, selection):
        data = TextFileParser(file_content=file_content, selection=selection).json_parse_content()
        self.uploader.upload_data(data)
        print("Data has been uploaded to MongoDB.")

    def download_questions_from_db(self, selection, query):
        print(f"La seleccion {selection} \n")
        data = TextFileParser(selection=selection, questions=query).txt_parse_content()
        return data
