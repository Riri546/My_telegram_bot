import bot_commands as bc

bc.bot.polling(none_stop=True, interval=0)




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

