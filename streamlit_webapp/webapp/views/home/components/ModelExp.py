import base64
import os
import streamlit as st


class ModelExp:

    PROJECT_PATH = os.getcwd()

    def encode_image(self):
        # Read and encode the image in base64 format
        with open(self.PROJECT_PATH + '/streamlit_webapp/assets/run1-blue.png', "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    def display(self):
        # Display the card container with the image and text
        st.markdown(
            f"""
               <div class="card">
                <strong>Resumidor de Textos</strong><br>
                   <img src="data:image/png;base64,{self.encode_image()}" class="card-img">
                   <div class="card-content">
                       Genera resúmenes concisos a partir de textos largos, facilitando la comprensión rápida de la información.
                       Ejemplos de uso: generación de resúmenes de documentos, artículos, diarios de sesión, etc.
                   </div>
               </div>
               """,
            unsafe_allow_html=True
        )