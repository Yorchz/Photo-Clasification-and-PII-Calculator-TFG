import zipfile
from io import BytesIO
from PIL import Image
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

    def download_images(self):
        images, labels = self.load_dataset()
        zip_buffer = self._create_zip_buffer(images, labels)
        print("Archivo zip creado con éxito.")
        return zip_buffer

    @staticmethod
    def _create_zip_buffer(images, labels):
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for image, label in zip(images, labels):
                img_bytes = BytesIO()
                image.save(img_bytes, format="JPEG")  # Guardar en formato JPG
                img_filename = f"{label}.jpg"  # Asegurar que el nombre de archivo termine en .jpg
                zip_file.writestr(img_filename, img_bytes.getvalue())

        zip_buffer.seek(0)
        return zip_buffer


