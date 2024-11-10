import streamlit as st
from views.questions.components.Subtitle import Subtitle
from views.questions.components.Title import Title
from views.questions.components.QuestionConfiguration import QuestionConfiguration
from views.questions.components.QInstructions import QInstructions
from views.questions.components.QuestionAssistant import QuestionAssistant
from views.questions.components.QSession import QSession


class QuestionsDownloader:

    @staticmethod
    def _initialize_session():
        QSession.session()

    @staticmethod
    def _generate_event():
        return {
            'selection': st.session_state.selected_file,
            'file': None
        }

    def run(self):
        Title.title()
        Subtitle.subtitle()

        question_conf = QuestionConfiguration()
        question_conf.configuration()

        QInstructions.download_instructions()

        question_assistant = QuestionAssistant(self._generate_event())
        question_assistant.event_download_questions()



