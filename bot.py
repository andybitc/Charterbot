import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
ALLOWED_GROUP_ID = int(os.environ["ALLOWED_GROUP_ID"])

KEYWORDS = ["Redditor", "Redditors", "redditor", "redditors"]

async def check_message(update, context):
    if update.message.chat_id != ALLOWED_GROUP_ID:
        return
    message = update.message
    text = (message.text or message.caption or "").lower()
    if any(kw in text for kw in KEYWORDS):
        await message.reply_text("Me")

async def check_forward(update, context):
    if update.message.chat_id != ALLOWED_GROUP_ID:
        return
    # Triggers on ANY forwarded message regardless of content
    await update.message.reply_text("Me")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))
app.add_handler(MessageHandler(filters.FORWARDED, check_forward))
app.run_polling()
