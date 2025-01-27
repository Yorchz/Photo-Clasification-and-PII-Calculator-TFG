from src.services.internal.ModelGenerator import ModelGenerator


class ModelTrainingController:

    def __init__(self, model_name: str, model_type: str):
        self.model_generator = ModelGenerator(model_name, model_type)

    def generate_answer(self, image_path, prompts):
        return self.model_generator.generate_answer(image_path, prompts)

