import streamlit as st


class QuestionUploader:

    @staticmethod
    def file_upload():
        st.session_state.uploaded_file = st.file_uploader(
            label="Seleccione el archivo que desea guardar",
            type=['txt']
        )
