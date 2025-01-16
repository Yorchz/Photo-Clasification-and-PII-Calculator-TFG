
import streamlit as st


class QInstructions:

    @staticmethod
    def instructions_upload():
        st.markdown("""
            <div class='instructions-container'>
                <h5 style="font-size: 18px;">Estás en la sección de Carga o Actualización de Preguntas. Aquí puedes gestionar los archivos de preguntas que se utilizarán en el modelo, permitiendo mantener las preguntas del sistema actualizadas.</h5>
                <ul style="list-style-type: disc;">
                    <li style="font-size: 14px;">Puedes subir o actualizar tantos archivos de preguntas como necesites, siempre que sigan el formato correcto.</li>
                    <li style="font-size: 14px;">Antes de realizar la carga o actualización, selecciona la base de datos de preguntas correspondiente. Las opciones disponibles son:
                        <ul style="list-style-type: circle; margin-left: 20px;">
                            <li style="font-size: 14px;">Categorización de actividades</li>
                            <li style="font-size: 14px;">Categorización de contextos</li>
                            <li style="font-size: 14px;">Categorización de sujetos</li>
                        </ul>
                    </li>
                    <li style="font-size: 14px;">El archivo debe ser un <b>.txt</b> donde cada línea tenga el siguiente formato: <code>questionX - pregunta</code>, donde <code>X</code> corresponde al número incremental de la pregunta. Por ejemplo:
                        <br><code>question1 - ¿Cuál es el nombre del hotel?</code><br>
                        <code>question2 - ¿Cuántas estrellas tiene el hotel?</code>
                    </li>
                    <li style="font-size: 14px;">Evita realizar preguntas demasiado generales para garantizar que el modelo entregue resultados precisos y relevantes.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    @staticmethod
    def instructions_download():
        st.markdown("""
            <div class='instructions-container'>
                <h5 style="font-size: 18px;">Descarga de Preguntas</h5>
                <ul style="list-style-type: disc;">
                    <li style="font-size: 14px;">Antes de realizar la descarga, selecciona la base de datos de preguntas que deseas exportar. Las opciones disponibles son:
                        <ul style="list-style-type: circle; margin-left: 20px;">
                            <li style="font-size: 14px;">Categorización de actividades</li>
                            <li style="font-size: 14px;">Categorización de contextos</li>
                            <li style="font-size: 14px;">Categorización de sujetos</li>
                        </ul>
                    </li>
                    <li style="font-size: 14px;">Una vez seleccionada, haz clic en el botón de descarga. Se generará un archivo con las preguntas correspondientes, que se guardará en tu carpeta de descargas.</li>
                    <li style="font-size: 14px;">El archivo llevará un nombre que incluirá la fecha y hora actuales, facilitando su identificación.</li>
                    <li style="font-size: 14px;">Puedes usar este archivo para consultar, editar y volver a cargar las preguntas si es necesario.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

