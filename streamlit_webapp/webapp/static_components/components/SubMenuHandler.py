from static_components.components.SubMenu import SubMenu
from static_components.components.Subtitle import Subtitle


class SubMenuHandler:
    @staticmethod
    def handle(menu_selection, menu_data):
        """
        Muestra y devuelve la selección de submenú según la opción seleccionada en el menú principal.
        """
        if menu_selection == '❓ Preguntas':
            Subtitle.display("Submenú Preguntas")
            return SubMenu.display(
                list(menu_data['❓ Preguntas']['submenu'].keys()),
                key="preguntas_submenu_unique"
            )

        elif menu_selection == '🖼️ Imágenes':
            Subtitle.display("Submenú Imágenes")
            return SubMenu.display(
                list(menu_data['🖼️ Imágenes']['submenu'].keys()),
                key="imagenes_submenu_unique"
            )

        # Si no hay submenú, retornar la selección del menú principal
        return menu_selection
