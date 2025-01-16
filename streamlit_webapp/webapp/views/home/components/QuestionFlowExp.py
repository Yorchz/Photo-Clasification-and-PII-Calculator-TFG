import base64
import streamlit as st
import os


class QuestionsFlowExp:

    PROJECT_PATH = os.getcwd()

    def encode_image(self):
        # Read and encode the image in base64 format
        with open(self.PROJECT_PATH + '/streamlit_webapp/assets/flow1-blue.png', "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    def display(self):
        # Display the card container with the image and text
        st.markdown(
            f"""
               <div class="card">
                <strong>Flujo de Preguntas</strong><br>
                   <img src="data:image/png;base64,{self.encode_image()}" class="card-img">
                   <div class="card-content" style="text-align: justify;">
                       En este apartado se gestiona el flujo lógico de las preguntas, permitiendo omitir aquellas irrelevantes según las respuestas dadas. 
                       Además, el flujo puede descargarse, modificarse y volver a cargarse para garantizar un proceso más eficiente y adaptado.
                   </div>
               </div>
               """,
            unsafe_allow_html=True
        )