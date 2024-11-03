from views.questions_flow.components.SubtitleUpload import SubtitleUpload
from views.questions_flow.components.TitleUpload import TitleUpload


class QFlowUploader:

    def run(self):
        TitleUpload.title()
        SubtitleUpload.subtitle()