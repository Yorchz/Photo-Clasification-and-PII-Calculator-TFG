import streamlit as st

class Explanation:

    @staticmethod
    def display():
        st.markdown(
            "<p class='instruction-title'>Aplicación en el ámbito del turismo de modelos de lenguaje visual (VLM) para la obtención de la imagen proyectada de fotografías mediante respuestas a preguntas visuales (VQA)</p>"
            "<p style='text-align: justify;'>Esta aplicación, desarrollada como ampliación de un Trabajo de Fin de Grado (TFG), utiliza modelos de lenguaje visual (VLM) para analizar imágenes turísticas y generar respuestas a preguntas visuales (VQA). "
            "Su objetivo es facilitar la comprensión y clasificación de fotografías turísticas mediante una interfaz interactiva, "
            "permitiendo un control integral sobre preguntas, flujo de respuestas, imágenes y resultados generados.</p>",
            unsafe_allow_html=True
        )
