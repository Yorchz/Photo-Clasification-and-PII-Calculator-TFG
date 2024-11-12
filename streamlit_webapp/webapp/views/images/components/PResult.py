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
            st.success("Se han actualizado las preguntas sobre la clasificación")

            st.markdown("### Preguntas actualizadas:")
            for idx, question in enumerate(response, start=1):
                st.markdown(
                    f"""
                                <div style="
                                    border: 1px solid #000; 
                                    padding: 10px; 
                                    margin: 10px 0; 
                                    border-radius: 8px;
                                    background-color: #262730;
                                    color: #FFFFFF;
                                    font-size: 16px;
                                    line-height: 1.6;">
                                    {question}
                                </div>
                                """,
                    unsafe_allow_html=True
                )

        else:
            st.warning("No se pudo cargar las preguntas. Verifique el archivo e intente nuevamente.")
