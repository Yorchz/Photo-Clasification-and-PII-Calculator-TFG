import streamlit as st


class ModelResult:

    @staticmethod
    def model_result(elapsed_time: float):
        if elapsed_time is not None and elapsed_time >= 0:
            st.write(f"El modelo ha terminado el proceso en {elapsed_time:.4f} segundos.")
        else:
            st.warning("Ha ocurrido algún problema durante la generación del modelo.")