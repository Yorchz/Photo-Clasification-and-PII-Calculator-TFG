import streamlit as st
from views.images.components.PSession import PSession
from views.images.components.SubtitleUpload import SubtitleUpload
from views.images.components.TitleUpload import TitleUpload
from views.images.components.DirectoryImageUploader import DirectoryImageUploader
from views.images.components.PInstructions import PInstructions
from views.images.components.ImageAssistant import ImageAssistant


class ImageUploader:

    @staticmethod
    def _initialize_session():
        PSession.session()

    @staticmethod
    def _generate_event():
        return {
            'images': [
                {'filename': img.name, 'content': img.getvalue()}
                for img in st.session_state.get('uploaded_images', [])
            ]
        }

    def run(self):
        TitleUpload.title()
        SubtitleUpload.subtitle()
        self._initialize_session()

        PInstructions.instructions_upload()
        DirectoryImageUploader.images_upload()

        image_assistant = ImageAssistant(self._generate_event())

        col1, col2 = st.columns([1, 1])
        with col1:
            image_assistant.event_upload_images()
        with col2:
            image_assistant.event_delete_images()

