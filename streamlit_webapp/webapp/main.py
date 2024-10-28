import base64
import os
import streamlit as st

from static_components.SideBar import SideBar
from views.ImagenesCarga import ImagenesCarga
from views.ImagenesDescarga import ImagenesDescarga
from views.home.Home import Home
from views.model.Model import Model
from views.questions.Questions import Questions
from views.questions_flow.QuestionsFlow import QuestionsFlow


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

        elif menu_selection == '⬇️ DU Preguntas':
            questions_control = Questions()
            questions_control.run()
        elif menu_selection == '⬆️ DU Lógica de Preguntas':
            question_flow = QuestionsFlow()
            question_flow.run()

        elif menu_selection == '⬇️ Descarga de Imágenes':
            imagenes_descarga_app = ImagenesDescarga()
            imagenes_descarga_app.run()
        elif menu_selection == '⬆️ Carga de Imágenes':
            imagenes_carga_app = ImagenesCarga()
            imagenes_carga_app.run()

        elif menu_selection == '🖥️ Modelo':
            modelo_app = Model()
            modelo_app.run()


if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
