import streamlit as st

class Title:

    @staticmethod
    def title():
        st.markdown("<h1 class='title'>Modelo</h1>", unsafe_allow_html=True)