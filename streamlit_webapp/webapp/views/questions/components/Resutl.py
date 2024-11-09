import streamlit as st
import pandas as pd
class Result:

    @staticmethod
    def result(response: bool, selection: str):
        if response:
            st.write(f"Se han actualizado las preguntas sobre la clasificación de {selection}")
        else:
            st.warning("No se pudo cargar las preguntas. Verifique el archivo e intente nuevamente.")
