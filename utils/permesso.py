from telegram import Update
from telegram.ext import ContextTypes

async def permesso_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏰ Inserisci orario e motivo del permesso (funzione in sviluppo)")