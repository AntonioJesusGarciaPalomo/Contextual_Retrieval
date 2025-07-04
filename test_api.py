import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("❌ ERROR: No se encontró la key")
else:
    print("✅ API Key cargada")

    try:
        llm = ChatOpenAI(model='gpt-4o', temperature=0)
        response = llm.invoke("Di 'Hola, la API funciona'")
        print(f"✅ Respuesta: {response.content}")
    except Exception as e:
        print(f"❌ Error al conectar: {e}")