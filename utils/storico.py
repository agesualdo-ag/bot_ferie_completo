from telegram import Update
from telegram.ext import ContextTypes

async def storico_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📚 Storico richieste (funzione in sviluppo)")