from views.questions_flow.components.SubtitleDownload import SubtitleDownload
from views.questions_flow.components.TitleDownload import TitleDownload
from views.questions_flow.components.FInstructions import FInstructions


class QFlowDownloader:

    def run(self):
        TitleDownload.title()
        SubtitleDownload.subtitle()

        FInstructions.instructions_download()

