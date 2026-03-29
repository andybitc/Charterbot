Good thinking! Forwarded messages need a small extra line in the code. Here's the updated **bot.py:**

```python
from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = "PASTE_YOUR_TOKEN_HERE"
ALLOWED_GROUP_ID = -1001234567890  # Paste your GC ID here

KEYWORDS = ["Redditors", "redditors", "Redditor"]

async def check_message(update, context):
    if update.message.chat_id != ALLOWED_GROUP_ID:
        return
    
    # This handles both normal AND forwarded messages
    message = update.message
    text = (message.text or message.caption or "").lower()
    
    if any(kw in text for kw in KEYWORDS):
        await message.reply_text("Me")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))
app.add_handler(MessageHandler(filters.FORWARDED, check_message))
app.run_polling()
```

---

**What changed:**
- Added `filters.FORWARDED` so it listens for forwarded messages too
- Added `message.caption` so it also catches keywords in **photo/video captions** (in case the admin forwards an image with text)

---

So now it will detect keywords whether the message is:
- ✅ Typed normally
- ✅ Forwarded by the admin
- ✅ A forwarded photo/video with a caption

Go ahead and use this updated code when uploading! 😊