import streamlit as st
from views.projected_img.components.ImgProjectedSession import ImgProjectedSession
from views.projected_img.components.ImgProjectedConfiguration import ImgProjectedConfiguration
from views.projected_img.components.ImgProjectedInstructions import ImgProjectedInstructions
from views.projected_img.components.Subtitle import Subtitle
from views.projected_img.components.Title import Title
from views.projected_img.components.ImgProjectedReader import ImgProjectedReader


class ImgProjected:

    @staticmethod
    def _initialize_session():
        ImgProjectedSession.session()

    @staticmethod
    def _generate_event():
        return {
            'selection': st.session_state.selected_zone,
            'file': st.session_state.uploaded_file.getvalue() if st.session_state.uploaded_file is not None else {}
        }

    def run(self):
        Title.title()
        Subtitle.subtitle()
        self._initialize_session()

        configuration = ImgProjectedConfiguration()
        configuration.configuration()

        ImgProjectedInstructions.instructions()

        ImgProjectedReader.file_upload()



