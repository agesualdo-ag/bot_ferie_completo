from telegram.ext import CommandHandler
from .start import start

def setup_handlers(application):
    application.add_handler(CommandHandler("start", start))
