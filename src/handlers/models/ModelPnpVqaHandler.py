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
        samples = self._match_img_q_gradcam(samples)
        samples = self._question_guided(samples)
        print(samples['captions'][0][:5])
        pred_answers = self.model.forward_qa(samples, num_captions=50)
        print(f"Esta es la respuesta seleccionada {pred_answers[0]}")
        return pred_answers[0]

    def _match_img_q_gradcam(self, samples):
        return self.model.forward_itm(samples=samples)

    def _question_guided(self, samples):
        return  self.model.forward_cap(samples=samples, num_captions=50, num_patches=20)

