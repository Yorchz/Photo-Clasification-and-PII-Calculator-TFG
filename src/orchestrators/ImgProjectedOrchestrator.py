from src.config.config import CONFIG
from src.img_projected.ImgProjectedDataProcessor import ImgProjectedDataProcessor
from src.img_projected.ImgProjectedResultFormatter import ImgProjectedResultFormatter
from src.orchestrators.MainOrchestrator import MainOrchestrator


class ImgProjectedOrchestrator:

    def __init__(self, data, selection):
        self.conditions =  CONFIG['data']['conditions']
        self.data = data
        print(selection)
        self.selection = 'Country' if selection == 'Basico' else 'Region'

    def processed_data(self):
        processor = ImgProjectedDataProcessor(self.data, self.conditions, self.selection)
        return self._formatter(processor.process_data())

    def _formatter(self, data):
        formatter = ImgProjectedResultFormatter()
        return formatter.format_results(data, self.selection)





