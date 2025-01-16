from src.controllers.QuestionFlowManager import QuestionFlowManager

class QuestionHandler:
    """Handles the question flow, including generating answers and deciding which questions to skip."""

    def __init__(self, flow_config_path, prompts, model_training_controller):
        self.flow_manager = QuestionFlowManager(flow_config_path)
        self.prompts = prompts
        self.model_training_controller = model_training_controller
        self.skip_questions = set()

    def process_image(self, image):
        """Processes an image, generates answers for prompts and handles skipped questions."""
        answers = {}
        self.skip_questions = set()

        for key, prompt in self.prompts.items():
            if key in self.skip_questions:
                answers[key] = None
                continue

            answer = self.model_training_controller.generate_answer(image,
                                                                    prompt)
            normalized_answer = answer.lower() if isinstance(answer, str) else answer

            answers[key] = normalized_answer

            next_skip = self.flow_manager.get_next_questions(key, normalized_answer)
            if next_skip:
                self.skip_questions.update(next_skip)

        return answers

