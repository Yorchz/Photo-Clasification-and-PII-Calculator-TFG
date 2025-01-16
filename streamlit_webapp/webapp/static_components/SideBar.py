import streamlit as st

from static_components.components.MainMenu import MainMenu
from static_components.components.SubMenuHandler import SubMenuHandler
from static_components.components.Title import Title


class SideBar:

    def run(self):
        with st.sidebar:
            Title.display()
            menu_selection = MainMenu.display()
            selection = SubMenuHandler.handle(menu_selection, MainMenu.menu)
        return selection
