# 🌍 VQA para Turismo - Análisis y Aplicación de Modelos Visual Question Answering

![Proyecto](https://img.shields.io/badge/VQA-Turismo-blueviolet) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![Status](https://img.shields.io/badge/Estado-En%20desarrollo-orange)

🚀 **Este repositorio contiene el código fuente de un sistema basado en modelos de Visual Question Answering (VQA) aplicado al análisis de imágenes turísticas.**  
El objetivo principal del proyecto es evaluar la compatibilidad y desempeño de modelos VQA en el sector del turismo, explorando su capacidad para interpretar imágenes y generar respuestas en lenguaje natural.  

Esta aplicación permite gestionar imágenes turísticas, formular preguntas estructuradas y calcular el **Índice de Imagen Proyectada (PII)**, proporcionando herramientas analíticas para la gestión y promoción de destinos turísticos.  

---

## 🖥️ **Características Principales**
✅ **Evaluación exhaustiva de modelos VQA** aplicados a imágenes del sector turístico.  
✅ **Automatización del cálculo del PII**, cuantificando la imagen proyectada de los destinos turísticos.  
✅ **Aplicación interactiva basada en Streamlit** para facilitar la experimentación con los modelos.  
✅ **Comparación y análisis detallado de modelos VQA**, identificando sus fortalezas y debilidades en distintos escenarios.  
✅ **Gestión eficiente de imágenes y preguntas** con almacenamiento en bases de datos en la nube.  

---

## 📌 **Estructura del Proyecto**
```
streamlit_webapp/
│── .streamlit/             # Configuración de Streamlit
│── assets/                 # Recursos gráficos y estáticos
│── webapp/                 # Código principal de la aplicación
│   ├── static_components/   # Componentes visuales de la UI
│   ├── views/               # Diferentes vistas de la aplicación
│   │   ├── home/            # Pantalla de inicio
│   │   ├── images/          # Gestión de imágenes
│   │   ├── model/           # Ejecución de modelos VQA
│   │   ├── projected_img/   # Cálculo del PII
│   │   ├── questions/       # Gestión de preguntas
│   │   ├── questions_flow/  # Gestión del flujo de preguntas
│   ├── main.py              # Entrada principal de la aplicación
│── style.css                # Estilos personalizados
```

---

## 🚀 **Cómo Ejecutar el Proyecto**

### 🔧 **Requisitos Previos**
- **Python 3.8+**  
- **pip** y virtualenv (opcional para entornos aislados)  

### 📦 **Instalación**
```bash
git clone https://github.com/tu_usuario/vqa-turismo.git
cd vqa-turismo
pip install -r requirements.txt
```

### ▶️ **Ejecutar la Aplicación**
```bash
streamlit run webapp/main.py
```
Accede a la aplicación en tu navegador en `http://localhost:8501/`

---

## 📊 **Modelos Utilizados**
| Modelo VQA           | Accuracy General | Accuracy en Sujetos | Accuracy en Actividades | Accuracy en Contexto | Tiempo de Ejecución |
|----------------------|----------------|------------------|--------------------|----------------|-----------------|
| VQAv2               | 18.23%         | 30.36%          | 27.6%             | 0.42%          | 188.22s         |
| BLIP2-T5 (5XL)      | 87.9%          | 99.7%           | 97.92%            | 79.44%         | 206.31s         |
| BLIP2-OPT 2.7B      | 57.61%         | 11.9%           | 5.21%             | 80.28%         | 1601.53s        |
| VQA Base            | 75.64%         | 67.86%          | 66.67%            | 77.22%         | 202.35s         |

📌 **Conclusión:** Se ha observado que una combinación de **BLIP2-T5 (5XL)** para sujetos y actividades, junto con **BLIP2-OPT** para contexto, mejora la precisión global en el análisis de imágenes turísticas.  

---

## 🛠️ **Funcionalidades de la Aplicación**

### 📌 **Vista de Inicio**
Pantalla principal donde se presentan las opciones disponibles.

### ❓ **Gestión de Preguntas**
- **Carga de Preguntas:** Permite subir preguntas en formato `.txt` para integrarlas en el sistema.  
- **Descarga de Preguntas:** Exporta preguntas almacenadas para su revisión y modificación.  

### 🔄 **Gestión del Flujo de Preguntas**
- **Carga de Flujo:** Define reglas sobre la relación entre preguntas y respuestas.  
- **Descarga de Flujo:** Exporta la estructura del flujo de preguntas utilizada en el modelo.  

### 🖼️ **Gestión de Imágenes**
- **Carga de Imágenes:** Permite subir imágenes para su análisis con los modelos.  
- **Descarga de Imágenes:** Exporta imágenes previamente analizadas para futuras comparaciones.  

### 🤖 **Ejecución de Modelos**
Permite seleccionar y ejecutar distintos modelos VQA sobre las imágenes cargadas para generar respuestas.

### 📈 **Índice de Imagen Proyectada (PII)**
- **Cálculo Básico:** Evaluación de la imagen proyectada a nivel de país.  
- **Cálculo Avanzado:** Análisis detallado por regiones.  

---

## 🔬 **Trabajo Futuro**
🚀 **Optimización de Modelos:** Fine-tuning en conjuntos de datos específicos del turismo.  
🔗 **Integración con Bases de Conocimiento:** Uso de *Knowledge Graphs* para enriquecer la calidad de respuestas.  
🌍 **Validación en Entornos Reales:** Implementación de la herramienta en escenarios turísticos.  
📊 **Ampliación de Métricas de Evaluación:** Incorporación de técnicas avanzadas de análisis de resultados.  

---

## 🏆 **Citación**
Si este trabajo te ha resultado útil, por favor, cítalo de la siguiente manera:

```bibtex
@article{OpenAI2023GPT4V,
  author    = {OpenAI},
  title     = {GPT-4V: Multimodal Large Language Model},
  year      = {2023},
  journal   = {OpenAI Technical Report},
  url       = {https://openai.com/research/gpt-4v}
}
```

---

## 🤝 **Colaboradores**
👤 **Tu Nombre** - [LinkedIn](https://linkedin.com/in/tu_usuario)  
📧 Contacto: [tuemail@correo.com](mailto:tuemail@correo.com)  

Si deseas contribuir, siéntete libre de hacer un *fork* del repositorio y enviar un *pull request* con tus mejoras.  

---

## 📜 **Licencia**
Este proyecto está bajo la licencia MIT. Consulta más detalles en el archivo `LICENSE`.

---

🎯 **Este repositorio busca proporcionar una base sólida para la investigación y aplicación de modelos VQA en turismo, ofreciendo herramientas para mejorar la gestión y promoción de destinos turísticos a través de la inteligencia artificial.**
