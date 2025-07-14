import logging
import nest_asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Attiva nest_asyncio per Render
nest_asyncio.apply()

# Carica le variabili d'ambiente da .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Log
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Benvenuto
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['/ferie', '/permesso'], ['/storico']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        """👋 Benvenuto! Usa il menu per:
/ferie - Richiedi ferie
/permesso - Richiedi permesso orario
/storico - Vedi le tue richieste""",
        reply_markup=reply_markup
    )

# Comando ferie
async def ferie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Funzione FERIE in sviluppo...")

# Comando permesso
async def permesso(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏰ Funzione PERMESSO in sviluppo...")

# Comando storico
async def storico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🗂️ Funzione STORICO in sviluppo...")

# Avvia il bot
async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ferie", ferie))
    application.add_handler(CommandHandler("permesso", permesso))
    application.add_handler(CommandHandler("storico", storico))

    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
