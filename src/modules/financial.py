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
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def render_financiero(van, tir, roi, cb, insight_texto):
    st.title("📊 Centro de Control Estratégico 4R+T")
    
    # KPIs Financieros de alto nivel
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("VAN", f"${van/1e6:.1f}M")
    c2.metric("TIR", f"{tir}%")
    c3.metric("ROI", f"{roi}%")
    c4.metric("C/B", f"1:{cb}")
    
    st.markdown("---")
    
    # Pestañas de Evidencia Técnica
    tab1, tab2 = st.tabs(["Tablero de Control (KPIs/KRIs)", "Evidencia IA Engine"])
    
    with tab1:
        st.subheader("Matriz de Monitoreo de Riesgos y Desempeño")
        # Datos extraídos del informe técnico 
        data = {
            "Categoría": ["Financiera", "Financiera", "Operaciones", "Operaciones", "Cumplimiento"],
            "Indicador": ["Margen/Tonelada", "ROI Aprovechamiento", "OTIF (Recolección)", "MAPE (Error Regresión)", "Multas"],
            "Tipo": ["KPI", "KPI", "KPI", "KPI Técnico", "KRI"],
            "Umbral": ["Maximizar", "> 15%", "98%", "< 5%", "0 Tolerancia"]
        }
        df_kri = pd.DataFrame(data)
        st.dataframe(df_kri, use_container_width=True)
        st.caption("Estructura de gobernanza basada en el Tablero de Control 4R+T.")

    with tab2:
        st.subheader("Evidencia del Motor de IA")
        # Gráfica de MAPE (Regresión) y Matriz (Clasificación)
        col_1, col_2 = st.columns(2)
        
        with col_1:
            st.write("### Modelo de Regresión (MAPE)")
            st.info(f"MAPE Actual: 3.8% (Objetivo < 5%) [cite: 68]")
            # Simulación de gráfica
            fig, ax = plt.subplots(figsize=(5,3))
            ax.plot([0,1,2,3,4], [10, 8, 5, 4, 3.8], marker='o', color='#FFD700')
            ax.set_title("Reducción de Error de Predicción")
            st.pyplot(fig)
            
        with col_2:
            st.write("### Clasificación de Residuos")
            st.write("**Matriz de Confusión**")
            st.text("TP: 450 | FP: 12\nFN: 08  | TN: 380")
            st.success("Precisión Validada (F1-Score): 0.91 [cite: 70]")

    st.warning(f"**Insight Estratégico:** {insight_texto}")