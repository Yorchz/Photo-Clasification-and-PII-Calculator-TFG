from src.config.config import CONFIG
from src.orchestrators.ImgProjectedOrchestrator import ImgProjectedOrchestrator
from src.orchestrators.MainOrchestrator import MainOrchestrator


class ImgProjectedService:

    @staticmethod
    def projection_calculator(data, selection):
        img_projected_controller = ImgProjectedOrchestrator(data, selection)
        result = img_projected_controller.processed_data()
        return result


