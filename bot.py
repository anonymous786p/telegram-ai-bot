from telegram.ext import Application
from config import BOT_TOKEN

application = Application.builder().token(BOT_TOKEN).build()

