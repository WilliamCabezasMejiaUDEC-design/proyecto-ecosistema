import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def render_financiero(van, tir, roi, cb, insight_texto):
    """
    Renderiza el módulo financiero con estilo Electric Gold.
    Evita escrituras en disco para máxima eficiencia en la nube.
    """
    st.title("📊 Centro de Control Estratégico 4R+T")
    
    # 1. KPIs Financieros (Disposición limpia)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("VAN", f"${van/1e6:.1f}M")
    col2.metric("TIR", f"{tir}%")
    col3.metric("ROI", f"{roi}%")
    col4.metric("C/B", f"1:{cb}")
    
    st.markdown("---")
    
    # 2. Gráfico de Tendencia (Renderizado en memoria)
    st.subheader("Análisis de Flujo Acumulado")
    
    # Datos simulados para el gráfico (Adaptar según tu lógica de negocio)
    anios = [0, 1, 2, 3, 4]
    flujos_acum = [-2.8, -1.5, 0.5, 2.2, 4.0] # Datos ejemplo
    
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor('#080808')
    ax.set_facecolor('#080808')
    
    ax.plot(anios, flujos_acum, color='#FFD700', linewidth=3, marker='o')
    ax.fill_between(anios, flujos_acum, alpha=0.1, color='#FFD700')
    ax.axhline(0, color='white', linewidth=1, linestyle='--')
    
    # Estilizado de ejes
    ax.tick_params(colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Renderizado directo sin guardar en disco
    st.pyplot(fig)
    
    # 3. Insights
    st.success(f"**Análisis:** {insight_texto}")