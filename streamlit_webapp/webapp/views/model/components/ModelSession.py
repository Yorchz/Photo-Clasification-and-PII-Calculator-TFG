import streamlit as st


class ModelSession:

    @staticmethod
    def session():
        if "is_initialized" not in st.session_state:
            st.session_state.selected_model = None
            st.session_state.is_initialized = []

