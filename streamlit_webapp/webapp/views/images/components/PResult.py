import streamlit as st


class PResult:

    @staticmethod
    def upload_result(response: bool):
        if response:
            st.write(f"Se ha actualizado correctamente labase de datos de imagenes")
        else:
            st.warning("No se pudo cargar el/los archivo dado. Verifique el archivo/s e intente nuevamente.")

    @staticmethod
    def download_result(response: list):
        if response:
            st.write(f"Se han descagado las imagenes de la base de datos")
        else:
            st.warning("No se pudo realizar la descarga. Verifique el archivo/s e intente nuevamente.")

    @staticmethod
    def delete_result(response: bool):
        if response:
            st.write(f"Se han eliminado las imagenes de la base de datos")
        else:
            st.warning("No se pudo realizar el borrado. Verifique el archivo/s e intente nuevamente.")
