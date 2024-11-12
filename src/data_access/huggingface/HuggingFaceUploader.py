from pathlib import Path
from datasets import load_dataset, Dataset, Features, Image, Value, concatenate_datasets, DatasetDict
from huggingface_hub import HfApi


class HuggingFaceUploader:
    def __init__(self, token: str, repo_name: str):
        self.token = token
        self.repo_name = repo_name
        self.api = HfApi()

    def _repo_exists(self) -> bool:
        """Verifica si el repositorio ya existe en Hugging Face."""
        try:
            self.api.repo_info(repo_id=self.repo_name, repo_type="dataset", token=self.token)
            return True
        except Exception as e:
            if "404" in str(e) or "not found" in str(e).lower():
                return False

    def _create_repo(self):
        """Crea un repositorio en Hugging Face si no existe."""
        self.api.create_repo(repo_id=self.repo_name, repo_type="dataset", token=self.token, exist_ok=True)

    def _get_or_create_repo(self):
        """Carga el dataset si el repositorio existe, o crea el repositorio si no existe."""
        if not self._repo_exists():
            self._create_repo()
            return None
        return load_dataset(self.repo_name, split="train", token=self.token)

    def upload_images(self, images: list):

        existing_dataset = self._get_or_create_repo()

        new_dataset = Dataset.from_dict(
            {
                "image": [img["content"] for img in images],  # Contenido binario de cada imagen
                "label": [img["filename"] for img in images]  # Nombre del archivo como etiqueta
            },
            features=Features({"image": Image(), "label": Value("string")})
        )

        combined_dataset = concatenate_datasets([existing_dataset, new_dataset]) if existing_dataset else new_dataset

        DatasetDict({"train": combined_dataset}).push_to_hub(repo_id=self.repo_name, token=self.token)
        print(f"Dataset updated and pushed to {self.repo_name}.")
