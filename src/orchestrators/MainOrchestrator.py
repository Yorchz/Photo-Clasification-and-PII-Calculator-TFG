from src.controllers.ImageController import ImageController
from src.controllers.ModelTrainingController import ModelTrainingController
from src.controllers.QuestionController import QuestionController
from src.services.internal.DataProcessor import DataProcessor
from src.handlers.QuestionHandler import QuestionHandler


class MainOrchestrator:
    """Main orchestrator to handle different processes."""

    def __init__(self, config):
        self.config = config
        self.question_controller = QuestionController(config['mongodb'])
        self.image_controller = ImageController(config)
        self.model_training_controller = ModelTrainingController(config)
        self.data_processor = DataProcessor(config['data'])

    def run(self):
        subjects = self.question_controller.load_questions('Subject_categorization')
        activities = self.question_controller.load_questions('Represented_activities_categorization')
        context = self.question_controller.load_questions('Context_categorization')

        prompts = self.data_processor.generate_prompts(subjects, activities, context)
        print(prompts)

        images, labels = self.image_controller.load_images()

        question_handler = QuestionHandler(self.config['data'].get('question_flow_yaml'), prompts, self.model_training_controller)

        for idx, (image, label) in enumerate(zip(images, labels)):
            answers = question_handler.process_image(image)

            ordered_answers = [answers[key] for key in prompts.keys()]
            self.data_processor.save_to_csv(label, ordered_answers)
            print(f"Processing image {idx + 1}/{len(images)}")

        print("Process completed successfully.")


