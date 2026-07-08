from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
)

from bot import application

from handlers import (
    start,
    help_command,
    message_handler,
    photo_handler,
)

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))

application.add_handler(
    MessageHandler(
        filters.PHOTO,
        photo_handler,
    )
)

application.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        message_handler,
    )
)

print("🤖 Bot Started...")

application.run_polling()