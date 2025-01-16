import streamlit as st

class SubMenu:
    @staticmethod
    def display(options, key):
        return st.selectbox(
            '',
            options,
            key=key,
            label_visibility="collapsed"
        )
