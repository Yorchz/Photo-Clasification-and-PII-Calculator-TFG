from src.config.config import CONFIG
from src.data_access.yaml_flow.YamlDataTransformer import YamlDataTransformer
from src.data_access.yaml_flow.YamlGenerator import YamlGenerator
from src.data_access.yaml_flow.YamlTextParser import YamlTextParser


class QFlowUploaderService:

    @staticmethod
    def upload(file):
        save_directory = CONFIG['data'].get('question_flow_yaml')
        try:
            data = YamlGenerator(YamlDataTransformer(YamlTextParser(file).parse()).transform(),
                          save_directory).generate()
            return True
        except Exception as e:
            print(f"Error al cargar el flujo de las preguntas: {e}")
            return False

