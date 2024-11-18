from src.config.config import CONFIG
from src.orchestrators.MainOrchestrator import MainOrchestrator


class ModelService:

    @staticmethod
    def run(model_name, model_type):
        model_controller = MainOrchestrator(CONFIG, model_name, model_type)
        try:
            model_controller.run()
            return True
        except Exception as e:
            print(f"Error al cargar las preguntas: {e}")
            return False

