from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Benvenuto! Usa il menu per:
"
        "/ferie - Richiedi ferie
"
        "/permesso - Richiedi permesso orario
"
        "/storico - Visualizza lo storico richieste"
    )