import streamlit as st


class YamlFlowUploader:

    @staticmethod
    def file_upload():
        st.session_state.uploaded_file = st.file_uploader(
            label="Seleccione el archivo con el flujo de preguntas que desea guardar o actualizar",
            type=['txt']
        )

