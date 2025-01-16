import os
from datetime import datetime

from src.services.internal.HuggingFaceService import HuggingFaceService


class ImageController:
    """Controller to handle image-related operations."""

    def __init__(self, config):
        self.hf_service = HuggingFaceService(config['huggingface'])
        self.out_path = config['data']['out_info_path']

    def upload_images(self, images: list):
        self.hf_service.upload_images(images)

    def load_images(self):
        return self.hf_service.load_dataset()

    def delete_images(self):
        self.hf_service.delete_all_images()


    def download_images_zip(self, zip_name="imagenes.zip"):
        zip_buffer = self.hf_service.download_images()

        with open(os.path.join(self.out_path, f"{zip_name}_{datetime.now().strftime('%Y%m%d')}.zip"), "wb") as f:
            f.write(zip_buffer.getvalue())

        print(f"Archivo ZIP guardado.")
