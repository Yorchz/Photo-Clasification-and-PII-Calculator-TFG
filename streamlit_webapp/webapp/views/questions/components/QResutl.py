import streamlit as st
import pandas as pd
class QResult:

    @staticmethod
    def upload_result(response: bool, selection: str):
        if response:
            st.write(f"Se han actualizado las preguntas sobre la clasificación de {selection}")
        else:
            st.warning("No se pudo cargar las preguntas. Verifique el archivo e intente nuevamente.")

    @staticmethod
    def download_result(response: bool):
        if response:
            st.write(f"Se han actualizado las preguntas sobre la clasificación")
        else:
            st.warning("No se pudo cargar las preguntas. Verifique el archivo e intente nuevamente.")