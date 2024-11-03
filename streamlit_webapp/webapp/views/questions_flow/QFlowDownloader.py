from views.questions_flow.components.SubtitleDownload import SubtitleDownload
from views.questions_flow.components.TitleDownload import TitleDownload


class QFlowDownloader:

    def run(self):
        TitleDownload.title()
        SubtitleDownload.subtitle()
