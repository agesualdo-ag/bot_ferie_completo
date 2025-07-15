import os
from telegram.ext import ApplicationBuilder
from handlers.commands import setup_handlers
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Registra tutti gli handler
    setup_handlers(application)

    # Imposta il Webhook
    await application.bot.set_webhook(url=WEBHOOK_URL)

    # Mantieni attivo il bot con Webhook
    await application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
