import streamlit as st

class Explanation:

    @staticmethod
    def display():
        st.markdown("<p class='instruction-title'>Esta es una aplicación de Clasificación de imagenes por medio de "
                    "modelos multimodales (Imagen-Texto) desarrollada como parte del proyecto de fin de grado. "
                    "La aplicación está diseñada para facilitar el uso y la clasificación de estas imagenes"
                    "mediante una interfaz interactiva.</p>"
                        , unsafe_allow_html=True)