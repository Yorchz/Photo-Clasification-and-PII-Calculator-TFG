from src.config.config import CONFIG
from src.data_access.yaml_flow.YamlToTextTransformer import YamlToTextTransformer


class QFlowDownloaderService:

    @staticmethod
    def download():
        yaml_directory = CONFIG['data'].get('question_flow_yaml')
        normalized_data = YamlToTextTransformer(yaml_directory).save_to_txt()
        return normalized_data

