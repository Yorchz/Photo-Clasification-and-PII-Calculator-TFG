from views.model.components.Subtitle import Subtitle
from views.model.components.Title import Title
from views.model.components.ModelConfiguration import ModelConfiguration


class Model:

    def run(self):
        Title.title()
        Subtitle.subtitle()
        configuration = ModelConfiguration()
        configuration.configuration()
