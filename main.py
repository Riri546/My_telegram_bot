from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import bot_commands as bc

updater = Updater('5662038385:AAF2I6d4wI78B4jOQ9Erkb_U7-uPBBnDyGo')
updater.dispatcher.add_handler(CommandHandler('hi', bc.hi_comand))
updater.dispatcher.add_handler(CommandHandler('time', bc.time_command))
updater.dispatcher.add_handler(CommandHandler('help', bc.help_command))
updater.dispatcher.add_handler(CommandHandler('sum', bc.sum_command))



print('server start')
updater.start_polling()
updater.idle()

def log(update: Update, context: CallbackContext):
 file = open('db.csv', 'a')
 file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
 file.close()