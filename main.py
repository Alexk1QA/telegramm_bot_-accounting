import telebot
from telebot import types
global mess

bot = telebot.TeleBot('5371438553:AAHE4kA1YNX_f6VhRh4bAQ3fKMqwtIBBgAk')


@bot.message_handler(commands=['start'])
def start(message):
    global mess
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Расходы")
    item2 = types.KeyboardButton("Доходы")
    markup.add(item1, item2)

    name = message.from_user.first_name
    if name != "None":
        mess = f"Привет {message.from_user.last_name}"

    lastname = message.from_user.last_name
    if lastname != "None":
        mess = f"Привет {message.from_user.first_name}"

    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler()
def info(message):
    if message.text == "Расходы":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Проезд", callback_data='travel')
        item2 = types.InlineKeyboardButton("Обед", callback_data='dinner')
        item3 = types.InlineKeyboardButton("Магазин", callback_data='shop')
        item4 = types.InlineKeyboardButton("Машина", callback_data='car')

        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, "Выбери категорию расходов", reply_markup=markup)

    elif message.text == "Доходы":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Зарплата 🎉", callback_data='salary')
        item2 = types.InlineKeyboardButton("Подработка", callback_data='time_job')

        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Выбери категорию доходов", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'travel':
                bot.send_message(call.message.chat.id, "Укажи сумму расхода")
            elif call.data == 'dinner':
                bot.send_message(call.message.chat.id, "Укажи сумму расхода")
            elif call.data == 'shop':
                bot.send_message(call.message.chat.id, "Укажи сумму расхода")
            elif call.data == 'salary':
                bot.send_message(call.message.chat.id, "Укажи сумму дохода")
            elif call.data == 'time_job':
                bot.send_message(call.message.chat.id, "Укажи сумму дохода")

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)