from views.questions_flow.components.SubtitleDownload import SubtitleDownload
from views.questions_flow.components.TitleDownload import TitleDownload
from views.questions_flow.components.FInstructions import FInstructions
from views.questions_flow.components.QFlowAssistant import QFlowAssistant
from views.questions_flow.components.FSession import FSession


class QFlowDownloader:

    @staticmethod
    def _initialize_session():
        FSession.session()

    @staticmethod
    def _generate_event():
        return {
            'file': None
        }

    def run(self):
        TitleDownload.title()
        SubtitleDownload.subtitle()

        FInstructions.instructions_download()

        question_flow_assistant = QFlowAssistant(self._generate_event())
        question_flow_assistant.event_download_questions_flow()

