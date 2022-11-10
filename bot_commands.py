from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
# hi_command
# time_command
# help_command
# sum_command

def hi_comand(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi{update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help')

def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')

# def sum_command(update: Update, context: CallbackContext):
#     update.message.reply_text(f'Hi{update.effective_user.first_name}!')

