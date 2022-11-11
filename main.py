import telebot
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
            message.from_user.id, "Я могу помочь тебе.\n- Если хочешь задать вопрос, напиши 'Привет'\n\
                - Если хочешь узнать, сколько сейчас время, напиши 'Время'\n\
                - Если хочешь узнать, какая сегодня дата, напиши 'Дата'")
    elif message.text == "Время":
        bot.send_message(message.from_user.id, {now.strftime("%H:%M:%S")})
    elif message.text == "Дата":
        bot.send_message(message.from_user.id, {now.strftime("%Y-%m-%d")})
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)


# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# import datetime
# import bot_commands as bc

# updater = Update("5662038385:AAF2I6d4wI78B4jOQ9Erkb_U7-uPBBnDyGo")
# updater.dispatcher.add_handler(CommandHandler('hi', bc.hi_comand))
# updater.dispatcher.add_handler(CommandHandler('time', bc.time_command))
# updater.dispatcher.add_handler(CommandHandler('help', bc.help_command))
# updater.dispatcher.add_handler(CommandHandler('sum', bc.sum_command))

# def hi_comand(update: Update, context: CallbackContext):
#     update.message.reply_text(f'Hi{update.effective_user.first_name}!')

# def help_command(update: Update, context: CallbackContext):
#     update.message.reply_text(f'/hi\n/time\n/help')

# def time_command(update: Update, context: CallbackContext):
#     update.message.reply_text(f'{datetime.datetime.now().time()}')


# print('server start')
# updater.start_polling()
# updater.idle()

# def log(update: Update, context: CallbackContext):
#  file = open('db.csv', 'a')
#  file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
#  file.close()
