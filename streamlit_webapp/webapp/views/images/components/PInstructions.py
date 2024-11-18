
import streamlit as st


class PInstructions:

    @staticmethod
    def instructions_upload():
        st.markdown("""
            <div class='instructions-container'>
                <h5 style="font-size: 18px;">Estás usando un resumidor para datos del Boletin Oficial de Canarias. Está orientado a realizar resumenes sobre este, así que aquí tienes unos consejos para obtener el máximo rendimiento:</h5>
                <ul style="list-style-type: disc;">
                    <li style="font-size: 14px;">Sé lo más específico posible al realizar una petición, usando un lenguaje neutro y claro.</li>
                    <li style="font-size: 14px;">El porcentaje hace referencia a la longitud del resumen de salida.</li>
                    <li style="font-size: 14px;">El máximo de tokens son el límite de palabras que el modelo utiliza para generar una respuesta. Es útil para controlar la longitud y la complejidad de las respuestas, asegurando que sean concisas y relevantes.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def instructions_download():
        st.markdown("""
            <div class='instructions-container'>
                <h5 style="font-size: 18px;">Estás usando un resumidor para datos del Boletin Oficial de Canarias. Está orientado a realizar resumenes sobre este, así que aquí tienes unos consejos para obtener el máximo rendimiento:</h5>
                <ul style="list-style-type: disc;">
                    <li style="font-size: 14px;">Sé lo más específico posible al realizar una petición, usando un lenguaje neutro y claro.</li>
                    <li style="font-size: 14px;">El porcentaje hace referencia a la longitud del resumen de salida.</li>
                    <li style="font-size: 14px;">El máximo de tokens son el límite de palabras que el modelo utiliza para generar una respuesta. Es útil para controlar la longitud y la complejidad de las respuestas, asegurando que sean concisas y relevantes.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
