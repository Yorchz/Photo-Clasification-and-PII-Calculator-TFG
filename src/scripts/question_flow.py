from src.config.config import CONFIG
from src.data_access.yaml_flow.YamlDataTransformer import YamlDataTransformer
from src.data_access.yaml_flow.YamlGenerator import YamlGenerator
from src.data_access.yaml_flow.YamlTextParser import YamlTextParser


if __name__ == "__main__":

    QUESTION_FLOW_TXT = CONFIG['data'].get('question_flow_txt')
    QUESTION_FLOW_YAML = CONFIG['data'].get('question_flow_yaml')


    YamlGenerator(YamlDataTransformer(YamlTextParser(QUESTION_FLOW_TXT).parse()).transform(),
                  QUESTION_FLOW_YAML).generate()
