import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# --- CONFIGURACIÓN DE LOGS ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- IMPORTACIÓN SEGURA ---
# Intentamos importar Streamlit solo para capturar el secreto si existe
try:
    import streamlit as st
except ImportError:
    st = None

try:
    from src.modules.data_analyzer import get_kpi_summary
except ImportError:
    # Fallback si no encuentra el módulo para evitar que el bot muera
    def get_kpi_summary(): return "Error: Módulo de datos no disponible."

# --- LÓGICA DE CREDENCIALES (HÍBRIDA) ---
def get_token():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token and st and hasattr(st, "secrets"):
        try:
            token = st.secrets["TELEGRAM_TOKEN"]
        except:
            pass
    return token

# --- COMANDOS DEL BOT ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="🤖 **ECORADARCONSULTOR** activo.\n\nComandos disponibles:\n/resumen - Ver KPIs actuales\n/status - Estado del sistema"
    )

async def resumen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Enviar mensaje mientras se procesa
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Calculando indicadores...")
    mensaje = get_kpi_summary()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje, parse_mode='Markdown')

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🚀 Ecosistema 4R+T: **Online** y operativo.")

# --- NÚCLEO DEL SERVICIO ---
def run_telegram_service():
    token = get_token()
    if not token:
        logging.error("Token de Telegram NO encontrado. Verifica tus variables de entorno o Secrets.")
        return

    application = ApplicationBuilder().token(token).build()
    
    # Manejadores
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('resumen', resumen))
    application.add_handler(CommandHandler('status', status))
    
    logging.info("ECORADARCONSULTOR escuchando en Telegram...")
    application.run_polling()