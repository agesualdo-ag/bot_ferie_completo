from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Benvenuto! Usa il menu per:\n/ferie - Richiedi ferie\n/permesso - Richiedi permesso orario")
