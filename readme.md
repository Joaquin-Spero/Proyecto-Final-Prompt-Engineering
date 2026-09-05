# 🚀 StreamBoost AI

Aplicación web interactiva desarrollada con **Streamlit** y conectada a la API de **OpenAI** (GPT-3.5-Turbo). Su objetivo principal es resolver la falta de inspiración de los creadores de contenido (streamers de Twitch/Kick) al momento de promocionar sus transmisiones en vivo.

## 📌 Funcionalidad Principal
A partir de un prompt con salida dirigida estandarizada en formato **JSON**, la IA procesa el juego y el ambiente del stream para generar automáticamente:
- Un título llamativo (máximo 60 caracteres).
- Un copy persuasivo para publicar en redes sociales (Twitter, Instagram).
- Una lista de etiquetas (tags) optimizadas.

## 📂 Estructura del Proyecto

```text
proyecto-final-ia/
├── app.py              # Código fuente principal de la aplicación Streamlit
├── requirements.txt    # Dependencias necesarias para ejecutar el proyecto
├── .env.example        # Plantilla de variables de entorno
├── .gitignore          # Archivos excluidos del control de versiones
└── README.md           # Documentación del proyecto
```

## 🛠️ Requisitos de Instalación
1. Clonar este repositorio.
2. Crear un entorno virtual (opcional pero recomendado).
3. Instalar las dependencias ejecutando:
   `pip install -r requirements.txt`
4. Renombrar el archivo `.env.example` a `.env` y colocar una API Key válida de OpenAI.

## 🚀 Ejecución
Para levantar el proyecto en local, ejecutar el siguiente comando en la terminal:
`python -m streamlit run app.py`