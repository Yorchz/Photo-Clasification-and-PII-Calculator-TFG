import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    'mongodb': {
        'host': os.getenv('MONGO_HOST'),
        'port': int(os.getenv('MONGO_PORT')),
        'db_name': os.getenv('MONGO_DB_NAME'),
    },
    'huggingface': {
        'token': os.getenv('HF_TOKEN'),
        'repo_name': os.getenv('HF_REPO_NAME'),
    },
    'data': {
        'csv_path': os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'results', 'results.csv')),

        'question_flow_yaml': os.path.abspath(os.path.join(os.getcwd(), 'src', 'config', 'question_flow.yaml')),

        'out_info_path': os.path.abspath(os.path.join(os.getcwd(), '..', '..', '..', 'Downloads')),

        'headers': ["Image_Id","Country","Region","People","Num_People","Role","Gender","Category","Age_Categories",
                    "Travel_Group","Activity_Type","Activity_Done","Context_Type","Resource_Types","Flora_Types",
                    "Fauna_Types","Landscape_Types","Tourist_Resource_Types","Heritage_Types","Cultural_Elements",
                    "Gastronomy_Types","Leisure_Activities","Leisure_Types","Sports_Types","Shopping_Facilities",
                    "Accommodation_Types","Infrastructure_Types"],
    },
}
