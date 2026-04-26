import streamlit as st

def render_portfolio():
    st.markdown("## 📦 Nuestro Portafolio (IA + Circularidad)")
    items = [
        {"nombre": "Auditoría IA", "desc": "Diagnóstico de residuos con IA.", "precio": "$500k"},
        {"nombre": "Ecobot Pro", "desc": "Chatbot asistente especializado.", "precio": "$200k"},
        {"nombre": "Clasificador ML", "desc": "Modelo para separar desechos.", "precio": "$1M"},
        {"nombre": "Reporte PGIRS", "desc": "Automatización de reportes.", "precio": "$300k"},
        {"nombre": "Consultoría", "desc": "Estrategia de economía circular.", "precio": "$400k"}
    ]
    for i, item in enumerate(items):
        with st.container(border=True):
            st.subheader(f"{i+1}. {item['nombre']}")
            st.write(f"**Descripción:** {item['desc']}")
            st.write(f"**Precio:** {item['precio']}")