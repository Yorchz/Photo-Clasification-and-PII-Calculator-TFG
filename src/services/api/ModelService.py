from src.config.config import CONFIG
from src.orchestrators.MainOrchestrator import MainOrchestrator


class ModelService:

    @staticmethod
    def run(model_name, model_type, stop_flag):
        model_controller = MainOrchestrator(CONFIG, model_name, model_type, stop_flag)
        execution_time = model_controller.run
        return execution_time


