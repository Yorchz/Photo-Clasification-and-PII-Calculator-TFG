import streamlit as st
from src.services.api.QFlowUploaderService import QFlowUploaderService
from views.questions_flow.components.FResult import FResult


class QFlowAssistant:

    def __init__(self, event):
        self.current_file = event['file']
        self.q_uploader_service = QFlowUploaderService()


    def event_upload_questions_flow(self):
        if st.button("Actualizar Fujo de Preguntas"):
            file_status = self._check_inputs_status()
            if not file_status:
                print(f"Este es el contenido del fichero: \n {self.current_file}")
                response = self.q_uploader_service.upload(self.current_file)
                FResult.result(response)
            else:
                st.error("Debe seleccionar la categoria del archivo y el nuevo archivo que quiere usar para su actualización.")

    

    def _check_inputs_status(self):
        file_status = self.current_file is None
        print(f"Fichero: {file_status}")
        return file_status
