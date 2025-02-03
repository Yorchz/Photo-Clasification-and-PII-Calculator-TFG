import base64
import os
import streamlit as st
from static_components.SideBar import SideBar
from views.projected_img.ImgProjected import ImgProjected
from views.images.ImageDownloader import ImageDownloader
from views.images.ImageUploader import ImageUploader
from views.questions_flow.QFlowDownloader import QFlowDownloader
from views.questions_flow.QFlowUploader import QFlowUploader
from views.questions.QuestionsDownloader import QuestionsDownloader
from views.home.Home import Home
from views.model.Model import Model
from views.questions.QuestionsUploader import QuestionsUploader


class MultiApp:
    """
    Main class that manages the Streamlit web application.
    """

    PROJECT_PATH = os.getcwd()

    def __init__(self):
        self.apps = []

    @staticmethod
    def _load_images(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    @staticmethod
    def _style_ulpgc_data(ulpgc_data):
        st.sidebar.markdown(
            f"""
               <div style="display: flex; justify-content: center; margin-top: -50px; margin-bottom: 30px">
                   <img src="data:image/png;base64,{ulpgc_data}" width="400" height="65">
               </div>
               """,
            unsafe_allow_html=True,
        )

    def _load_style(self):
        with open(self.PROJECT_PATH + '/streamlit_webapp/webapp/style.css') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def run(self):

        self._load_style()
        ulpgc_data = self._load_images(self.PROJECT_PATH + "/streamlit_webapp/assets/eii.png")
        self._style_ulpgc_data(ulpgc_data)

        menu_selection = SideBar().run()

        if menu_selection == '🏡 Inicio':
            home = Home()
            home.run()

        elif menu_selection == '⬆️ Carga Preguntas':
            questions_uploader = QuestionsUploader()
            questions_uploader.run()
        elif menu_selection == '⬇️️ Descargas Preguntas':
            questions_downloader = QuestionsDownloader()
            questions_downloader.run()

        elif menu_selection == '⬆️ Carga Flujo':
            flow_uploader = QFlowUploader()
            flow_uploader.run()
        elif menu_selection == '⬇️ Descarga Flujo':
            flow_downloader = QFlowDownloader()
            flow_downloader.run()

        elif menu_selection == '⬆️ Carga Imagenes':
            image_uploader = ImageUploader()
            image_uploader.run()
        elif menu_selection == '⬇️️ Descarga Imagenes':
            image_downloader = ImageDownloader()
            image_downloader.run()


        elif menu_selection == '🖥️ Modelo':
            model_app = Model()
            model_app.run()

        elif menu_selection == '📽 Imagen Projectada':
            img_projected = ImgProjected()
            img_projected.run()


if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
