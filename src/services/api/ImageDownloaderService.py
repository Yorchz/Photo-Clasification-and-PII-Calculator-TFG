from src.config.config import CONFIG
from src.controllers.ImageController import ImageController


class ImageDownloaderService:

    @staticmethod
    def download():
        image_controller = ImageController(CONFIG)
        try:
            image_controller.download_images_zip()
            return True
        except Exception as e:
            print(f"Error al cargar las imagenes en la base de datos: {e}")
            return False

