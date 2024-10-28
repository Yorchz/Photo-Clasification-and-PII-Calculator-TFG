import streamlit as st

class Subtitle:

    @staticmethod
    def subtitle():
        st.markdown("<h1 class='subtitle'>Has seleccionado el apartado del modelo.</h1>", unsafe_allow_html=True)