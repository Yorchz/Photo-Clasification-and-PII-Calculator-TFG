from src.handlers.models.model_factory.ModelHandler import ModelHandler


class ModelBlipVqaHandler(ModelHandler):
    def __init__(self, model, txt_processors):
        self.model = model

    def generate(self, image, prompt):
        return self.model.predict_answers(
            samples={"image": image, "text_input": prompt},
            inference_method="generate"
        )
