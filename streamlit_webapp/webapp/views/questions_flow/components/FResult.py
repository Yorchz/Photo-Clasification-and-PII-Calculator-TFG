import streamlit as st


class FResult:

    @staticmethod
    def result(response: bool):
        if response:
            st.write(f"Se han actualizado correctamente el flujo de preguntas")
        else:
            st.warning("No se pudo cargar el archivo dado. Verifique el archivo e intente nuevamente.")
