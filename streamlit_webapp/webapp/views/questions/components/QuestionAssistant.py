import streamlit as st
from dotenv import set_key
from views.questions.components.Resutl import Result
from src.services.api.QuestionUploaderService import QuestionUploaderService


class QuestionAssistant:

    def __init__(self, event):
        self.selected_file = event['selection']
        self.current_file = event['file']
        self.q_uploader_service = QuestionUploaderService()


    def event_upload_questions(self):
        if st.button("Actualizar Preguntas"):
            selection_status, file_status = self._check_inputs_status()
            print(f"Sleccion del fichero {self.selected_file}, Fichero {self.current_file}")
            if not (selection_status and file_status):
                response = self.q_uploader_service.upload(self.current_file, self.selected_file)
                print("La respuesta boleana es {}".format(response))
                Result.result(response, self.selected_file)
            else:
                st.error("Debe seleccionar la categoria del archivo y el nuevo archivo que quiere usar para su actualización.")



    def _check_inputs_status(self):
        selection_status = self.selected_file is None
        print(f"Seleccion fichero: {selection_status}")
        file_status = self.current_file is None
        print(f"Fichero: {file_status}")
        return selection_status, file_status
