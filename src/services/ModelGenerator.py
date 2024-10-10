import torch
from lavis.models import load_model_and_preprocess

class ModelGenerator:
    """Generates answers using the trained model."""

    def __init__(self, config):
        self.device = str(torch.device("cuda") if torch.cuda.is_available() else "cpu")
        self.model, self.vis_processors = self.load_model(config['model_name'], config['model_type'])

    def load_model(self, model_name, model_type):
        """Carga el modelo y los preprocesadores visuales usando los valores del config."""
        print(f"Loading model {model_name} of type {model_type}")
        model, vis_processors, _ = load_model_and_preprocess(
            name=model_name, model_type=model_type, is_eval=True, device=self.device
        )
        return model, vis_processors

    def generate_answer(self, image_path, prompt):
        """Genera una respuesta para una imagen dada y un prompt."""
        image = image_path.convert('RGB')
        image_tensor = self.vis_processors["eval"](image).unsqueeze(0).to(self.device)
        answer = self.model_generate(image_tensor, prompt)
        return answer

    def model_generate(self, image_tensor, prompt):
        """Genera una respuesta utilizando el modelo cargado."""
        answer = self.model.generate({"image": image_tensor, "prompt": prompt})
        return answer
