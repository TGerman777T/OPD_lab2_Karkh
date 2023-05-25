import telebot
from telebot import types
import random
import xlrd

def main():
    token = '6102435493:AAESrem46Un1_B06Zpapo9JvcIc9WuV-4VU'
    bot = telebot.TeleBot(token)

    rb = xlrd.open_workbook('вопросы.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("Правила")
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         'Приветствую! Предназначением данного бота является игра \"Кто хочет стать миллионером\".\nДля начала игры нажмите \"Начать игру\", а для прочтения правил игры нажмите \"Правила\".',
                         reply_markup=keyboard)

    @bot.message_handler(content_types=['text'])
    def func(message):
        if (message.text == "Начать игру" or message.text == "Начать заново"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            row = sheet.cell_value(0, 0)
            sampo = [1, 2, 3, 4]
            random.shuffle(sampo)
            wr1 = sheet.cell_value(0, 2)
            wr2 = sheet.cell_value(0, 3)
            wr3 = sheet.cell_value(0, 4)
            btn1 = types.KeyboardButton(sheet.cell_value(0, sampo[0]))
            btn2 = types.KeyboardButton(sheet.cell_value(0, sampo[1]))
            btn3 = types.KeyboardButton(sheet.cell_value(0, sampo[2]))
            btn4 = types.KeyboardButton(sheet.cell_value(0, sampo[3]))
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Первый вопрос:\n" + row, reply_markup=markup)
        elif (message.text == sheet.cell_value(0, 1)):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            row = sheet.cell_value(1, 0)
            sampo = [1, 2, 3, 4]
            random.shuffle(sampo)
            wr1 = sheet.cell_value(0, 2)
            wr2 = sheet.cell_value(0, 3)
            wr3 = sheet.cell_value(0, 4)
            btn1 = types.KeyboardButton(sheet.cell_value(1, sampo[0]))
            btn2 = types.KeyboardButton(sheet.cell_value(1, sampo[1]))
            btn3 = types.KeyboardButton(sheet.cell_value(1, sampo[2]))
            btn4 = types.KeyboardButton(sheet.cell_value(1, sampo[3]))
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Правильно! Второй вопрос:\n" + row, reply_markup=markup)
        elif (message.text == sheet.cell_value(1, 1)):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            row = sheet.cell_value(2, 0)
            sampo = [1, 2, 3, 4]
            random.shuffle(sampo)
            wr1 = sheet.cell_value(0, 2)
            wr2 = sheet.cell_value(0, 3)
            wr3 = sheet.cell_value(0, 4)
            btn1 = types.KeyboardButton(sheet.cell_value(2, sampo[0]))
            btn2 = types.KeyboardButton(sheet.cell_value(2, sampo[1]))
            btn3 = types.KeyboardButton(sheet.cell_value(2, sampo[2]))
            btn4 = types.KeyboardButton(sheet.cell_value(2, sampo[3]))
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Правильно! Третий вопрос:\n" + row, reply_markup=markup)
        elif (message.text == sheet.cell_value(2, 1)):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            row = sheet.cell_value(3, 0)
            sampo = [1, 2, 3, 4]
            random.shuffle(sampo)
            wr1 = sheet.cell_value(0, 2)
            wr2 = sheet.cell_value(0, 3)
            wr3 = sheet.cell_value(0, 4)
            btn1 = types.KeyboardButton(sheet.cell_value(3, sampo[0]))
            btn2 = types.KeyboardButton(sheet.cell_value(3, sampo[1]))
            btn3 = types.KeyboardButton(sheet.cell_value(3, sampo[2]))
            btn4 = types.KeyboardButton(sheet.cell_value(3, sampo[3]))
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Правильно! Четвёртый вопрос:\n" + row, reply_markup=markup)
        elif (message.text == sheet.cell_value(3, 1)):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            row = sheet.cell_value(4, 0)
            sampo = [1, 2, 3, 4]
            random.shuffle(sampo)
            wr1 = sheet.cell_value(0, 2)
            wr2 = sheet.cell_value(0, 3)
            wr3 = sheet.cell_value(0, 4)
            btn1 = types.KeyboardButton(sheet.cell_value(4, sampo[0]))
            btn2 = types.KeyboardButton(sheet.cell_value(4, sampo[1]))
            btn3 = types.KeyboardButton(sheet.cell_value(4, sampo[2]))
            btn4 = types.KeyboardButton(sheet.cell_value(4, sampo[3]))
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Правильно! Пятый вопрос:\n" + row, reply_markup=markup)
        elif (message.text == sheet.cell_value(4, 1)):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Начать заново")
            btn2 = types.KeyboardButton("Правила")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="🎉Поздравляю, вы победили!🎉", reply_markup=markup)
        elif (message.text == sheet.cell_value(0, 2) or
        message.text == sheet.cell_value(0, 3) or
        message.text == sheet.cell_value(0, 4) or
        message.text == sheet.cell_value(1, 2) or
        message.text == sheet.cell_value(1, 3) or
        message.text == sheet.cell_value(1, 4) or
        message.text == sheet.cell_value(2, 2) or
        message.text == sheet.cell_value(2, 3) or
        message.text == sheet.cell_value(2, 4) or
        message.text == sheet.cell_value(3, 2) or
        message.text == sheet.cell_value(3, 3) or
        message.text == sheet.cell_value(3, 4) or
        message.text == sheet.cell_value(4, 2) or
        message.text == sheet.cell_value(4, 3) or
        message.text == sheet.cell_value(4, 4)):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Начать заново")
            btn2 = types.KeyboardButton("Правила")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="К сожалению, это был неправильный ответ! Хотите попробовать снова или прочитать правила?", reply_markup=markup)
        elif (message.text == "Правила"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            bot.send_message(message.chat.id, 'Игра Кто хочет стать миллионером? - это конкурс викторина, в котором участники должны правильно ответить на ряд вопросов с несколькими вариантами ответов, чтобы перейти на следующий уровень. Всего 5 вопросов.', reply_markup=markup)
        elif (message.text == "Вернуться в главное меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Начать игру")
            button2 = types.KeyboardButton("Правила")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован...")

    bot.polling(none_stop=True)