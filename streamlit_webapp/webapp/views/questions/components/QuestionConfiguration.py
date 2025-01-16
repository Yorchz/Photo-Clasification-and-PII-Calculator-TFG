import streamlit as st
from streamlit import selectbox


class QuestionConfiguration():

    def configuration(self):
        with st.expander("Selecciona el fichero sobre el que quieres trabajar"):
            selection = self._select_box()
            st.session_state.selected_file = selection
            st.write(f"Has seleccionado: {selection}")

    @staticmethod
    def _select_box():

        seleccion = st.selectbox(
            "Elige una opción:",
            ["Represented_activities_categorization", "Subject_categorization", "Context_categorization"],
            index=0
        )
        return seleccion