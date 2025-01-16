from src.config.config import CONFIG
from src.controllers.ImageController import ImageController


class ImageUploaderService:

    @staticmethod
    def upload(images):
        image_controller = ImageController(CONFIG)
        try:
            image_controller.upload_images(images)
            return True
        except Exception as e:
            print(f"Error al cargar las imagenes en la base de datos: {e}")
            return False

