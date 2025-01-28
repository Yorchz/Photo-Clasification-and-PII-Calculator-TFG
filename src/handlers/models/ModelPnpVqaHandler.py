from random import sample

from prometheus_client import samples

from src.handlers.models.model_factory.ModelHandler import ModelHandler


class ModelPnpVqaHandler(ModelHandler):
    def __init__(self, model, txt_processors):
        self.model = model
        self.txt_processors = txt_processors

    def generate(self, image, prompt):
        question = self.txt_processors["eval"](prompt)
        samples = {"image": image, "text_input": [question]}
        pred_answers, _, _ = self.model.predict_answers(samples, num_captions=50, num_patches=20)
        return pred_answers[0]

    def _match_img_q_gradcam(self, samples):
        return self.model.forward_itm(samples=samples)

    def _question_guided(self, samples):
        return  self.model.forward_cap(samples=samples, num_captions=50, num_patches=20)

