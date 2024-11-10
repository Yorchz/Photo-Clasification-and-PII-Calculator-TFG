import streamlit as st
from views.questions.components.QResutl import QResult
from src.services.api.QuestionDownloaderService import QuestionDownloaderService
from src.services.api.QuestionUploaderService import QuestionUploaderService


class QuestionAssistant:

    def __init__(self, event):
        self.selected_file = event['selection']
        self.current_file = event['file']
        self.q_uploader_service = QuestionUploaderService()
        self.q_downloader_service = QuestionDownloaderService()


    def event_upload_questions(self):
        if st.button("Actualizar Preguntas"):
            selection_status, file_status = self._check_inputs_status()
            if not (selection_status and file_status):
                response = self.q_uploader_service.upload(self.current_file, self.selected_file)
                QResult.upload_result(response, self.selected_file)
            else:
                st.error("Debe seleccionar la categoria del archivo y el nuevo archivo que quiere usar para su actualización.")

    def event_download_questions(self):
        if st.button("Descargar Preguntas"):
            selection_status, file_status = self._check_inputs_status()
            if not selection_status:
                response = self.q_downloader_service.download(self.selected_file)
                print(f"Esta es la resupues {response}")
                QResult.download_result(response)
            else:
                st.error("Debe seleccionar la categoria del archivo para proceder a la descarga.")


    def _check_inputs_status(self):
        selection_status = self.selected_file is None
        file_status = self.current_file is None
        return selection_status, file_status
