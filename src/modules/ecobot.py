import streamlit as st
import os
from google import genai

# --- CONFIGURACIÓN DE CONOCIMIENTO (IDENTIDAD 4R+T) ---
CONTEXTO_MAESTRO = """Eres el consultor experto de 4R+T. 
Tu base de conocimiento incluye las FAQs del proyecto.
Responde con precisión sobre: Misión, Visión, MEGA (Meta: 10,000 toneladas), 
y servicios técnicos (Logística Inversa, Consultoría PGIRS, Trazabilidad).
Si no conoces la respuesta, sé honesto y solicita contactar a soporte."""

def get_gemini_api_key():
    # Intenta obtener desde Streamlit Secrets (Nube)
    try:
        if st.secrets and "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
    # Respaldo local
    return os.environ.get("GEMINI_API_KEY")

def render_ecobot():
    st.markdown("## 🤖 Ecobot 4R+T — Inteligencia Operativa")
    
    api_key = get_gemini_api_key()
    if not api_key:
        st.error("Error: GEMINI_API_KEY no configurada. (Revisar st.secrets)")
        return

    # Inicializar cliente
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"Error al inicializar cliente IA: {e}")
        return
    
    # --- PERSISTENCIA Y CACHÉ ---
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "cache_memoria" not in st.session_state:
        st.session_state.cache_memoria = {}

    # Mostrar historial de chat
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Interacción
    if prompt := st.chat_input("Consulta técnica sobre 4R+T..."):
        prompt_key = prompt.lower().strip()
        
        # Guardar y mostrar usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # --- LÓGICA DE CACHE (Prevención 429) ---
            if prompt_key in st.session_state.cache_memoria:
                response_text = st.session_state.cache_memoria[prompt_key]
                st.markdown(f"*(Respuesta desde archivo)*\n\n{response_text}")
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            else:
                # --- CONSULTA A API CON MANEJO DE ERRORES ---
                try:
                    prompt_completo = f"{CONTEXTO_MAESTRO}\n\nPregunta del usuario: {prompt}"
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=prompt_completo
                    )
                    response_text = response.text
                    
                    # Guardar en memoria caché y persistencia
                    st.session_state.cache_memoria[prompt_key] = response_text
                    st.markdown(response_text)
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                    
                except Exception as e:
                    if "429" in str(e):
                        st.warning("⚠️ Límite de tráfico alcanzado. El sistema se recuperará en breve. Espera 1 minuto e intenta de nuevo.")
                    else:
                        st.error(f"Error de sistema: {e}")