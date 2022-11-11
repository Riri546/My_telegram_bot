# import bot_commands as bc

num = int(input())

def summ():
    print(sum(num))

# def start(message):
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, "Как тебя зовут?")
#         # следующий шаг – функция get_name
#         bot.register_next_step_handler(message, get_name)
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /reg')