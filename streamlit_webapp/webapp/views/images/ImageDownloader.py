import streamlit as st
from views.images.components.PSession import PSession
from views.images.components.SubtitleDownload import SubtitleDownload
from views.images.components.TitleDownload import TitleDownload

from streamlit_webapp.webapp.views.images.components.ImageAssistant import ImageAssistant
from streamlit_webapp.webapp.views.images.components.PInstructions import PInstructions


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
        image_assistant.event_download_images()