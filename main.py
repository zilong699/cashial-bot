from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# 从环境变量获取 Bot Token（更安全）
TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_URL = "https://t.me/apectrade07"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📚 Learn about Web3 rewards", url=CHANNEL_URL)],
        [InlineKeyboardButton("🚀 View featured projects", url=CHANNEL_URL)],
        [InlineKeyboardButton("🎁 Access member benefits", url=CHANNEL_URL)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        text=(
            "👋 Welcome to *Cashial Assistant Bot*!\n\n"
            "Tap any option below to explore exclusive resources and join the community 👇"
        ),
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Use /start to see the options and explore Web3 rewards.")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("❓ I didn't understand that. Please tap /start to begin.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    updater.start_polling()
    print("✅ Cashial Assistant Bot is running...")
    updater.idle()

if __name__ == '__main__':
    main()
