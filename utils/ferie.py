from telegram import Update
from telegram.ext import ContextTypes

async def ferie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🗓️ Inserisci le date per le ferie (funzione in sviluppo)")