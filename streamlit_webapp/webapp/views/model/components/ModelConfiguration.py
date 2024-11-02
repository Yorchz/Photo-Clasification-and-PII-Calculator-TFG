import streamlit as st


class ModelConfiguration:

    def configuration(self):
        with st.expander("Configuracion del modelo", expanded=False):
            model = self._select_box()
            st.session_state.current_model = model

            model_version = self._model_version_select_box(model)
            st.session_state.current_model_version = model_version

            percentage = self._slider()
            st.session_state.percentage = percentage

    @staticmethod
    def _select_box():
        # Se define el selectbox para elegir el modelo principal
        model = st.selectbox(
            "Seleccione el modelo de resumen:",
            ["mistral", "gpt"],
            index=0
        )
        return model

    @staticmethod
    def _model_version_select_box(model):
        # Se define el selectbox para elegir la versión del modelo basado en el modelo principal seleccionado
        if model == "mistral":
            model_version = st.selectbox(
                "Seleccione la versión del modelo:",
                ["7B", "8x7B"],
                index=0
            )
        elif model == "gpt":
            model_version = st.selectbox(
                "Seleccione la versión del modelo:",
                ["3.5-turbo", "4-o"],
                index=0
            )
        return model_version

    @staticmethod
    def _slider():
        # Se define el slider para elegir el porcentaje de resumen
        percentage = st.slider(
            "Porcentaje de resumen:",
            min_value=0.1,
            max_value=1.0,
            value=0.5,
            step=0.1
        )
        return percentage