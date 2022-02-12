from telegram.ext import *
from telegram import *
from information import *
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'anurag_telegram_refund.settings'
django.setup()

from home.models import *

def start(update: Update, context: CallbackContext):
      kb = [[KeyboardButton('Stores')], [KeyboardButton('Forms')], [KeyboardButton('Giveaways')], [KeyboardButton('Tickets')], [KeyboardButton('Vouches')]]
      kb_markup = ReplyKeyboardMarkup(kb)
      context.bot.send_message(chat_id=update.message.chat_id,
      text=f"Hi, {update['message']['chat']['first_name']}. Kindly Select one of the following:", reply_markup=kb_markup)

def handle_message(update, context):

      if len(context.user_data) == 0:
            context.user_data["initial"] = [update.message.text]
      else:
            context.user_data["initial"].append(update.message.text)
      print(context.user_data)

      if context.user_data["initial"][0] == "Stores":
            if len(context.user_data["initial"]) == 1:
            # stores = []
                  stores_list = []

                  stores_obj = Store.objects.all()

                  for store in stores_obj:
                        stores_list.append(f"{store.id}\n{store.store_name}\n{store.store_address}\n{store.store_state}\n{store.store_pincode}")

                  print(update.message.chat_id)
                  store_markup = ReplyKeyboardMarkup([[store.id, ] for store in stores_obj])

                  context.bot.send_message(chat_id=update.message.chat_id, text=f"Hi, {update['message']['chat']['first_name']}. Kindly select the store id of one of the stores:\n" + "\n\n".join(stores_list), reply_markup=store_markup)

if __name__ == '__main__':
      updater = Updater(BOT_API, use_context=True)
      dp = updater.dispatcher

      dp.add_handler(CommandHandler("start", start))
      dp.add_handler(MessageHandler(Filters.text, handle_message))

      updater.start_polling(1.0)
      updater.idle()