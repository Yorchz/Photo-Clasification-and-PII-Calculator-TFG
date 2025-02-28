# VQA Imagen Proyectada

![Proyecto](https://img.shields.io/badge/VQA-Turismo-blueviolet) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![Status](https://img.shields.io/badge/Estado-En%20desarrollo-orange) 🚀

## 🌍 Descripción del Proyecto

Este proyecto explora la aplicación de modelos de Visual Question Answering (VQA) en el ámbito del turismo para analizar la imagen proyectada de los destinos a través de fotografías 📸. Se utilizan modelos avanzados de inteligencia artificial 🤖 para extraer información de imágenes y calcular el Índice de Imagen Proyectada (PII), permitiendo una evaluación cuantitativa de la percepción turística. 

Este análisis proporciona información clave 📊 para la gestión de destinos turísticos, ayudando en la toma de decisiones estratégicas basadas en datos visuales. La herramienta desarrollada facilita el procesamiento y análisis de grandes volúmenes de imágenes, permitiendo generar reportes automatizados 📑 y proporcionando métricas cuantificables para la planificación turística. Además, este enfoque facilita la identificación de patrones emergentes en el sector turístico, lo que puede ser clave para adaptar estrategias de promoción y mejorar la experiencia del visitante.

## ✨ Autores
- **Jorge Hernández Hernández**

## 🏫 Tutores
- **Jose Javier Lorenzo Navarro**
- **Patricia Picazo Peral**

## 🎯 Objetivos del Proyecto
- 🔍 **Analizar la imagen proyectada en fotografías turísticas** mediante modelos de VQA para identificar patrones visuales relevantes en destinos turísticos.
- 📌 **Evaluar la precisión de modelos de lenguaje-visión** en la identificación de características clave en imágenes, mejorando la fiabilidad de los análisis.
- 🖥️ **Desarrollar una aplicación con una interfaz intuitiva** que permita a los usuarios cargar imágenes, realizar consultas y visualizar los resultados obtenidos por los modelos de VQA.
- 📊 **Comparar distintos modelos VQA** para determinar cuál ofrece mejores resultados en la evaluación de imágenes turísticas.
- 🌟 **Crear una herramienta útil para investigadores y gestores de turismo**, permitiendo el análisis de tendencias y optimización de campañas de promoción.

## 🔧 Recursos Utilizados
### 🖥️ Hardware
- **GPU de alto rendimiento** ⚡ para asegurar tiempos de inferencia óptimos y procesamiento eficiente.

### 📦 Software y Librerías
- **Python 3.8+** 🐍 con **PyTorch**, **Transformers (Hugging Face)** y **OpenCV** para manipulación de imágenes.
- **MongoDB** 🗄️ para almacenamiento y gestión eficiente de datos.
- **Jupyter Notebooks** 📓 para experimentación y validación de modelos.
- **Streamlit** 🖥️ para la interfaz interactiva.

## 📊 Resultados Principales
### 🏆 Evaluación de Modelos VQA
Se evaluaron varios modelos VQA para determinar su rendimiento en tareas de clasificación y análisis de imágenes turísticas:

- **BLIP-VQA** obtuvo una precisión general del **18.23%**, con una mejor identificación en sujetos humanos (30.36%) pero un desempeño muy bajo en análisis de contexto (0.42%).
- **BLIP2-T5** demostró una precisión significativamente mayor (**87.9% general**), con un rendimiento excepcional en detección de sujetos y actividades.
- **PNP-VQA** mostró un equilibrio entre precisión y versatilidad, logrando un accuracy general del **75.64%** y destacando en clasificación de contexto y actividades.

### 📈 Análisis de Errores y Desafíos
- ❌ **Errores en clasificación de contexto:** Los modelos presentan dificultades en la identificación de elementos ambientales, afectando la precisión en análisis globales.
- ⚠️ **Limitaciones en deportes y actividades acuáticas:** Se observó una mayor tasa de fallos en deportes de montaña y agua, probablemente debido a la falta de datos representativos en el entrenamiento.
- 🔄 **Optimización mediante ajuste fino:** Se recomienda incorporar técnicas de reentrenamiento y ajuste en dominios específicos para mejorar la capacidad de reconocimiento de actividades y objetos específicos en el contexto turístico.

## 🔮 Trabajo Futuro
- ⚡ **Optimización del rendimiento en tiempo real** para mejorar la velocidad de inferencia.
- 🔍 **Reducción de sesgos en la interpretación de imágenes**, mitigando posibles distorsiones.
- 🎨 **Integración con modelos de generación de imágenes** para simulaciones visuales.
- 📚 **Expansión de la base de datos**, incluyendo más imágenes y tipos de turismo.
- 🤖 **Implementación de aprendizaje por refuerzo** para mejorar la adaptabilidad de los modelos a distintos entornos y condiciones.

## 📜 Licencia
Este proyecto se encuentra bajo la licencia **MIT**, permitiendo su uso y modificación sin restricciones significativas.

---

💡 **¿Tienes alguna idea o sugerencia?** ¡Abre un issue en el repositorio! 🚀

📢 **¡Gracias por tu interés en este proyecto!** 🎉
