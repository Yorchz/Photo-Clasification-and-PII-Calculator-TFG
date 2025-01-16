
import streamlit as st


class PInstructions:

    @staticmethod
    def instructions_upload():
        st.markdown("""
            <div class='instructions-container'>
                <h5 style="font-size: 18px;">Estás en la sección de Carga o Actualización de Imágenes. Aquí puedes gestionar las imágenes que se utilizarán en el modelo.</h5>
                <ul style="list-style-type: disc;">
                    <li style="font-size: 14px;">Puedes subir una única imagen o un conjunto de imágenes, seleccionándolas desde tu dispositivo.</li>
                    <li style="font-size: 14px;">Las imágenes deben estar en formato <b>.jpg</b>. Asegúrate de que tengan la resolución adecuada para un análisis eficiente.</li>
                    <li style="font-size: 14px;">Es recomendable utilizar nombres claros y reconocibles para las imágenes, ya que el nombre será el único identificador para asociarlas con las clasificaciones generadas.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def instructions_download():
        st.markdown("""
            <div class='instructions-container'>
                <h5 style="font-size: 18px;">Descarga de Imágenes</h5>
                <ul style="list-style-type: disc;">
                    <li style="font-size: 14px;">En esta sección, puedes descargar todas las imágenes almacenadas en la base de datos del modelo.</li>
                    <li style="font-size: 14px;">Al hacer clic en el botón de descarga, se generará un archivo comprimido (<b>.zip</b>) que contendrá todas las imágenes disponibles.</li>
                    <li style="font-size: 14px;">El archivo <b>.zip</b> se guardará automáticamente en tu carpeta de descargas, facilitando el acceso y organización de las imágenes.</li>
                    <li style="font-size: 14px;">Este archivo comprimido puede ser utilizado para consultar, respaldar o analizar las imágenes fuera de la aplicación.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

