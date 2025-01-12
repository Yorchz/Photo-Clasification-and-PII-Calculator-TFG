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
                <strong>Ejecución del Modelo</strong><br>
                   <img src="data:image/png;base64,{self.encode_image()}" class="card-img">
                   <div class="card-content" style="text-align: justify;">
                       Permite ejecutar el modelo utilizando las imágenes y preguntas proporcionadas. Si todo está correctamente configurado, 
                       genera un archivo CSV con la clasificación de las imágenes, que se guarda automáticamente para su uso posterior.
                   </div>
               </div>
               """,
            unsafe_allow_html=True
        )