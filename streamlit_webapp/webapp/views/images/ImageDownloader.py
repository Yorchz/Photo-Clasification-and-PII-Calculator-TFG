import streamlit as st
from views.images.components.PSession import PSession
from views.images.components.SubtitleDownload import SubtitleDownload
from views.images.components.TitleDownload import TitleDownload


class ImageDownloader:

    @staticmethod
    def _initialize_session():
        PSession.session()

    @staticmethod
    def _generate_event():
        return {
            'file': st.session_state.uploaded_file.getvalue() if st.session_state.uploaded_file is not None else {}
        }

    def run(self):
        TitleDownload.title()
        SubtitleDownload.subtitle()
        self._initialize_session()