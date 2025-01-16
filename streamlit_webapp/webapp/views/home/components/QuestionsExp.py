import base64
import streamlit as st
import os


class QuestionsExp:

    PROJECT_PATH = os.getcwd()

    def encode_image(self):
        # Read and encode the image in base64 format
        with open(self.PROJECT_PATH + '/streamlit_webapp/assets/question2-blue.png', "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    def display(self):
        # Display the card container with the image and text
        st.markdown(
            f"""
               <div class="card">
                <strong>Control de Preguntas</strong><br>
                   <img src="data:image/png;base64,{self.encode_image()}" class="card-img">
                   <div class="card-content" style="text-align: justify;">
                       Esta sección permite subir y descargar preguntas, modificarlas según las necesidades del usuario, 
                       y gestionar su uso de forma flexible y personalizable, adaptándose a diferentes escenarios y proyectos.
                   </div>
               </div>
               """,
            unsafe_allow_html=True
        )


