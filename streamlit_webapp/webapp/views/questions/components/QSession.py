import streamlit as st


class QSession:

    @staticmethod
    def session():
        if "is_initialized" not in st.session_state:
            st.session_state.selected_file = None
            st.session_state.uploaded_file = None
            st.session_state.is_initialized = []

