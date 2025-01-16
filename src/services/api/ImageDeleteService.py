from src.config.config import CONFIG
from src.controllers.ImageController import ImageController


class ImageDeleteService:

    @staticmethod
    def delete():
        image_controller = ImageController(CONFIG)
        try:
            image_controller.delete_images()
            return True
        except Exception as e:
            print(f"Error al cargar las imagenes en la base de datos: {e}")
            return False

