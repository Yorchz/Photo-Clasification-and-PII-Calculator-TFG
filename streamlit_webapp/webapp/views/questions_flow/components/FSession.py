import streamlit as st


class FSession:

    @staticmethod
    def session():
        if "is_initialized" not in st.session_state:
            st.session_state.uploaded_file = None
            st.session_state.is_initialized = []

