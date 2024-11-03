from views.questions.components.Subtitle import Subtitle
from views.questions.components.Title import Title
from views.questions.components.QuestionConfiguration import QuestionConfiguration
from views.questions.components.QuestionUploader import QuestionUploader


class QuestionsUploader:

    def run(self):
        Title.title()
        Subtitle.subtitle()

        question_conf = QuestionConfiguration()
        question_conf.configuration()

        QuestionUploader.file_upload()

