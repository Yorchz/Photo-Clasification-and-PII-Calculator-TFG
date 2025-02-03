import streamlit as st

class MainMenu:
    menu = {
        '🏡 Inicio': {'submenu': None},
        '❓ Preguntas': {
            'submenu': {
                '⬆️ Carga Preguntas': "Carga de preguntas",
                '⬇️️ Descargas Preguntas': "Descarga de preguntas",
            }
        },
        '🔁 Flujo de Preguntas': {
            'submenu': {
                '⬆️ Carga Flujo': "Carga del Flujo de preguntas",
                '⬇️ Descarga Flujo': "Descarga del Flujo de Preguntas",
            }
        },
        '🖼️ Imágenes': {
            'submenu': {
                '⬆️ Carga Imagenes': "Carga de Imágenes",
                '⬇️️ Descarga Imagenes': "Descarga de Imágenes"
            }
        },
        '🖥️ Modelo': {'submenu': None},
        'Imagen Projectada': {'submenu': None}
    }

    @staticmethod
    def display():
        return st.selectbox(
            '',
            list(MainMenu.menu.keys()),
            key="main_menu_unique",
            label_visibility="collapsed"
        )
