import streamlit as st

class Subtitle:
    @staticmethod
    def display(subtitle_text):
        st.markdown(f"<h2 class='subtitle' style='color: white;'>{subtitle_text}</h2>", unsafe_allow_html=True)
