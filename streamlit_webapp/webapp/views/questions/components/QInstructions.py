
import streamlit as st


class QInstructions:

    @staticmethod
    def instructions_upload():
        st.markdown("""
            <div class='instructions-container'>
                <h5 style="font-size: 18px;">Estás en la sección de Carga o Actualización de Preguntas. Aquí puedes gestionar los archivos de preguntas que se utilizarán en el modelo. Permitiendo mantener las pregutnas del sistema actualizadas </h5>
                <ul style="list-style-type: disc;">
                    <li style="font-size: 14px;">Puedes subir o actualizar tantos archivos de preguntas como necesites, siempre que sigan el formato correcto.</li>
                    <li style="font-size: 14px;">El archivo debe ser un <b>.txt</b> donde cada línea tenga el siguiente formato: <code>questionX - pregunta</code>, donde <code>X</code> corresponde al número incremental de la pregunta, por ejemplo: 
                        <br><code>question1 - ¿Cuál es el nombre del hotel?</code><br>
                        <code>question2 - ¿Cuántas estrellas tiene el hotel?</code></li>
                    <li style="font-size: 14px;">Evita realizar preguntas demasiado generales para garantizar que el modelo entregue resultados precisos y relevantes.</li>
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
