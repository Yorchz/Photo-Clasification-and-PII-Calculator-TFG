import streamlit as st
import pandas as pd
class ModelResult:

    @staticmethod
    def model_result(response: bool):
        if response:
            st.write(f"El modelo ha comenzado el proceso de clasificación")
        else:
            st.warning("A ocurrido algun problema durante la generación del modelo")