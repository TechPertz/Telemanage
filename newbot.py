from information import *
import telebot
from telebot import types

import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'anurag_telegram_refund.settings'
django.setup()

from home.models import *

bot = telebot.TeleBot(BOT_API)


user_dict = {}
form_dict = {}
ticket_dict = {}
vouch_dict = {}


class Ticket_class:
    def __init__(self, name):
        self.user_name = name
        self.user_id = None
        self.ticket_nos = None

class Form_class:
    def __init__(self, name):
        self.user_name = name
        self.user_id = None
        self.store = None
        self.enquiry = None

class Ticket_class:
    def __init__(self, name):
        self.user_name = name
        self.user_id = None
        self.issue = None
        self.ticket_status = None

class Vouch_class:
    def __init__(self, name):
        self.user_name = name
        self.user_id = None
        self.vouch = None


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    kb_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    kb_markup.add("Stores", "Forms").add("Vouches", "Tickets")
    msg = bot.reply_to(message, """\
Hi there, I am ypur Refund bot.
Please select one of the following options:
""", reply_markup=kb_markup)
    bot.register_next_step_handler(msg, decider)

@bot.message_handler(commands=['cancel'])
def cancel(message):
        bot.next_step_backend.clear_handlers(message)

def decider(message):
    print(message.text)
    print(type(message.text))
    if message.text == "Stores" or message.text == "Forms":

        stores_list = []

        stores_obj = Store.objects.all()

        for store in stores_obj:
            stores_list.append(f"{store.id}\n{store.store_name}\n{store.store_address}\n{store.store_state}\n{store.store_pincode}")
        
        stores_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        stores_markup.add(*[str(store.id) for store in stores_obj], row_width=2)    

        msg = bot.reply_to(message, text=f"Hi! Kindly select the store id of one of the stores:\n" + "\n\n".join(stores_list), reply_markup=stores_markup)

        bot.register_next_step_handler(msg, get_enquiry_for_store)
    
    # if message.text == "Forms":
    #     None
    # if message.text == "Giveaways":
    #     None
    if message.text == "Tickets":
        tickets_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        tickets_markup.add("Your Existing Tickets", "New Tickets", row_width=1) 
        msg = bot.reply_to(message, text=f"Hi! Kindly select one of the following:\n" + "\n\n", reply_markup=tickets_markup)
        bot.register_next_step_handler(msg, your_tickets)

    if message.text == "Vouches":
        vouches_list = []

        vouches_obj = Vouch.objects.all()

        if len(vouches_obj) != 0:
            for vouch in vouches_obj:
                vouches_list.append(f"{vouch.id}\n{vouch.vouch}")

            bot.send_message(message.chat.id, "\n\n".join(vouches_list))
            
        msg = bot.reply_to(message, text=f"Hi! Thanks for deciding to give me a vouch. Kindly enter below:\n")
        bot.register_next_step_handler(msg, save_vouch)

def save_vouch(message):

    v = Vouch()
    v.user_id = message.from_user.id
    v.user_name = message.from_user.username
    v.vouch = message.text
    v.save()

    bot.send_message(message.chat.id, 'Your vouch has been submitted!\n' + "Vouch ID: " + str(v.id) + "\nUsername: " + v.user_name + "\nVouch: " + v.vouch)


def your_tickets(message):
    if message.text == "Your Existing Tickets":
        tickets_list = []

        try:
            tickets_obj = Ticket.objects.filter(user_id = message.from_user.id)
            for ticket in tickets_obj:
                tickets_list.append(f"{ticket.ticket_nos}\n{ticket.user_name}\n{ticket.issue}\n{ticket.ticket_status}")

            msg = bot.reply_to(message, text=f"Hi! These are the list of all your tickets:\n" + "\n\n".join(tickets_list))
        
        except Ticket.DoesNotExist:
            msg = bot.reply_to(message, text=f"Hi! There aren't any tickets available for your account!\n")

        # if tickets_obj.exists():
        #     for ticket in tickets_obj:
        #         tickets_obj.append(f"{ticket.ticket_nos}\n{ticket.user_name}\n{ticket.issue}\n{ticket.ticket_status}")

        #     msg = bot.reply_to(message, text=f"Hi! These are the list of all your tickets:\n" + "\n\n".join(tickets_list))
        # else:
        #     msg = bot.reply_to(message, text=f"Hi! There aren't any tickets available for your account!\n")
        
    if message.text == "New Tickets":
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_name = message.from_user.username
        ticket_class = Ticket_class(user_name)
        ticket_class.user_id = user_id
        ticket_dict[chat_id] = ticket_class

        msg = bot.reply_to(message, "Kindly state your issue:")
        bot.register_next_step_handler(msg, save_ticket)

def save_ticket(message):
    chat_id = message.chat.id
    issue = message.text
    ticket_class = ticket_dict[chat_id]
    ticket_class.issue = issue

    t = Ticket()
    t.user_id = ticket_class.user_id
    t.user_name = ticket_class.user_name
    t.issue = ticket_class.issue
    t.save()

    bot.send_message(chat_id, 'Your ticket has been submitted!\n' + "Ticket ID: " + str(t.ticket_nos) + "\nUsername: " + t.user_name + "\nIssue: " + t.issue)

        

def get_enquiry_for_store(message):

    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.username
    form_class = Form_class(user_name)
    form_class.user_id = user_id
    print(message.text)
    print(type(message.text))
    form_class.store = Store.objects.get(id=int(message.text))
    form_dict[chat_id] = form_class

    msg = bot.reply_to(message, "Kindly state your enquiry:")
    bot.register_next_step_handler(msg, save_form)

def forms(message):
    None

def giveaways(message):
    None

def tickets(message):
    None

def vouches(message):
    None

def save_form(message):
    chat_id = message.chat.id
    enquiry = message.text
    form_class = form_dict[chat_id]
    form_class.enquiry = enquiry

    f = Form()
    f.user_id = form_class.user_id
    f.user_name = form_class.user_name
    f.enquiry = form_class.enquiry
    f.store = form_class.store
    f.save()

    bot.send_message(chat_id, 'Your form has been submitted!\n' + "Store ID: " + str(form_class.store) + "\nUsername: " + form_class.user_name + "\nIssue: " + form_class.enquiry)

# def process_name_step(message):
#     try:
#         chat_id = message.chat.id
#         name = message.text
#         user = User(name)
#         user_dict[chat_id] = user
#         msg = bot.reply_to(message, 'How old are you?')
#         bot.register_next_step_handler(msg, process_age_step)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')


# def process_age_step(message):
#     try:
#         chat_id = message.chat.id
#         age = message.text
#         if not age.isdigit():
#             msg = bot.reply_to(message, 'Age should be a number. How old are you?')
#             bot.register_next_step_handler(msg, process_age_step)
#             return
#         user = user_dict[chat_id]
#         user.age = age
#         markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#         markup.add('Male', 'Female')
#         msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
#         bot.register_next_step_handler(msg, process_sex_step)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')


# def process_sex_step(message):
#     try:
#         chat_id = message.chat.id
#         sex = message.text
#         user = user_dict[chat_id]
#         if (sex == u'Male') or (sex == u'Female'):
#             user.sex = sex
#         else:
#             raise Exception("Unknown sex")
#         bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
# bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

bot.infinity_polling()