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
        'image_dir': os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'modeling', 'images')),

        'question_flow_yaml': os.path.abspath(os.path.join(os.getcwd(), 'src', 'config', 'question_flow.yaml')),

        'out_flow_path': os.path.abspath(os.path.join(os.getcwd(), '..', '..', '..', 'Downloads')),

        'question_flow_txt': os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'modeling', 'question_flow',
                                                                       'Question_flow.txt')),



        'headers': ["Image_Id","Num_People","Role","Gender","Category","Age_Categories","Travel_Group","Activity_Type",
                    "Activity_Done","Natural_Resources","Resource_Types","Flora_Types","Fauna_Types","Landscape_Types",
                    "Tourist_Resources","Tourist_Resource_Types","Heritage_Types","Cultural_Elements","Gastronomy_Types",
                    "Recreational_Products","Leisure_Activities","Leisure_Types","Sports_Types","Shopping_Facilities",
                    "Accommodation","Accommodation_Types","Infrastructures","Infrastructure_Types"],
    },
    'model': {
        'model_name': 'blip2_t5',
        'model_type': 'pretrain_flant5xxl',
    }
}
