import requests
import time
from telegram.ext import * 
from information import *

def handle_message(update , context):
    text = str(update.message.text).lower()

    update.message.reply_text(f"Hi, {update['message']['chat']['first_name']}")

if __name__ == '__main__':
    updater = Updater(BOT_API , use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text , handle_message))

    updater.start_polling(1.0)
    updater.idle()