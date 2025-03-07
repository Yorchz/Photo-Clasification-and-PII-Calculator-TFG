from src.config.config import CONFIG
from src.controllers.QuestionController import QuestionController

if __name__ == "__main__":
    print("Starting Question Upload Process")

    ACTV_QUESTIONS = CONFIG['data'].get('actv_questions')
    SUBJ_QUESTIONS = CONFIG['data'].get('subj_questions')
    CONT_QUESTIONS = CONFIG['data'].get('cont_questions')

    text_file_paths = [ACTV_QUESTIONS]

    question_controller = QuestionController(CONFIG['mongodb'])
    question_controller.upload_questions(text_file_paths, "actv_questions")

    print("Question Upload Process Completed")
