import streamlit as st
import os
from google import genai

# --- CONFIGURACIÓN DE CONOCIMIENTO (IDENTIDAD 4R+T) ---
CONTEXTO_MAESTRO = """
Eres el Consultor Experto de 4R+T, la plataforma de inteligencia circular. 
Tu misión es sincronizar el cumplimiento industrial con la dignificación humana bajo el concepto 'Electric Gold'.

Base de Conocimiento Obligatoria para Consultas:

--- CATÁLOGO DE ACTIVOS 4R+T ---
[BIENES]
1. Materia Prima Secundaria: Insumos post-consumo de alta pureza (PET, HDPE, Cartón). Valor: $2.500 COP/kg.
2. Guías de Separación 4R: Kit pedagógico de segregación en la fuente. Valor: $15.000 COP/kit.
3. Puntos Ecológicos 4R: Estaciones modulares de segregación inteligente. Valor: $1.200.000 COP/set.
4. Certificaciones REP: Cumplimiento de Responsabilidad Extendida del Productor. Valor: $450.000 COP/cert.
5. Productos Upcycling: Diseño circular a partir de residuos. Valor: $80.000 COP/prom.

[SERVICIOS]
6. Logística Inversa 4R: Recolección georreferenciada con trazabilidad. Valor: $600.000 COP/mes.
7. Educación Técnica IA: Capacitación certificada en oficios circulares. Valor: $200.000 COP/pers.
8. Consultoría PGIRS: Implementación de planes de gestión de residuos. Valor: $8.000.000 COP/proy.
9. Dashboard ESG SaaS: Visualización en tiempo real de impacto (CO2, Toneladas). Valor: $300.000 COP/mes.
10. Auditoría ACV: Análisis de Ciclo de Vida (Cradle-to-Grave). Valor: $5.000.000 COP/aud.

--- REGLAS DE INTERACCIÓN ---
1. Tono: Transformador, transparente, inclusivo y técnicamente preciso.
2. Si te preguntan por precios, cita los valores de la lista anterior.
3. Si la duda es sobre 'Guardianes', enfatiza que son los protagonistas del proyecto (el 'Electric Gold').
4. Si no conoces la respuesta técnica exacta, sé honesto: "Esa consulta requiere validación de nuestra oficina técnica. Por favor, contacta a soporte".
"""

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
                # --- CONSULTA A API ---
                try:
                    # Se incluye todo el contexto maestro en cada llamada
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
                        st.warning("⚠️ Límite de tráfico alcanzado. Por favor, espera 1 minuto e intenta de nuevo.")
                    else:
                        st.error(f"Error de sistema: {e}")