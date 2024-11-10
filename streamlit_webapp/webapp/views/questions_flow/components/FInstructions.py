
import streamlit as st


class FInstructions:

    @staticmethod
    def instructions():
        st.markdown("""
                <div class='instructions-container'>
                    <h1 class='instruction-title'>Estás usando un resumidor para datos del Boletin Oficial de Canarias. Está orientado a realizar resumenes sobre este, así que aquí tienes unos consejos para obtener el máximo rendimiento:</h1>
                    <ul class='instruction-list'>
                        <li>Sé lo más específico posible al realizar una petición, usando un lenguaje neutro y claro.</li>
                        <li>El porcentaje hace referencia a la longitud del resumen de salida.</li>
                        <li>El máximo de tokens son el límite de palabras que el modelo utiliza para generar una respuesta. Es útil para controlar la longitud y la complejidad de las respuestas, asegurando que sean concisas y relevantes.</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)