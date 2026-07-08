import os

from telegram import Update
from telegram.ext import ContextTypes

from excel_manager import ExcelManager
from ai_engine import answer_question
from qr_reader import read_qr

manager = ExcelManager()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 AI Project Assistant Ready!\n\n"
        "You can:\n"
        "• Ask questions\n"
        "• Send UID\n"
        "• Upload QR Code"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Examples:\n\n"
        "Who is Alice?\n"
        "Marketing\n"
        "UID-005\n\n"
        "Or simply upload a QR code."
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    question = update.message.text

    rows = manager.search_anything(question)

    if len(rows) == 0:
        rows = manager.df

    answer = answer_question(question, rows)

    await update.message.reply_text(answer)


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    photo = update.message.photo[-1]

    telegram_file = await photo.get_file()

    os.makedirs("temp", exist_ok=True)

    image_path = "temp/qr.png"

    await telegram_file.download_to_drive(image_path)

    uid = read_qr(image_path)

    if uid is None:

        await update.message.reply_text(
            "❌ QR Code not detected."
        )

        return

    rows = manager.get_by_uid(uid)

    if len(rows) == 0:

        await update.message.reply_text(
            f"❌ UID {uid} not found."
        )

        return

    answer = answer_question(uid, rows)

    await update.message.reply_text(answer)