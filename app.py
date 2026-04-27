import sys
import os
import streamlit as st

# --- 1. BLINDAJE DE RUTA (CRÍTICO) ---
# Forzamos a Python a reconocer la raíz del proyecto para que 'src' sea importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- 2. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="4R+T | Ecosistema Circular", layout="wide")

# --- 3. TEMA "DEEP SPACE" (CSS LIGERO) ---
st.markdown("""
<style>
    .stApp { background-color: #050505 !important; color: #E0E0E0 !important; }
    h1, h2 { color: #00FF9D !important; font-weight: 800 !important; }
    .stMetricValue { color: #FFFFFF !important; }
    .stMetricLabel { color: #00FF9D !important; }
</style>
""", unsafe_allow_html=True)

# --- 4. IMPORTACIÓN SEGURA DE MÓDULOS ---
# Usamos try-except para atrapar errores antes de que colapse la app
try:
    from src.modules.identity import render_identity
    from src.modules.portfolio import render_portfolio
    from src.modules.financial import render_financiero
    from src.modules.ecobot import render_ecobot
except ImportError as e:
    st.error(f"Error crítico de estructura: {e}")
    st.info("Asegúrate de que existan archivos __init__.py en src y src/modules/")
    st.stop()

# --- 5. INTERFAZ Y NAVEGACIÓN ---
with st.sidebar:
    if os.path.exists("LOGO (4RT).png"):
        st.image("LOGO (4RT).png", use_column_width=True)
    st.markdown("---")
    menu = st.selectbox("Módulos de Gestión", ["Identidad", "Portafolio", "Financiero", "Ecobot"])

# --- 6. EJECUCIÓN (Lógica única) ---
if menu == "Identidad":
    render_identity()
elif menu == "Portafolio":
    render_portfolio()
elif menu == "Financiero":
    render_financiero(van=2800000, tir=31, roi=145, cb=3.4)
elif menu == "Ecobot":
    render_ecobot()