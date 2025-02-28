
import streamlit as st


class ImgProjectedInstructions:

    @staticmethod
    def instructions():
        st.markdown("""
                    <div class='instructions-container'>
                        <h5 style="font-size: 18px;">Estas en la sección de cálculo del Índice de Imagen Proyectada (PII)</h5>
                        <ul style="list-style-type: disc;">
                            <li style="font-size: 14px;">Para calcular el PII, es necesario subir un archivo <b>.csv</b> o <b>.xlsx</b> con la clasificación de los puntos.</li>
                            <li style="font-size: 14px;">Se recomienda generar este archivo a través de las herramientas proporcionadas por la aplicación para garantizar su compatibilidad y precisión.</li>
                            <li style="font-size: 14px;">Existen dos niveles de profundidad en el cálculo del PII:
                                <ul style="list-style-type: circle; margin-left: 20px;">
                                    <li style="font-size: 14px;"><b>Nivel Básico:</b> Calcula el PII a un nivel general basado en países (Ejemplo: España, Egipto, Francia, etc.).</li>
                                    <li style="font-size: 14px;"><b>Nivel Avanzado:</b> Calcula el PII con mayor precisión a nivel regional (Ejemplo: Gran Canaria, Tenerife, Málaga, etc.).</li>
                                </ul>
                            </li>
                            <li style="font-size: 14px;">Una vez subido el archivo, selecciona el nivel de profundidad deseado y ejecuta el cálculo del PII.</li>
                            <li style="font-size: 14px;">Si los resultados no son los esperados, revisa que el archivo tenga el formato correcto y que los datos hayan sido procesados correctamente por las herramientas de la aplicación.</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)

