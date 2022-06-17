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
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    chooseProfession = types.KeyboardButton('Выбор специальностей')
    specialize = types.KeyboardButton('Специальности')
    adaptation = types.KeyboardButton('Все для адаптации')
    howToEntry = types.KeyboardButton('Как поступить?')
    markup.add(chooseProfession, specialize, adaptation, howToEntry)
    bot.send_message(message.chat.id, 'Привет тебе, дорогой абитуриент! Это главное мое меню, можешь ознакомиться со всеми моими возможностями прямо тут! ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def choose_specialize(message):
    #ОСНОВНЫЕ КНОПКИ МЕНЮ
    if message.text == "Выбор специальностей":
        bot.send_message(message.chat.id, "Поступление в #APC2022 : наши специальности: \n"
                                      "1. Программное обеспечение (Разработчик ПО) \n"
                                      "2. Программное обеспечение (Техник информационных систем) \n"
                                      "3. Системы информационной безопасности \n"
                                      "4. Радиотехника, электроника и телекоммуникации \n"
                                      "5. Дизайн, реставрация и реконструкция гражданских зданий \n"
                                      "6. Строительство и эксплуатация зданий и сооружений \n"
                                      "7. Монтаж и эксплуатация оборудования и систем газоснабжения \n"
                                      "8. Техническое обслуживание, ремонт и эксплуатация автомобильного транспорта \n"
                                      "9. Гостиничный бизнес \n"
                                      "10. Туризм \n"
                                      "11. Учет и аудит", parse_mode='html')
        photo = open('pic\entrance\поступление1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Поступление в #APC2022 стало проще, основные правила. "
                                         "Вступительных экзаменов нет. Сдал документы и все. Ждешь результатов «битвы аттестатов».",
                        parse_mode='html')
    elif message.text == "Специальности":
        bot.send_message(message.chat.id,
                         "У нас в колледже есть различные специальности! Чтобы увидеть информацию, выберите кнопку с соотвутствующей специальностью.",
                         parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        design = types.KeyboardButton('дизайнеры')
        builders = types.KeyboardButton('строители')
        tourism = types.KeyboardButton('туристы')
        back = types.KeyboardButton('Назад')
        markup.add(design, builders, tourism, back)
        bot.send_message(message.chat.id, 'Просмотрите списки профессий', reply_markup=markup)
    elif message.text == "Все для адаптации":
        bot.send_message(message.chat.id,
                         "Я помогу тебе адаптироваться к студенческой жизни, понажимай на кнопки, там много интересной информации!",
                         parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        marks = types.KeyboardButton('Система оценок')
        rings = types.KeyboardButton('Звонки')
        buildings = types.KeyboardButton('Корпуса')
        cabinet = types.KeyboardButton('Как найти аудиторию?')
        back = types.KeyboardButton('Назад')
        markup.add(marks, rings, buildings, cabinet, back)
        bot.send_message(message.chat.id, 'Кнопки доступны в меню!', reply_markup=markup)
    elif message.text == "Как поступить?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        marks = types.KeyboardButton('Список основных документов')
        rings = types.KeyboardButton('text')
        buildings = types.KeyboardButton('text')
        cabinet = types.KeyboardButton('text')
        back = types.KeyboardButton('Назад')
        markup.add(marks, rings, buildings, cabinet, back)
        bot.send_message(message.chat.id, 'Кнопки доступны в меню!', reply_markup=markup)


    # КНОПКИ ДЛЯ ВЫБОРА СПЕЦИАЛЬНОСТЕЙ
    elif message.text == "дизайнеры":
        photo = open('pic\graduates info\дизайнер.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "строители":
        photo = open('pic\graduates info\строитель1.png', 'rb')
        photo1 = open('pic\graduates info\строитель2.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1)
    elif message.text == "туристы":
        photo = open('pic\graduates info\туризм1.png', 'rb')
        photo1 = open('pic\graduates info\туризм2.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1)


    # ГЛАВНОЕ МЕНЮ
    elif message.text == "Поступление в #APC2022 на бесплатное обучение":
        photo = open('pic\entrance\грант.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                            "Возникает вопрос: все ли поступят на бесплатное обучение? Если поступающих больше, чем по госзаказу - зачисление осуществляется на основе среднего конкурсного балла по основным и профильным предметам, по среднему баллу аттестата, а также квоте.",
                            parse_mode='html')

    # АДАПТАЦИЯ
    elif message.text == "Система оценок":
        photo = open('pic\Odaptation\marks.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "3 - 50-69\n"
                         "4 - 70-89\n"
                         "5 - 90-100",
                         parse_mode='html')
    elif message.text == "Звонки":
        photo = open('pic\Odaptation\online.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\Odaptation\offline.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Большая перемена 30 минут после 2 и 5 пары.",
                         parse_mode='html')

    elif message.text == "Корпуса":
        photo = open('pic\Odaptation\corp.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Размещение столовых:\n"
                         "1 корпус - подвал с правой стороны от входа\n"
                         "2 корпус - налево по корридору от входа\n"
                         "Столоffка - через дорогу позади 2 корпуса.",
                         parse_mode='html')
    elif message.text == "Как найти аудиторию?":
        photo = open('pic\Odaptation\cabkaz.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\Odaptation\cabrus.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Произносится сначала первое число из двух цифр, потом второе: 23|18 - двадцать три восемнадцать ",
                         parse_mode='html')

    # КАК ПОСТУПИТЬ?
    elif message.text == "Список основных документов":
        photo = open('pic\entrance\docs.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\entrance\docskaz.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Документы можно сдать как оффлайн, так и онлайн!"
                         "Telegram-бот приемной комиссии - http://t.me/GoAstanaPolytechBot",
                         parse_mode='html')


    elif message.text == "Назад":
        start(message)
    else:
        bot.send_message(message.chat.id, f'Убедитесь, что команда введена верно!', parse_mode='html')







bot.polling(none_stop=True)
