from src.services.internal.HuggingFaceService import HuggingFaceService


class ImageController:
    """Controller to handle image-related operations."""

    def __init__(self, config):
        self.hf_service = HuggingFaceService(config['huggingface'])

    def upload_images(self, image_dir: str):
        self.hf_service.upload_images(image_dir)

    def load_images(self):
        return self.hf_service.load_dataset()
