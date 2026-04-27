import sys
import os
import streamlit as st

# --- 1. CONFIGURACIÓN DE RUTA (BLINDAJE) ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# --- 2. IMPORTACIONES ---
try:
    from src.modules.identity import render_identity
    from src.modules.portfolio import render_portfolio
    from src.modules.financial import render_financiero
    from src.modules.ecobot import render_ecobot
except ImportError as e:
    st.error(f"Error de Importación: {e}")
    st.stop()

# --- 3. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="4R+T | Ecosistema Circular", layout="wide")

# --- 4. CSS INDUSTRIAL ---
st.markdown("""
<style>
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; }
    h1 { color: #FFD700 !important; font-size: 5rem !important; font-weight: 900 !important; }
    h2 { color: #FFD700 !important; font-size: 4rem !important; font-weight: 800 !important; }
    .stMetricValue { font-size: 5rem !important; color: #FFFFFF !important; font-weight: 700 !important; }
    .stMetricLabel { font-size: 1.8rem !important; color: #FFD700 !important; }
    p, div, li { font-size: 1.6rem !important; line-height: 1.5 !important; }
</style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    if os.path.exists("LOGO (4RT).png"):
        st.image("LOGO (4RT).png", use_column_width=True)
    st.divider()
    menu = st.selectbox("Módulos de Gestión", ["Identidad", "Portafolio", "Financiero", "Ecobot"], key="menu_main")

# --- 6. RENDERIZADO ---
if menu == "Identidad":
    render_identity()
elif menu == "Portafolio":
    render_portfolio()
elif menu == "Financiero":
    render_financiero(van=2800000, tir=31, roi=145, cb=3.4, insight_texto="Viabilidad técnica y circular confirmada.")
elif menu == "Ecobot":
    render_ecobot()