import streamlit as st

class DirectoryImageUploader:
    @staticmethod
    def images_upload():
        st.session_state.uploaded_images = st.file_uploader(
            label="Seleccione una o varias imágenes para cargar",
            type=['jpg'],
            accept_multiple_files=True
        )
