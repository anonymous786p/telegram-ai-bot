from telegram import Update
from telegram.ext import ContextTypes

from excel_manager import ExcelManager
from ai_engine import answer_question

manager = ExcelManager()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 AI Project Assistant Ready!\n\n"
        "You can:\n"
        "• Ask questions\n"
        "• Search by Project\n"
        "• Search by Employee\n"
        "• Search by UID"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Examples:\n\n"
        "Who is Alice?\n"
        "Marketing\n"
        "UID-005"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    question = update.message.text

    rows = manager.search_anything(question)

    if len(rows) == 0:
        rows = manager.df

    answer = answer_question(question, rows)

    await update.message.reply_text(answer)