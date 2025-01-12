
import streamlit as st


class FInstructions:

    @staticmethod
    def instructions_upload():
        st.markdown("""
            <div class='instructions-container'>
                <h5 style="font-size: 18px;">Estás en la sección de Gestión del Flujo de Preguntas. Aquí defines cómo debe comportarse el modelo ante diferentes combinaciones de preguntas y respuestas.</h5>
                <ul style="list-style-type: disc;">
                    <li style="font-size: 14px;">Esta sección permite establecer reglas que determinan qué preguntas deben omitirse en función de las respuestas dadas previamente. Por ejemplo, si a una pregunta sobre el número de personas se responde con "0", las preguntas relacionadas con personas en la imagen no se realizarán.</li>
                    <li style="font-size: 14px;">El flujo debe estar contenido en un archivo <b>.txt</b> siguiendo un formato estructurado. A continuación, un ejemplo genérico del formato de flujo de preguntas:</li>
                    <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; font-size: 12px;">
                    </pre>
                    <li style="font-size: 14px;">Cada línea sigue la estructura: <code>&lt;tipo&gt;=valor_respuesta: &lt;tipo_siguiente1&gt; &lt;tipo_siguiente2&gt; | es_global=valor</code>, donde:
                        <ul style="list-style-type: circle; margin-left: 20px;">
                            <li style="font-size: 14px;"><b>&lt;tipo&gt;</b>: Representa el término inicial (puede ser <code>context</code>, <code>activity</code>, <code>subject</code>, etc.).</li>
                            <li style="font-size: 14px;"><b>valor_respuesta</b>: La respuesta que activa el salto de preguntas.</li>
                            <li style="font-size: 14px;"><b>&lt;tipo_siguiente&gt;</b>: Representa los términos o preguntas que deben omitirse.</li>
                            <li style="font-size: 14px;"><b>es_global</b>: Indica si la regla afecta globalmente (<code>true</code>) o solo al contexto local (<code>false</code>).</li>
                        </ul>
                    </li>
                    <li style="font-size: 14px;">Asegúrate de revisar y validar el archivo antes de subirlo para evitar errores en el comportamiento del modelo.</li>
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
