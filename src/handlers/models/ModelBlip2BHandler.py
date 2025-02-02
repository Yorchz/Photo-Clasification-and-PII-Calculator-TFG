from src.handlers.models.model_factory.ModelHandler import ModelHandler


class ModelBlip2BHandler(ModelHandler):
    def __init__(self, model, _):
        self.model = model

    def generate(self, image, prompt):
        return self.model.generate({"image": image, "prompt": prompt})[0]


