import streamlit as st
import os
import sys

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