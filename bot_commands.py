import telebot
import model as mod
import datetime
from datetime import datetime


bot = telebot.TeleBot('TOKEN')
now = datetime.now()
@bot.message_handler(content_types=['text'])


def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,"Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(
            message.from_user.id, "Я могу помочь тебе.\n- Если хочешь задать вопрос, напиши 'Привет'\
                \n- Если хочешь узнать, сколько сейчас время, напиши 'Время'\
                \n- Если хочешь узнать, какая сегодня дата, напиши 'Дата'")
    elif message.text == "Время":
        bot.send_message(message.from_user.id, {now.strftime("%H:%M:%S")})
    elif message.text == "Дата":
        bot.send_message(message.from_user.id, {now.strftime("%Y-%m-%d")})
    # elif message.text == "Фибо":
    #     bot.send_message(message.from_user.id, "Введите число")
    #     num = input()
    #     bot.send_message(message.from_user.id, {mod.fib(num)})   
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")





#  from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# import datetime
# # hi_command
# # time_command
# # help_command
# # sum_command

# def hi_comand(update: Update, context: CallbackContext):
#     update.message.reply_text(f'Hi{update.effective_user.first_name}!')

# def help_command(update: Update, context: CallbackContext):
#     update.message.reply_text(f'/hi\n/time\n/help')

# def time_command(update: Update, context: CallbackContext):
#     update.message.reply_text(f'{datetime.datetime.now().time()}')

# # def sum_command(update: Update, context: CallbackContext):
# #     update.message.reply_text(f'Hi{update.effective_user.first_name}!')

