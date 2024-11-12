from src.data_access.huggingface.HuggingFaceLoader import HuggingFaceLoader
from src.data_access.huggingface.HuggingFaceUploader import HuggingFaceUploader


class HuggingFaceService:
    """Service to manage Hugging Face operations."""

    def __init__(self, config):
        self.token = config['token']
        self.repo_name = config['repo_name']

    def upload_images(self, images: list):
        uploader = HuggingFaceUploader(self.token, self.repo_name)
        uploader.upload_images(images)
        print(f"Images from have been uploaded to {self.repo_name}.")

    def load_dataset(self):
        loader = HuggingFaceLoader(self.repo_name, token=self.token)
        dataset = loader.load_images()
        images = [item['image'] for item in dataset['train']]
        labels = [item['label'] for item in dataset['train']]
        print(f"Dataset from {self.repo_name} loaded successfully.")
        return images, labels
