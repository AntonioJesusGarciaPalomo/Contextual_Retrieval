# Webinar CRAG

Este proyecto consiste en la creación de un Contextual RAG:
1. Creación del contexto de cada chunk del PDF.
2. Guardado en Chroma y BM25.
3. Recuperación con ReRanker.

![crag](imgs/crag.webp)

## Estructura de carpetas

```plaintext
📦 webinar_crag
├── 📁 app                         # Código de la aplicacion
│   ├── 📁 chatbot    
│   │   ├── 📄 __init__.py         # Convierte un directorio en un paquete
│   │   ├── 📄 chatbot.py          # Clase del agente RAG 
│   │   └── 📄 prompt.py           # Prompts del sistema
│   └── 📁 tools                   # Herramientas 
│       ├── 📄 __init__.py         # Convierte un directorio en un paquete
│       ├── 📄 retrieve.py         # Codigo para recuperacion desde Chroma
│       └── 📄 tools.py            # Herramientas (logger)
│
├── 📁 data                        # Carpeta con los pdfs, se guarda aqui chroma y BM25
│
├── 📁 imgs                        # Carpeta con las imagenes usadas
│
├── 📁 notebooks                   # Carpeta de notebooks de prueba
│   └── 📄 CRAG.ipynb              # Jupyter notebook con todo el proceso
│
├── 📄 .gitignore                  # Archivos y carpetas a ignorar en Git
├── 📄 README.md                   # Documentación principal del proyecto
└── 📄 requirements.txt            # Dependencias y configuración 
```


## Dependencias

1. **Activación del entorno virtual**

    Activar el entorno virtual usado el siguiente comando:

    ```bash
    source .venv/bin/activate
    ```

    También puede usarse conda y crear un entorno virtual con:
     ```bash
    conda create -n sql python=3.12
    ```

2. **Sincronizar dependencias con pip**:

    ```bash
    pip install -r requirements.txt
    ```

    Este comando instala las dependencias en el entorno virtual definidas en el archivo `requirements.txt`. 

## Variables de entorno

Este proyecto necesita obtener una API KEY de OpenAI [aqui](https://platform.openai.com/api-keys).

`OPENAI_API_KEY = 'sk-WrrN..................'`




## Proceso de instalación y uso

1. Instalar dependencias con el archivo `requirements.txt` usando el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```


2. Levantar el front de chainlit de la carpeta app con el siguiente comando:
    ```bash
    chainlit run front.py -w --port 8001
    ```

