# VQA Imagen Proyectada

![Proyecto](https://img.shields.io/badge/VQA-Turismo-blueviolet) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![Status](https://img.shields.io/badge/Estado-En%20desarrollo-orange)

## Descripción del Proyecto

Este proyecto explora la aplicación de modelos de Visual Question Answering (VQA) en el ámbito del turismo para analizar la imagen proyectada de los destinos a través de fotografías. Se utilizan modelos avanzados de inteligencia artificial para extraer información de imágenes y calcular el Índice de Imagen Proyectada (PII), permitiendo una evaluación cuantitativa de la percepción turística. Este análisis proporciona información clave para la gestión de destinos turísticos, ayudando en la toma de decisiones estratégicas basadas en datos visuales. La herramienta desarrollada facilita el procesamiento y análisis de grandes volúmenes de imágenes, permitiendo generar reportes automatizados y proporcionando métricas cuantificables para la planificación turística.

## Autores
- **Jorge Hernández Hernández**

## Tutores
- **Jose Javier Lorenzo Navarro**
- **Patricia Picazo Peral**

## Objetivos del Proyecto
- **Analizar la imagen proyectada en fotografías turísticas mediante modelos de VQA** para identificar patrones visuales relevantes en destinos turísticos.
- **Evaluar la precisión de modelos de lenguaje-visión** en la identificación de características clave en imágenes, mejorando la fiabilidad de los análisis.
- **Desarrollar una aplicación con una interfaz intuitiva** que permita a los usuarios cargar imágenes, realizar consultas y visualizar los resultados obtenidos por los modelos de VQA.
- **Comparar distintos modelos VQA** para determinar cuál ofrece mejores resultados en la evaluación de imágenes turísticas.
- **Crear una herramienta útil para investigadores y gestores de turismo**, permitiendo el análisis de tendencias y optimización de campañas de promoción.

## Modelos Utilizados
El proyecto emplea varios modelos de Visual Question Answering para analizar y clasificar imágenes:
- **BLIP (Bootstrapping Language-Image Pretraining)**: Modelo basado en transformers que integra imagen y texto mediante aprendizaje contrastivo y generación de descripciones. Este modelo permite generar respuestas detalladas y contextualizadas basadas en el contenido visual.
- **BLIP-2**: Optimización de BLIP con un mecanismo de alineación más eficiente entre imagen y texto, lo que permite una mejor comprensión multimodal y mayor precisión en respuestas generadas.
- **PNP-VQA (Plug-and-Play Visual Question Answering)**: Modelo modular que combina visión y lenguaje sin necesidad de reentrenamiento, permitiendo una rápida integración y escalabilidad en distintos dominios.

## Metodología
Se sigue la metodología **CRISP-DM**, ampliamente utilizada en ciencia de datos, que proporciona una estructura clara para el desarrollo del proyecto:
1. **Comprensión del negocio**: Se identifican las necesidades del sector turístico y se establece cómo el análisis de imágenes puede mejorar la gestión y promoción de destinos.
2. **Comprensión de los datos**: Recopilación y exploración de imágenes turísticas provenientes de redes sociales, bancos de imágenes y fuentes institucionales.
3. **Preparación de los datos**: Se lleva a cabo la limpieza de datos, etiquetado de imágenes y estructuración de información en bases de datos no relacionales.
4. **Modelado**: Se implementan y evalúan distintos modelos de VQA para analizar la capacidad de respuesta de cada uno.
5. **Evaluación**: Se comparan métricas de rendimiento para identificar el modelo más eficiente en términos de precisión y velocidad de respuesta.
6. **Despliegue**: La herramienta se implementa como una aplicación web basada en Streamlit para facilitar su acceso y uso.

## Recursos Utilizados
### Hardware
- **GPU de alto rendimiento** para la ejecución de modelos de IA, asegurando tiempos de inferencia óptimos y capacidad para procesar grandes volúmenes de imágenes.

### Software y Librerías
- **Python 3.8+** con librerías especializadas como **PyTorch**, **Transformers (Hugging Face)** y **OpenCV** para la manipulación y análisis de imágenes.
- **MongoDB** para el almacenamiento y gestión de datos, permitiendo consultas rápidas y escalabilidad del proyecto.
- **Jupyter Notebooks** para la experimentación y validación de modelos.
- **Streamlit** para la implementación de una interfaz de usuario interactiva y accesible.

## Aplicación
Se ha desarrollado una aplicación basada en **Streamlit** que permite:
- **Gestión de preguntas e imágenes**, permitiendo la carga y almacenamiento eficiente de datos visuales.
- **Ejecución de modelos de VQA**, que procesan imágenes en tiempo real para extraer información clave.
- **Cálculo del Índice de Imagen Proyectada (PII)**, una métrica que evalúa la percepción visual del destino basándose en múltiples parámetros.
- **Visualización de resultados**, permitiendo la exploración interactiva de las respuestas generadas por los modelos.

## Resultados y Conclusiones
- Se ha demostrado la viabilidad del uso de modelos VQA para el análisis de imágenes turísticas, proporcionando información estructurada sobre la percepción de los destinos.
- **BLIP-2 mostró un rendimiento superior** en términos de precisión en la generación de respuestas, consolidándose como el modelo más robusto para la tarea.
- **PNP-VQA destacó por su flexibilidad y facilidad de integración**, permitiendo la implementación sin necesidad de reentrenamiento.
- La combinación de estos modelos ha permitido optimizar la evaluación de imágenes, generando reportes automatizados y métricas útiles para la toma de decisiones en el sector turístico.

## Trabajo Futuro
- **Optimización del rendimiento en tiempo real**, mejorando la velocidad de inferencia de los modelos para facilitar su uso en entornos con restricciones de hardware.
- **Reducción de sesgos en la interpretación de imágenes**, evaluando estrategias para mitigar posibles distorsiones en la representación de los datos.
- **Integración con modelos de generación de imágenes**, permitiendo simulaciones visuales basadas en tendencias turísticas emergentes.
- **Aplicaciones en otros sectores**, explorando su uso en educación, marketing y análisis documental.
- **Expansión de la base de datos**, incluyendo imágenes de diversas regiones y tipos de turismo para mejorar la representatividad del análisis.

## Licencia
Este proyecto se encuentra bajo la licencia **MIT**, permitiendo su uso y modificación sin restricciones significativas.

---

Si tienes alguna pregunta o sugerencia, por favor, abre un issue en el repositorio. ¡Gracias por tu interés en este proyecto!
