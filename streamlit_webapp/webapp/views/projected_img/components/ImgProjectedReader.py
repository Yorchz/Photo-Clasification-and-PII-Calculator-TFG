import streamlit as st


class ImgProjectedReader:

    @staticmethod
    def file_upload():
        st.session_state.uploaded_file = st.file_uploader(
            label="Seleccione el archivo que desea utilizar para el análisis",
            type=['csv']
        )

