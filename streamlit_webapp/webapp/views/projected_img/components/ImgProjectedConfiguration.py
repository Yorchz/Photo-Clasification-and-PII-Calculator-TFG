import streamlit as st


class ImgProjectedConfiguration:

    def configuration(self):
        with st.expander("Selecciona el nivel de profundidad del análisis"):
            selection = self._select_box()
            st.session_state.selected_zone = selection
            st.write(f"Has seleccionado: {selection}")

    @staticmethod
    def _select_box():
        seleccion = st.selectbox(
            "Elige una opción:",
            ["Basico", "Avanzado"],
            index=0
        )
        return seleccion