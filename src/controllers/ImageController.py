from src.services.internal.HuggingFaceService import HuggingFaceService


class ImageController:
    """Controller to handle image-related operations."""

    def __init__(self, hf_config):
        self.hf_service = HuggingFaceService(hf_config)

    def upload_images(self, images: list):
        self.hf_service.upload_images(images)

    def load_images(self):
        return self.hf_service.load_dataset()
