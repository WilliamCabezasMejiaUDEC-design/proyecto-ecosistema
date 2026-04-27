import streamlit as st

def render_portfolio():
    """
    Renderiza el portafolio con diseño tipo Grid (2 columnas).
    La estructura 'Grid' es estándar en portafolios de alto impacto.
    """
    st.markdown("# 📦 Portafolio de Soluciones 4R+T")
    st.markdown("---")
    
    # Definición de productos (Escalable: puedes agregar elementos aquí)
    items = [
        {"nombre": "Auditoría IA", "desc": "Diagnóstico de residuos con IA.", "precio": "500k"},
        {"nombre": "Ecobot Pro", "desc": "Chatbot asistente especializado.", "precio": "200k"},
        {"nombre": "Clasificador ML", "desc": "Modelo para separar desechos.", "precio": "1M"},
        {"nombre": "Reporte PGIRS", "desc": "Automatización de reportes.", "precio": "300k"},
        {"nombre": "Consultoría", "desc": "Estrategia de economía circular.", "precio": "400k"}
    ]
    
    # Creación de Grid de 2 columnas (Balance visual)
    col1, col2 = st.columns(2)
    
    for i, item in enumerate(items):
        # Alternar entre columnas para mantener el balance
        target_col = col1 if i % 2 == 0 else col2
        
        with target_col:
            with st.container(border=True):
                st.markdown(f"### {item['nombre']}")
                st.write(f"{item['desc']}")
                # Usamos metric para destacar el precio de forma profesional
                st.metric(label="Inversión desde", value=item['precio'])

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
