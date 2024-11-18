import streamlit as st
from views.questions.components.QResutl import QResult
from src.services.api.QuestionDownloaderService import QuestionDownloaderService
from src.services.api.QuestionUploaderService import QuestionUploaderService


class ModelAssistant:

    def __init__(self, event):
        self.selected_model = event['model_name']
        self.model_type = event['model_type']



    def event_generate_data(self):
        if st.button("Generar datos"):
            model_type_status, model_status = self._check_inputs_status()
            print(f"{self.selected_model}, {self.model_type}")

    def _check_inputs_status(self):
        selection_status = self.selected_model is None
        file_status = self.model_type is None
        return selection_status, file_status
