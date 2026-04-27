import streamlit as st

def render_identity():
    """
    Renderiza la Identidad Estratégica del Ecosistema 4R+T.
    Diseño limpio, enfocado en legibilidad y autoridad.
    """
    st.markdown("# 🏢 Identidad Estratégica: 4R+T")
    st.markdown("---")
    
    # --- MEGA: El ancla estratégica ---
    st.markdown("### 🎯 MEGA (Meta Estratégica Grande y Ambiciosa)")
    st.success(
        "Para el año 2028, transformar 10,000 toneladas de residuos en un fondo "
        "de inversión social que garantiza 5,000 becas de educación profesional "
        "técnica para la red de 'Guardianes del Primer Paso'."
    )
    
    # --- Misión y Visión ---
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Misión")
        st.write(
            "Plataforma de inteligencia circular que sincroniza el cumplimiento "
            "industrial con la dignificación humana, convirtiendo el impacto "
            "ambiental en recursos tangibles para la educación técnica y profesional."
        )
        
    with c2:
        st.subheader("Visión 2030")
        st.write(
            "Ser el ecosistema líder y referente global en gestión inteligente de "
            "residuos, integrando saberes tradicionales con innovación tecnológica "
            "de vanguardia y trazabilidad total."
        )
    
    # --- Valores Clave ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Valores Operativos")
    
    v1, v2, v3 = st.columns(3)
    v1.metric("Transformación", "Valor: Alto")
    v2.metric("Transparencia", "Valor: Total")
    v3.metric("Trazabilidad", "Valor: Rigurosa")
    
    st.markdown("""
    * **Circularidad:** Cero desperdicio, valor máximo.
    * **Dignidad:** El reciclador es el centro del sistema.
    * **Eficacia:** Datos para la toma de decisiones.
    """)

def render_identity():
    st.markdown("# 🏢 Identidad Estratégica: 4R+T")
    st.markdown("---")
    
    # MEGA, Misión y Visión
    st.info("### 🎯 MEGA (Meta Estratégica Grande y Ambiciosa)")
    st.write("Para el año 2028, transformar 10,000 toneladas de residuos en un fondo de inversión social que garantiza 5,000 becas de educación profesional técnica para la red de 'Guardianes del Primer Paso'. [cite: 238]")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Misión")
        st.write("Plataforma de inteligencia circular que sincroniza el cumplimiento industrial con la dignificación humana, convirtiendo el impacto ambiental en recursos tangibles para la educación técnica y profesional de recicladores. [cite: 239]")
    with col2:
        st.subheader("Visión 2030")
        st.write("Ser el ecosistema líder y referente global en gestión inteligente de residuos, integrando la sabiduría tradicional del reciclaje con innovación tecnológica de vanguardia y trazabilidad total. [cite: 240]")
    
    # Valores
    st.subheader("Valores y Principios")
    c1, c2, c3 = st.columns(3)
    c1.metric("Transformación", "Pasión por convertir residuos. [cite: 242]")
    c2.metric("Transparencia", "Trazabilidad verificable 100%. [cite: 243]")
    c3.metric("Inclusión", "Dignificación del reciclador. [cite: 244]")