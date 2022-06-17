import telebot
from telebot import types

bot = telebot.TeleBot('5515564481:AAHyZdFrYrJv_uoKj3Z3zZyCyTvuZbe_9pU')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://google.com"))
    bot.send_message(message.chat.id, 'Перейдите на сайт...', reply_markup=markup)


@bot.message_handler(commands=['start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    makrs = types.KeyboardButton('Система оценивания')
    stages = types.KeyboardButton('Старт')

    markup.add(makrs, stages)
    bot.send_message(message.chat.id, 'Бот готов к работе!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Система оценивания":
        photo = open('pic\stages.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    else:
        bot.send_message(message.chat.id, f'Убедитесь, что команда введена верно!', parse_mode='html')


bot.polling(none_stop=True)
