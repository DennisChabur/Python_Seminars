from telebot import TeleBot, types
import os

TOKEN = '5972349135:AAGOKrfsJlIaI_L9JkB4EHpPrtONMa6TK7Y'

bot = TeleBot(TOKEN)


# Функция для сохранения документа, отправленного боту
# @bot.message_handler(content_types=['document'])
# def answer(msg: types.Message):
#     filename = msg.document.file_name
#     with open(filename, 'wb') as file:
#         file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
#     bot.send_message(chat_id=msg.from_user.id, text='Вывожу логыыыы')

    # Можете раскомментировать, если потребуется затем удалять файл после обработки,
    # чтобы не тратить память.
    # Не забудьте импортировать os
    # os.remove(filename)


dct = {}


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    dct[msg.from_user.id] = []
    bot.send_message(chat_id=msg.from_user.id, text=f'Здравствуйте. Введите арифметическую операцию')


@bot.message_handler(commands=['log'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')


@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text
    if text == '+':
        bot.register_next_step_handler(msg, sum_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    elif text == '-':
        bot.register_next_step_handler(msg, sub_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
    elif text == '*':
        bot.register_next_step_handler(msg, mult_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите умножаемое и множитель')
    elif text == '/':
        bot.register_next_step_handler(msg, div_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите делимое и делитель')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')

def is_complex(ex):
    flag = True if "j" in ex else False
    if flag:
        return complex(ex)
    return float(ex)


def sum_(msg):
    # a, b = msg.text.split()
    # if is_complex(a) or is_complex(b):
    a, b = map(is_complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')

def sub_(msg):
    # a, b = map(float, msg.text.split())
    a, b = map(is_complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')

def mult_(msg):
    # a, b = map(float, msg.text.split())
    a, b = map(is_complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {a * b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')

def div_(msg):
    # a, b = map(float, msg.text.split())
    a, b = map(is_complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a / b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')

# @bot.message_handler()
# def answer(msg: types.Message):
#     id_ = msg.from_user.id
#     text = msg.text
#     if len(dct[id_]) == 0:
#         if text.count('.') <= 1 and text.replace('.', '').isdigit():
#             dct[id_].append(float(text))
#             bot.send_message(chat_id=msg.from_user.id, text=f'Введите второе число')
#         else:
#             bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите число')
#     elif len(dct[id_]) == 1:
#         if text.count('.') <= 1 and text.replace('.', '').isdigit():
#             bot.send_message(chat_id=msg.from_user.id, text=f'Результат: {float(text) + dct[id_][0]}')
#             dct[id_].clear()
#         else:
#             bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите число')


bot.polling()