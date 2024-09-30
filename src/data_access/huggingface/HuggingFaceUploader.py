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

    def upload_images(self, image_dir: str):
        """Sube imágenes al repositorio, combinando con las imágenes existentes si ya hay un dataset."""
        existing_dataset = self._get_or_create_repo()

        # Cargar las nuevas imágenes desde el directorio
        images = [{"image": str(path), "label": path.name} for path in Path(image_dir).glob("*") if path.is_file()]
        if not images:
            print(f"No images found in {image_dir}.")
            return

        # Crear el nuevo dataset con las imágenes de la carpeta
        new_dataset = Dataset.from_dict({"image": [img["image"] for img in images],
                                         "label": [img["label"] for img in images]},
                                        features=Features({"image": Image(), "label": Value("string")}))

        # Combinar datasets si ya existen imágenes
        combined_dataset = concatenate_datasets([existing_dataset, new_dataset]) if existing_dataset else new_dataset

        # Subir el dataset combinado
        DatasetDict({"train": combined_dataset}).push_to_hub(repo_id=self.repo_name, token=self.token)
        print(f"Dataset updated and pushed to {self.repo_name}.")
