import torch
from lavis.models import load_model_and_preprocess

from src.handlers.models.model_factory.Factory import Factory


class ModelGenerator:

    def __init__(self, model_name: str, model_type: str):
        self.device = str(torch.device("cuda") if torch.cuda.is_available() else "cpu")
        self.model, self.vis_processors, self.txt_processors = self.load_model(model_name, model_type)
        self.model_key = f"{model_name}_{model_type}"

    def load_model(self, model_name, model_type):
        print(f"Loading model {model_name} of type {model_type} on {self.device}")
        model, vis_processors, txt_processors = load_model_and_preprocess(
            name=model_name, model_type=model_type, is_eval=True, device=self.device
        )
        return model, vis_processors, txt_processors

    def generate_answer(self, image_path, prompt):
        print(prompt)
        image = image_path.convert('RGB').resize((400, 300))
        image_tensor = self.vis_processors["eval"](image).unsqueeze(0).to(self.device)
        answer = self.model_generate(image_tensor, prompt)
        return answer

    def model_generate(self, image_tensor, prompt):
        cls = Factory.initialize_class(self.model_key)
        answer = cls(self.model, self.txt_processors).generate(image_tensor, prompt)
        return answer
