import streamlit as st
from views.questions.components.Title import Title
from views.questions.components.QuestionConfiguration import QuestionConfiguration
from views.questions.components.QuestionUploader import QuestionUploader
from views.questions.components.QuestionAssistant import QuestionAssistant
from views.questions.components.QInstructions import QInstructions
from views.questions.components.QSession import QSession
from views.questions.components.Subtitle import Subtitle


class QuestionsUploader:

    @staticmethod
    def _initialize_session():
        QSession.session()

    @staticmethod
    def _generate_event():
        return {
            'selection': st.session_state.selected_file,
            'file': st.session_state.uploaded_file.getvalue() if st.session_state.uploaded_file is not None else {}
        }

    def run(self):
        Title.title()
        Subtitle.subtitle()
        self._initialize_session()

        question_conf = QuestionConfiguration()
        question_conf.configuration()

        QInstructions.upload_instructions()
        QuestionUploader.file_upload()

        question_assistant = QuestionAssistant(self._generate_event())
        question_assistant.event_upload_questions()

