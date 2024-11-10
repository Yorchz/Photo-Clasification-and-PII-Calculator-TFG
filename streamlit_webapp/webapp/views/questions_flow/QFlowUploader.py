import streamlit as st
from views.questions_flow.components.SubtitleUpload import SubtitleUpload
from views.questions_flow.components.TitleUpload import TitleUpload
from views.questions_flow.components.FSession import FSession
from views.questions_flow.components.FInstructions import FInstructions
from views.questions_flow.components.YamlFlowUploader import YamlFlowUploader

from src.services.api.QFlowUploaderService import QFlowUploaderService
from streamlit_webapp.webapp.views.questions_flow.components.QFlowAssistant import QFlowAssistant


class QFlowUploader:

    @staticmethod
    def _initialize_session():
        FSession.session()

    @staticmethod
    def _generate_event():
        return {
            'file': st.session_state.uploaded_file.getvalue() if st.session_state.uploaded_file is not None else {}
        }

    def run(self):
        TitleUpload.title()
        SubtitleUpload.subtitle()
        self._initialize_session()

        FInstructions.instructions()
        YamlFlowUploader.file_upload()

        question_flow_assistant = QFlowAssistant(self._generate_event())
        question_flow_assistant.event_upload_questions_flow()