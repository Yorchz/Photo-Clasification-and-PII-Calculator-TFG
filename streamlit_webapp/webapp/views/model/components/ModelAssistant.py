import streamlit as st
from src.services.api.ModelService import ModelService
from views.model.components.ModelResult import ModelResult


class ModelAssistant:

    def __init__(self, event):
        self.selected_model = event['model_name']
        self.model_type = event['model_type']
        self.model_controller = ModelService()


    def event_generate_data(self):

        col1, col2, col3 = st.columns([1, 2.2, 1])
        with col1:
            if st.button("Generar datos"):
                st.session_state.stop_requested = False
                model_type_status, model_status = self._check_inputs_status()
                if not (model_type_status and model_status):
                    response = self.model_controller.run(self.selected_model,
                        self.model_type,
                        stop_flag=lambda: st.session_state.get("stop_requested", False))
                    ModelResult.model_result(response)
                else:
                    st.error("Debe seleccionar el modelo que va a utilizar previamente.")
        with col3:
            if st.button("Detener ejecucuión"):
                st.session_state.stop_requested = True
                st.write("Se ha solicitado detener el modelo.")

    def _check_inputs_status(self):
        selection_status = self.selected_model is None
        file_status = self.model_type is None
        return selection_status, file_status
