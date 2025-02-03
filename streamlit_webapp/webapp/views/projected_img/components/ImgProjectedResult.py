import streamlit as st
import pandas as pd
class ImgProjectedResult:

    @staticmethod
    def img_projected_result(result):
        st.table(result)