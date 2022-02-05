from telegram import * 
from telegram.ext import * 
from information import *
# from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

def start(update: Update, context: CallbackContext):
    kb = [[KeyboardButton('Stores')],
          [KeyboardButton('Forms')],
          [KeyboardButton('Giveaways')],
          [KeyboardButton('Tickets')],
          [KeyboardButton('Vouchers')]
          ]
    kb_markup = ReplyKeyboardMarkup(kb)
    context.bot.send_message(chat_id=update.message.chat_id,
                     text="your message",
                     reply_markup=kb_markup)


def handle_message(update , context):
    update.message.reply_text(f"Hi, {update['message']['chat']['first_name']}")

    # update.message.reply(reply_markup=keyboard1)

if __name__ == '__main__':
    updater = Updater(BOT_API , use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text , handle_message))

    updater.start_polling(1.0)
    updater.idle()