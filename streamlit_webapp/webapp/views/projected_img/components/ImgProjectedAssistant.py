import streamlit as st
from src.services.api.ImgProjectedService import ImgProjectedService
from views.projected_img.components.ImgProjectedResult import ImgProjectedResult


class ImgProjectedAssistant:

    def __init__(self, event):
        self.selected_depth = event['selection']
        self.current_file = event['file']
        self.img_projected_calculator = ImgProjectedService()


    def event_generate_img_projection(self):
        if st.button("Generar indices de Imagen Proyectada"):
            selection_status, file_status = self._check_inputs_status()
            if not (selection_status and file_status):
                response = self.img_projected_calculator.projection_calculator(self.current_file, self.selected_depth)
                ImgProjectedResult.img_projected_result(response)
            else:
                st.error("Debe seleccionar la categoria del archivo y el nuevo archivo que quiere usar para su actualización.")


    def _check_inputs_status(self):
        selection_status = self.selected_depth is None
        file_status = self.current_file is None
        return selection_status, file_status