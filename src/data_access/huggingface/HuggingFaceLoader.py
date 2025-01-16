from datasets import load_dataset


from datasets import load_dataset

class HuggingFaceLoader:
    """Loader to retrieve datasets from Hugging Face."""

    def __init__(self, repo_name: str, token: str):
        self.repo_name = repo_name
        self.token = token

    def load_images(self):
        dataset = load_dataset(self.repo_name, token=self.token)
        return dataset

