from src.config.config import CONFIG
from src.controllers.ImageController import ImageController
from src.data_access.yaml_flow.YamlDataTransformer import YamlDataTransformer
from src.data_access.yaml_flow.YamlGenerator import YamlGenerator
from src.data_access.yaml_flow.YamlTextParser import YamlTextParser


class ImageUploaderService:

    @staticmethod
    def upload(images):
        image_controller = ImageController(CONFIG['huggingface'])
        try:
            image_controller.upload_images(images)
            return True
        except Exception as e:
            print(f"Error al cargar las imagenes en la base de datos: {e}")
            return False

