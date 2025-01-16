from static_components.components.SubMenu import SubMenu
from static_components.components.Subtitle import Subtitle


class SubMenuHandler:
    @staticmethod
    def handle(menu_selection, menu_data):

        if menu_selection == '❓ Preguntas':
            Subtitle.display("Submenú Preguntas")
            return SubMenu.display(
                list(menu_data['❓ Preguntas']['submenu'].keys()),
                key="preguntas_submenu_unique"
            )

        elif menu_selection == '🔁 Flujo de Preguntas':
            Subtitle.display("Submenú Flujo de Preguntas")
            return SubMenu.display(
                list(menu_data['🔁 Flujo de Preguntas']['submenu'].keys()),
                key="imagenes_submenu_unique"
            )

        elif menu_selection == '🖼️ Imágenes':
            Subtitle.display("Submenú Imágenes")
            return SubMenu.display(
                list(menu_data['🖼️ Imágenes']['submenu'].keys()),
                key="imagenes_submenu_unique"
            )

        return menu_selection
