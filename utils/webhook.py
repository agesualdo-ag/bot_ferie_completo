import os

async def run_webhook(application):
    port = int(os.getenv("PORT", 8080))
    webhook_url = os.getenv("WEBHOOK_URL")
    await application.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=webhook_url
    )
