import telebot
import model as mod
import datetime
from datetime import datetime


bot = telebot.TeleBot('5662038385:AAF2I6d4wI78B4jOQ9Erkb_U7-uPBBnDyGo')


# name = ''
# surname = ''
# age = 0
now = datetime.now()


@bot.message_handler(content_types=['text'])


# def start(message):
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, "Как тебя зовут?")
#         # следующий шаг – функция get_name
#         bot.register_next_step_handler(message, get_name)
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /reg')


# def get_name(message):  # получаем фамилию
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
#     bot.register_next_step_handler(message, get_surname)


# def get_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message('Сколько тебе лет?')
#     bot.register_next_step_handler(message, get_age)


# def get_age(message):
#     global age
#     while age == 0:  # проверяем что возраст изменился
#         try:
#             age = int(message.text)  # проверяем, что возраст введен корректно
#         except Exception:
#             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#             bot.send_message(message.from_user.id, 'Тебе '+str(age) +
#                      ' лет, тебя зовут '+name+' '+surname+'?')


def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(
            message.from_user.id, "Я могу помочь тебе.\n- Если хочешь задать вопрос, напиши 'Привет'\
                \n- Если хочешь узнать, сколько сейчас время, напиши 'Время'\
                \n- Если хочешь узнать, какая сегодня дата, напиши 'Дата'")
    elif message.text == "Время":
        bot.send_message(message.from_user.id, {now.strftime("%H:%M:%S")})
    elif message.text == "Дата":
        bot.send_message(message.from_user.id, {now.strftime("%Y-%m-%d")})
    # elif message.text == "Сумма":
    #     bot.send_message(message.from_user.id, {now.strftime("%Y-%m-%d")})

    # elif message.text == "Фибо":
    #     bot.send_message(message.from_user.id, "Введите число")
    #     num = input()
    #     bot.send_message(message.from_user.id, {mod.fib(num)})
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")


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
