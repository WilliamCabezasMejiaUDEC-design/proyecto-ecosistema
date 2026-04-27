import sys
import os

# Agregamos la ruta actual al sistema para que encuentre la carpeta 'src'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

# 1. Blindaje de entorno: Asegura que Python encuentre la carpeta 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# 2. Imports Modulares
from src.modules.identity import render_identity
from src.modules.portfolio import render_portfolio
from src.modules.financial import render_financiero
from src.modules.ecobot import render_ecobot
from src.modules.ml_engine import run_ml_analysis

# 3. Configuración inicial
st.set_page_config(page_title="Ecosistema 4R+T", layout="wide", initial_sidebar_state="expanded")

# 4. Inyección de Estilos (CSS externo desde la raíz)
def load_css():
    if os.path.exists("style.css"):
        with open("style.css", "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# 5. Sidebar Maestro
st.sidebar.title("⚡ 4R+T Labs")
menu = st.sidebar.radio("Navegación", ["Identidad", "Portafolio", "Financiero", "Ecobot", "IA Engine"])

st.sidebar.markdown("---")
st.sidebar.caption("Proyecto Final · Inteligencia Circular")

# 6. Renderizado Condicional (Limpio y Funcional)
def main():
    if menu == "Identidad":
        render_identity()
    elif menu == "Portafolio":
        render_portfolio()
    elif menu == "Financiero":
        # Datos inyectados: Mantenemos el estándar de tu arquitectura
        render_financiero(van=2800000, tir=31, roi=145, cb=3.4, insight_texto="Viabilidad técnica confirmada.")
    elif menu == "Ecobot":
        render_ecobot()
    elif menu == "IA Engine":
        # Asegúrate de que este archivo exista en tu carpeta data
        csv_path = os.path.join("data", "datos_4RT_historico.csv")
        run_ml_analysis(csv_path, target_col='riesgo')

if __name__ == "__main__":
    main()

import streamlit as st
import os
import sys

# --- 1. CONFIGURACIÓN DE RUTA (BLINDAJE) ---
base_path = os.path.dirname(os.path.abspath(__file__))
if base_path not in sys.path:
    sys.path.insert(0, base_path)

# --- 2. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="4R+T | Ecosistema Circular", layout="wide")

# --- 3. IMPORTACIONES ---
try:
    from src.modules.financial import render_financiero
    from src.modules.ecobot import render_ecobot
    from src.modules.identity import render_identity
    from src.modules.portfolio import render_portfolio
except ImportError as e:
    st.error(f"Error de Importación: {e}")
    st.stop()

# --- 4. CSS INDUSTRIAL (Optimizado) ---
st.markdown("""
<style>
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; }
    
    /* Títulos masivos */
    h1 { color: #FFD700 !important; font-size: 5rem !important; font-weight: 900 !important; }
    h2 { color: #FFD700 !important; font-size: 4rem !important; font-weight: 800 !important; }
    
    /* Texto y Métricas */
    .stMetricValue { font-size: 5rem !important; color: #FFFFFF !important; font-weight: 700 !important; }
    .stMetricLabel { font-size: 1.8rem !important; color: #FFD700 !important; }
    p, div, li { font-size: 1.6rem !important; line-height: 1.5 !important; }
</style>
""", unsafe_allow_html=True)


# --- 5. SIDEBAR (CORRECCIÓN DE IMAGEN) ---
with st.sidebar:
    if os.path.exists("LOGO (4RT).png"):
        # USAMOS EL COMANDO COMPATIBLE CON TU VERSIÓN
        st.image("LOGO (4RT).png", use_column_width=True)
    st.divider()

# ASIGNACIÓN GLOBAL DEL MENÚ
menu = st.sidebar.selectbox(
    "Módulos de Gestión", 
    ["Identidad", "Portafolio", "Financiero", "Ecobot"], 
    key="menu_main"
)

# --- 6. RENDERIZADO ---
if menu == "Identidad":
    render_identity()
elif menu == "Portafolio":
    render_portfolio()
elif menu == "Financiero":
    render_financiero(van=2800000, tir=31, roi=145, cb=3.4, insight_texto="Viabilidad técnica y circular confirmada.")
elif menu == "Ecobot":
    render_ecobot()