from src.services.internal.ModelGenerator import ModelGenerator


class ModelTrainingController:
    """Controller for model training and inference operations."""

    def __init__(self, config):
        self.model_generator = ModelGenerator(config['model'])

    def generate_answer(self, image_path, prompts):
        return self.model_generator.generate_answer(image_path, prompts)

