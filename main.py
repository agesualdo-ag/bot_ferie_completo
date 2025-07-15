import os
import asyncio
from telegram.ext import ApplicationBuilder
from handlers.commands import setup_handlers  # ✅ Importa la funzione correttamente
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    setup_handlers(application)  # ✅ chiama la funzione registrando i comandi

    await application.bot.set_webhook(url=WEBHOOK_URL)

    await application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    asyncio.run(main())
