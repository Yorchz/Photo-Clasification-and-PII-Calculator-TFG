import streamlit as st
from streamlit import selectbox


class QuestionConfiguration():

    def configuration(self):
        with st.expander("Selecciona el fichero sobre el que quieres trabajar"):
            seleccion = self._select_box()
            st.session_state.seleccion = seleccion
            st.write(f"Has seleccionado: {seleccion}")

    @staticmethod
    def _select_box():

        seleccion = st.selectbox(
            "Elige una opción:",
            ["a", "b", "c"],
            index=0
        )
        return seleccion