import streamlit as st

class MainMenu:
    menu = {
        '🏡 Inicio': {'submenu': None},
        '❓ Preguntas': {
            'submenu': {
                '⬇️ DU Preguntas': "Carga/Descarga de preguntas",
                '⬆️ DU Lógica de Preguntas': "Carga/Descarga de Lógica de Preguntas",
            }
        },
        '🖼️ Imágenes': {
            'submenu': {
                '⬇️ Descarga de Imágenes': "Descarga de Imágenes",
                '⬆️ Carga de Imágenes': "Carga de Imágenes"
            }
        },
        '🖥️ Modelo': {'submenu': None},
    }

    @staticmethod
    def display():
        return st.selectbox(
            '',
            list(MainMenu.menu.keys()),
            key="main_menu_unique",
            label_visibility="collapsed"
        )
