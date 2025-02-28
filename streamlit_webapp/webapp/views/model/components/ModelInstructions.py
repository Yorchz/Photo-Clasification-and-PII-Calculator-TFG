
import streamlit as st


class ModelInstructions:

    @staticmethod
    def instructions():
        st.markdown("""
                    <div class='instructions-container'>
                        <h5 style="font-size: 18px;">Estas en la sección de ejecución del Modelo</h5>
                        <ul style="list-style-type: disc;">
                            <li style="font-size: 14px;">Antes de ejecutar el modelo, asegúrate de que los datos necesarios han sido correctamente cargados. Esto incluye:
                                <ul style="list-style-type: circle; margin-left: 20px;">
                                    <li style="font-size: 14px;">Imágenes subidas correctamente.</li>
                                    <li style="font-size: 14px;">Preguntas en el formato adecuado.</li>
                                    <li style="font-size: 14px;">Opcionalmente, un flujo de preguntas estructurado.</li>
                                </ul>
                            </li>
                            <li style="font-size: 14px;">Una vez verificados los datos, puedes proceder a ejecutar el modelo pulsando el botón <b>"Run"</b>.</li>
                            <li style="font-size: 14px;">Durante la ejecución, si se detecta algún error, anomalía o problema con los datos cargados, puedes detener el modelo en cualquier momento.</li>
                            <li style="font-size: 14px;">Si encuentras inconsistencias en los resultados, revisa la calidad de los datos y vuelve a ejecutar el proceso tras realizar las correcciones necesarias.</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)

