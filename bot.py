import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]
ALLOWED_GROUP_ID = int(os.environ["ALLOWED_GROUP_ID"])

KEYWORDS = ["charters", "charter"]

async def check_message(update, context):
    if update.message.chat_id != ALLOWED_GROUP_ID:
        return
    message = update.message
    text = (message.text or message.caption or "").lower()
    if any(kw in text for kw in KEYWORDS):
        await message.reply_text("Me")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))
app.add_handler(MessageHandler(filters.FORWARDED, check_message))
app.run_polling()
