import streamlit as st

class Title:
    @staticmethod
    def display():
        st.markdown("<h1 class='title' style='color: white; margin-top: 80px;'>Menú Principal</h1>", unsafe_allow_html=True)
