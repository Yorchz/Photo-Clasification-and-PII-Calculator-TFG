import streamlit as st
from views.home.components.Explanation import Explanation
from views.home.components.ImageExp import ImageExp
from views.home.components.ModelExp import ModelExp
from views.home.components.QuestionFlowExp import QuestionsFlowExp
from views.home.components.QuestionsExp import QuestionsExp
from views.home.components.Subtitle import Subtitle
from views.home.components.Title import Title
from views.home.components.CreatorInformation import CreatorInformation


class Home:

    def __init__(self):
        self.questionExp = QuestionsExp()
        self.imageExp = ImageExp()
        self.modelExp = ModelExp()
        self.questionsFlow = QuestionsFlowExp()

    def run(self):
        Title.title()
        Subtitle.subtitle()
        Explanation.display()

        # Two rows of two columns each
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            self.questionExp.display()

        with col2:
            self.questionsFlow.display()

        with col3:
            self.modelExp.display()

        with col4:
            self.imageExp.display()

        CreatorInformation.display()
