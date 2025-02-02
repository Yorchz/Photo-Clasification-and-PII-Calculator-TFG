from huggingface_hub import delete_repo


class HuggingFaceErased:

    def __init__(self, repo_name: str, token: str = None):
        self.repo_name = repo_name
        self.token = token

    def delete_images(self):
        delete_repo(repo_id=self.repo_name, repo_type="dataset", token=self.token)
