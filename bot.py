from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = "7962721050:AAFu_4VUq-W7MbRFupUIUhvG94Ov_1leaQY"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть питомца 🐾", web_app=WebAppInfo(url="https://shizykalnstinct.github.io/MyTalkingKktek.github.io/"))]  # <- Замени на свой URL!
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Это твой говорящий питомец:", reply_markup=reply_markup)

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()