import streamlit as st

from src.services.api.ImageDownloaderService import ImageDownloaderService
from src.services.api.ImageUploaderService import ImageUploaderService
from views.questions_flow.components.FResult import FResult
from views.images.components.PResult import PResult


class ImageAssistant:

    def __init__(self, event):
        self.images = event['images']
        self.image_uploader_service = ImageUploaderService()
        self.image_download_service = ImageDownloaderService()


    def event_upload_images(self):
        if st.button("Actualizar Base de Datos de Preguntas"):
            images_status = self._check_inputs_status()
            if not images_status:
                response = self.image_uploader_service.upload(self.images)
                PResult.upload_result(response)
            else:
                st.error("Debe seleccionar la categoria del archivo y el nuevo archivo que quiere usar para su actualización.")


    def event_download_images(self):
        if st.button("Descargar Imagenes de la Base de Datos"):
            response = self.image_download_service.download()
            PResult.download_result(response)



    def _check_inputs_status(self):
        file_status = self.images is None
        print(f"Fichero: {file_status}")
        return file_status
