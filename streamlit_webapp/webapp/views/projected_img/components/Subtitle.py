import streamlit as st

class Subtitle:

    @staticmethod
    def subtitle():
        st.markdown("<h1 class='subtitle'>Has seleccionado el apartado de imagen proyectada.</h1>",
                    unsafe_allow_html=True)