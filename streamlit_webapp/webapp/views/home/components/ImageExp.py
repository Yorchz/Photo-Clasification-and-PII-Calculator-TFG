import os
import base64
import streamlit as st

class ImageExp:
    PROJECT_PATH = os.getcwd()

    def encode_image(self):
        # Read and encode the image in base64 format
        with open(self.PROJECT_PATH + '/streamlit_webapp/assets/image-blue.png', "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    def display(self):
        # Display the card container with the image and text
        st.markdown(
            f"""
               <div class="card">
                <strong>Control de Imágenes</strong><br>
                   <img src="data:image/png;base64,{self.encode_image()}" class="card-img">
                   <div class="card-content" style="text-align: justify;">
                       Permite subir imágenes de forma individual o en grupos, así como descargarlas para su análisis posterior. 
                       Este apartado ofrece flexibilidad para gestionar las imágenes utilizadas en el proceso de clasificación.
                   </div>
               </div>
               """,
            unsafe_allow_html=True
        )

