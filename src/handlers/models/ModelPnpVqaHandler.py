from src.handlers.models.model_factory.ModelHandler import ModelHandler


class ModelPnpVqaHandler(ModelHandler):
    def __init__(self, model):
        self.model = model

    def generate(self, image, prompt):
        samples = {"image": image, "text_input": [prompt]}
        return self.model.forward_qa(samples)
