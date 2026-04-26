# En src/modules/ecobot.py
def render_ecobot():
    st.title("🤖 Ecobot Pro")
    st.warning("⚠️ Módulo en fase de entrenamiento final (Under Maintenance).")
    st.image("https://img.icons8.com/color/96/000000/maintenance.png")
    st.write("El asistente especializado estará activo tras la auditoría de seguridad.")


import streamlit as st
import os
from google import genai

def render_ecobot():
    st.markdown("## 🤖 Ecobot — Inteligencia Circular")
    
    # 1. Persistencia de estado (Evita que el bot se borre)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 2. Mostrar historial
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 3. Interacción
    if prompt := st.chat_input("Consulta sobre el PGIRS o el proyecto..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=f"Responde como experto en 4R+T usando estos datos: {prompt}"
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("Error en conexión. Verifica tu llave API.")



# ... (imports previos)

def render_ecobot():
    # Contexto extraído del documento "INFORME TÉCNICO"
    CONTEXTO_MAESTRO = """Eres el consultor experto de 4R+T. 
    Tu base de conocimiento incluye las 50 FAQs del repositorio maestro.
    Responde con precisión sobre: Misión, Visión, MEGA (Meta: 10,000 toneladas), 
    y servicios técnicos (Logística Inversa, Consultoría PGIRS, Trazabilidad)."""
    
    # ... (resto de la lógica del cliente GenAI)
    # Al momento de configurar el modelo, inyecta el contexto:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"{CONTEXTO_MAESTRO}\nPregunta: {prompt}"
    )


import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def render_ecobot():
    st.markdown("## 🤖 Ecobot — Inteligencia Circular")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        st.error("Error: GEMINI_API_KEY no encontrada en .env")
        return
        
    client = genai.Client(api_key=api_key)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Consulta técnica sobre economía circular..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents=prompt
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error en IA: {e}")