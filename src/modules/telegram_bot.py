import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from src.modules.data_analyzer import get_kpi_summary

# --- BLINDAJE DE IMPORTACIÓN ---
# Intentamos cargar streamlit, si no existe (al correr en terminal), st será None
try:
    import streamlit as st
except ImportError:
    st = None

# --- CONFIGURACIÓN DE LOGS ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- FUNCIÓN SEGURA PARA EL TOKEN ---
def get_safe_token():
    # 1. Busca en variables de entorno (Lo que configuras en tu PC con 'set')
    token = os.getenv("TELEGRAM_TOKEN")
    # 2. Si no lo encuentra y Streamlit está disponible, busca en secrets
    if not token and st is not None:
        try:
            token = st.secrets.get("TELEGRAM_TOKEN")
        except:
            token = None
    return token

# --- COMANDOS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="🤖 **ECORADARCONSULTOR** activo.\n\nComandos disponibles:\n/resumen - Ver KPIs actuales\n/status - Estado del sistema"
    )

async def resumen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Calculando indicadores...")
    mensaje = get_kpi_summary()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje, parse_mode='Markdown')

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🚀 Ecosistema 4R+T: **Online** y operativo.")

# --- NÚCLEO ---
def run_telegram_service():
    token = get_safe_token()
    
    if not token:
        logging.error("Token de Telegram NO encontrado. Configura la variable 'TELEGRAM_TOKEN' en tu terminal.")
        return

    application = ApplicationBuilder().token(token).build()
    
    # Manejadores
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('resumen', resumen))
    application.add_handler(CommandHandler('status', status))
    
    logging.info("ECORADARCONSULTOR escuchando en Telegram...")
    application.run_polling()

if __name__ == "__main__":
    run_telegram_service()