from telegram.ext import *
from telegram import *
from information import *
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'anurag_telegram_refund.settings'
django.setup()

from home.models import *

def start(update: Update, context: CallbackContext):
      kb = [[KeyboardButton('Stores')], [KeyboardButton('Forms')], [KeyboardButton('Giveaways')], [KeyboardButton('Tickets')], [KeyboardButton('Vouchers')]]
      kb_markup = ReplyKeyboardMarkup(kb)
      print(update.message.chat_id)
      context.bot.send_message(chat_id=update.message.chat_id,
      text=f"Hi, {update['message']['chat']['first_name']}. Kindly Select one of the following:", reply_markup=kb_markup)

def handle_message(update, context):
# update.message.reply_text(f"Hi, {update['message']['chat']['first_name']}")

# update.message.reply(reply_markup=keyboard1)

      # stores = [[KeyboardButton('Store 1')], [KeyboardButton('Store 2')], [KeyboardButton('Store 3')], [KeyboardButton('Store 4')], [KeyboardButton('Store 5')]]
      # store_markup = ReplyKeyboardMarkup(stores)

      if update.message.text == "Stores":
            # stores = []
            stores_list = []

            stores_obj = Store.objects.all()

            for store in stores_obj:
                  stores_list.append(f"{store.id}\n{store.store_name}\n{store.store_address}\n{store.store_state}\n{store.store_pincode}")

            print(update.message.chat_id)
            store_markup = ReplyKeyboardMarkup([[store.id, ] for store in stores_obj])

            context.bot.send_message(chat_id=update.message.chat_id, text=f"Hi, {update['message']['chat']['first_name']}. Kindly select the store id of one of the stores:\n" + "\n\n".join(stores_list), reply_markup=store_markup)

            

      vouchers = [[KeyboardButton('Voucher 1')], [KeyboardButton('Voucher 3')], [KeyboardButton('Voucher 2')], [KeyboardButton('Voucher 4')], [KeyboardButton('Voucher 5')]]
      voucher_markup = ReplyKeyboardMarkup(vouchers)

      if update.message.text == "Vouchers":
            context.bot.send_message(chat_id=update.message.chat_id, text=f"Hi, {update['message']['chat']['first_name']}. Kindly Select one of the stores:", reply_markup=voucher_markup)

      tickets = [[KeyboardButton('Active Tickets')], [KeyboardButton('New Ticket')]]
      ticket_markup = ReplyKeyboardMarkup(tickets)

      if update.message.text == "Tickets":
            context.bot.send_message(chat_id=update.message.chat_id,
      text=f"Hi, {update['message']['chat']['first_name']}. Kindly Select one of the tickets:", reply_markup=ticket_markup)

      activetickets = [[KeyboardButton('Ask for an update')], [KeyboardButton('Delete Ticket')]]
      active_ticket_markup = ReplyKeyboardMarkup(activetickets)

      if update.message.text == "Active Tickets":
            context.bot.send_message(chat_id=update.message.chat_id, text="Ticket Nos: 1\nIssue: Refund delayed\nIssue Created: 24/01/22\nStatus: Pending", reply_markup=active_ticket_markup)
            # update.message.reply_text(f"Ticket Nos: 1\nIssue: Refund delayed\nIssue Created: 24/01/22\nStatus: Pending")

if __name__ == '__main__':
      updater = Updater(BOT_API, use_context=True)
      dp = updater.dispatcher

      dp.add_handler(CommandHandler("start", start))
      dp.add_handler(MessageHandler(Filters.text, handle_message))

      updater.start_polling(1.0)
      updater.idle()