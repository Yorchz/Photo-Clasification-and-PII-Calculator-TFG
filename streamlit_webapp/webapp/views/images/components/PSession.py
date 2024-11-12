import streamlit as st


class PSession:

    @staticmethod
    def session():
        if "is_initialized" not in st.session_state:
            st.session_state.uploader_images = None
            st.session_state.is_initialized = []

