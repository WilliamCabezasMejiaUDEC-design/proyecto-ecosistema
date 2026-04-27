import streamlit as st
from src.knowledge_engine import construir_prompt_maestro
from google import genai

def render_ecobot():
    st.markdown("## 🤖 Ecobot 4R+T — Inteligencia Operativa")
    
    # Inicializar historial
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # UI del Chat
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input del usuario
    if prompt := st.chat_input("Consulta técnica sobre 4R+T..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # Construcción del contexto (RAG)
                prompt_maestro = construir_prompt_maestro(prompt)
                
                # Acceso a Secrets (Forma segura)
                client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt_maestro
                )
                
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error de sistema: No pude conectar con el Ecosistema. ({e})")