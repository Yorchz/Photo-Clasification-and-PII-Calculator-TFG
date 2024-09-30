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
        'csv_path': os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'results', 'results2.csv')),
        'image_dir': os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'modeling', 'images')),
        'actv_questions': os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'modeling', 'questions_txt',
                                                       'Represented_activities_categorization.txt')),
        'subj_questions': os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'modeling', 'questions_txt',
                                                       'Subjet_categorization.txt')),
        'cont_questions': os.path.abspath(os.path.join(os.getcwd(), '..', '..', 'data', 'modeling', 'questions_txt',
                                                       'Context_categorization.txt')),

        'headers': ['Image', 'Number_of_People', 'Relevance', 'Gender', 'Location', 'Age', 'Group_Type', 'Activity_Type', 'Activity'],
    },
    'model': {
        'model_name': 'blip2_t5',
        'model_type': 'pretrain_flant5xxl',
    }
}
