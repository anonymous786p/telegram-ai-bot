from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import (
    start,
    help_command,
    message_handler,
    photo_handler,
)

# Create Telegram Application
application = Application.builder().token(BOT_TOKEN).build()

# Commands
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))

# Text Messages
application.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        message_handler,
    )
)

# Photo / QR Code
application.add_handler(
    MessageHandler(
        filters.PHOTO,
        photo_handler,
    )
)

print("🤖 Bot Started...")

application.run_polling()