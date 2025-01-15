import streamlit as st
from views.model.components.Subtitle import Subtitle
from views.model.components.Title import Title
from views.model.components.ModelConfiguration import ModelConfiguration
from views.model.components.ModelInstructions import ModelInstructions
from views.model.components.ModelSession import ModelSession
from views.model.components.ModelAssistant import ModelAssistant


class Model:

    @staticmethod
    def _initialize_session():
        ModelSession.session()

    @staticmethod
    def _generate_event():

        model_name, model_type = st.session_state.selected_model.split(" ", 1) \
            if st.session_state.selected_model else (None, None)

        return {
            'model_name': model_name,
            'model_type': model_type,
        }

    def run(self):
        Title.title()
        Subtitle.subtitle()
        self._initialize_session()

        configuration = ModelConfiguration()
        configuration.configuration()

        ModelInstructions.instructions()

        model_assistant = ModelAssistant(self._generate_event())
        model_assistant.event_generate_data()



