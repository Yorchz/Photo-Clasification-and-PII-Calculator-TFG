from src.controllers.ImageController import ImageController
from src.controllers.ModelTrainingController import ModelTrainingController
from src.controllers.QuestionController import QuestionController
from src.services.DataProcessor import DataProcessor
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
        # Cargar preguntas de cada categoría
        subjects = self.question_controller.load_questions('Subject')
        activities = self.question_controller.load_questions('Activity')
        context = self.question_controller.load_questions('Context')

        # Generar prompts con el DataProcessor
        prompts = self.data_processor.generate_prompts(subjects, activities, context)
        print(prompts)

        # Cargar imágenes y etiquetas
        images, labels = self.image_controller.load_images()

        # Inicializar el manejador de preguntas
        question_handler = QuestionHandler('C:/Users/usuario/Desktop/Photo_Categorization/photoCategorization/src/config/question_flow.yaml', prompts, self.model_training_controller)

        # Procesar cada imagen y generar respuestas
        for idx, (image, label) in enumerate(zip(images, labels)):
            answers = question_handler.process_image(image)

            # Guardar las respuestas en el CSV
            ordered_answers = [answers[key] for key in prompts.keys()]
            self.data_processor.save_to_csv(label, ordered_answers)
            print(f"Processing image {idx + 1}/{len(images)}")

        print("Process completed successfully.")


