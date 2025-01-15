import streamlit as st
from views.images.components.PSession import PSession
from views.images.components.SubtitleDownload import SubtitleDownload
from views.images.components.TitleDownload import TitleDownload
from views.images.components.ImageAssistant import ImageAssistant
from views.images.components.PInstructions import PInstructions


class ImageDownloader:

    @staticmethod
    def _initialize_session():
        PSession.session()

    @staticmethod
    def _generate_event():
        return {
            'images': None
        }

    def run(self):
        TitleDownload.title()
        SubtitleDownload.subtitle()
        self._initialize_session()

        PInstructions.instructions_download()

        image_assistant = ImageAssistant(self._generate_event())

        col1, col2, col3 = st.columns([1, 0.5, 1])
        with col1:
            image_assistant.event_download_images()
        with col3:
            image_assistant.event_delete_images()