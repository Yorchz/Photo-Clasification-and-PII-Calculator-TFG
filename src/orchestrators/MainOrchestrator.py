from src.controllers.ImageController import ImageController
from src.controllers.ModelTrainingController import ModelTrainingController
from src.controllers.QuestionController import QuestionController
from src.services.DataProcessor import DataProcessor


class MainOrchestrator:
    """Main orchestrator to handle different processes."""

    def __init__(self, config):
        self.config = config
        self.question_controller = QuestionController(config['mongodb'])
        self.image_controller = ImageController(config)
        self.model_training_controller = ModelTrainingController(config)
        self.data_processor = DataProcessor(config['data'])

    def run(self):
        # Load questions from MongoDB
        subjects = self.question_controller.load_questions('Subject')
        activities = self.question_controller.load_questions('Activity')

        # Generate prompts
        prompts = self.data_processor.generate_prompts(subjects, activities)

        # Load images and labels from HuggingFace
        images, labels = self.image_controller.load_images()

        # Process images and generate answers
        for idx, (image, label) in enumerate(zip(images, labels)):
            answers = self.model_training_controller.generate_answers(image, prompts)
            self.data_processor.save_to_csv(label, answers)
            print(f"Processing image {idx + 1}/{len(images)}")

        print("Process completed successfully.")
