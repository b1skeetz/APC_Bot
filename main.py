import telebot
from telebot import types
import mysql.connector

COUNT = 0

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='IosifStalin2',
    port='3306',
    database='pythonbot'
)

bot = telebot.TeleBot('5515564481:AAHyZdFrYrJv_uoKj3Z3zZyCyTvuZbe_9pU')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    butRu = types.KeyboardButton('Ru')
    butKz = types.KeyboardButton('Kz')
    markup.add(butRu, butKz)
    bot.send_message(message.chat.id, "Выберите язык/Тілді таңдаңыз", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def choose_specialize(message):
    # ОСНОВНЫЕ КНОПКИ МЕНЮ
    global COUNT
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
    elif message.text == "Мамандықтарды таңдау":
        bot.send_message(message.chat.id, "#APC2022 қабылдау: біздің мамандықтар \n"
                                          "1. Бағдарламалық қамтамасыздандыруды құрастырушысы \n"
                                          "2. Ақпараттық жүйелер технигі \n"
                                          "3. Ақпараттық қауіпсіздік жүйелері \n"
                                          "4. Радиотехника, электроника және телекоммуникациялар \n"
                                          "5. Дизайн, азаматтық ғимараттарды жобалау, қалпына келтіру, қайта құру \n"
                                          "6. Ғимараттар мен құрылыстарды салу және пайдалану \n"
                                          "7. Газбен қамтамасыз ету жабдықтары мен жүйелерін құрастыру және пайдалану \n"
                                          "8. Автомобиль көлігіне техникалық қызмет көрсету, жөндеу және пайдалану \n"
                                          "9. Қонақ үй бизнесі \n"
                                          "10. Туризм \n"
                                          "11. Учет и аудит", parse_mode='html')
        photo = open('pic\entrance\поступление1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "#APC2022-ге кіру оңай, негізгі ережелер. "
                                          "Қабылдау емтихандары жоқ. Мен құжаттарды және бәрін тапсырдым. «аттестаттар шайқасының» нәтижесін> күтесіз.",
                         parse_mode='html')
    elif message.text == "Вернуться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        chooseProfession = types.KeyboardButton('Выбор специальностей')
        #studentsList = types.KeyboardButton('Списки абитуриентов')
        specialize = types.KeyboardButton('Специальности')
        adaptation = types.KeyboardButton('Все для адаптации')
        howToEntry = types.KeyboardButton('Как поступить?')
        language = types.KeyboardButton('Сменить язык')
        markup.add(chooseProfession, specialize, adaptation, howToEntry, language)
        bot.send_message(message.chat.id, 'Главная страница', reply_markup=markup)

    elif message.text == "Сменить язык":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        chooseProfession = types.KeyboardButton('Мамандықтарды таңдау')
        # studentsList = types.KeyboardButton('Талапкерлер тізімі')
        specialize = types.KeyboardButton('Мамандықтар')
        adaptation = types.KeyboardButton('Барлығы бейімделу үшін')
        howToEntry = types.KeyboardButton('Қалай түсуге болады?')
        language = types.KeyboardButton('Тілді өзгерту')
        markup.add(chooseProfession, specialize, adaptation, howToEntry, language)
        bot.send_message(message.chat.id,
                         'Басты бет',
                         reply_markup=markup)
    elif message.text == "Тілді өзгерту":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        chooseProfession = types.KeyboardButton('Выбор специальностей')
        #studentsList = types.KeyboardButton('Списки абитуриентов')
        specialize = types.KeyboardButton('Специальности')
        adaptation = types.KeyboardButton('Все для адаптации')
        howToEntry = types.KeyboardButton('Как поступить?')
        language = types.KeyboardButton('Сменить язык')
        markup.add(chooseProfession, specialize, adaptation, howToEntry, language)
        bot.send_message(message.chat.id, 'Главная страница', reply_markup=markup)

    elif message.text == "Оралу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        chooseProfession = types.KeyboardButton('Мамандықтарды таңдау')
       # studentsList = types.KeyboardButton('Талапкерлер тізімі')
        specialize = types.KeyboardButton('Мамандықтар')
        adaptation = types.KeyboardButton('Барлығы бейімделу үшін')
        howToEntry = types.KeyboardButton('Қалай түсуге болады?')
        language = types.KeyboardButton('Тілді өзгерту')
        markup.add(chooseProfession, specialize, adaptation, howToEntry, language)
        bot.send_message(message.chat.id,
                         'Басты бет',
                         reply_markup=markup)

    elif message.text == "Специальности":
        bot.send_message(message.chat.id,
                         "У нас в колледже есть различные специальности! Чтобы увидеть информацию, выберите кнопку с соотвутствующей специальностью.",
                         parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        design = types.KeyboardButton('дизайнеры')
        builders = types.KeyboardButton('строители')
        tourism = types.KeyboardButton('туристы')
        progers = types.KeyboardButton('программисты')
        infsys = types.KeyboardButton('информационные системы')
        infsec = types.KeyboardButton('информационная безопасность')
        con = types.KeyboardButton('связисты')
        gas = types.KeyboardButton('газовики')
        vehicle = types.KeyboardButton('механики')
        hotel = types.KeyboardButton('гостиничный бизнес')
        econom = types.KeyboardButton('экономисты')
        back = types.KeyboardButton('Вернуться')
        markup.add(design, builders, tourism, progers, infsys, infsec, con, gas, vehicle, hotel, econom, back)
        bot.send_message(message.chat.id, 'Просмотрите списки профессий', reply_markup=markup)

    elif message.text == "Мамандықтар":
        bot.send_message(message.chat.id,
                         "Біздің колледжде әртүрлі мамандықтар бар! Ақпаратты көру үшін тиісті мамандығы бар түймені таңдаңыз.",
                         parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        design = types.KeyboardButton('дизайнерлер')
        builders = types.KeyboardButton('құрылысшылар')
        tourism = types.KeyboardButton('туристер')
        progers = types.KeyboardButton('бағдарламашылар')
        infsys = types.KeyboardButton('ақпараттық жүйелер')
        infsec = types.KeyboardButton('ақпараттық қауіпсіздік')
        con = types.KeyboardButton('байланысшылар')
        gas = types.KeyboardButton('газшылар')
        vehicle = types.KeyboardButton('механиктар')
        hotel = types.KeyboardButton('қонақ үй бизнесі')
        econom = types.KeyboardButton('экономистер')
        back = types.KeyboardButton('Оралу')
        markup.add(design, builders, tourism, progers, infsys, infsec, con, gas, vehicle, hotel, econom, back)
        bot.send_message(message.chat.id, 'Мамандықтар тізімін қарап шығыңыз', reply_markup=markup)

    elif message.text == "Ru":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        chooseProfession = types.KeyboardButton('Выбор специальностей')
        #studentsList = types.KeyboardButton('Списки абитуриентов')
        specialize = types.KeyboardButton('Специальности')
        adaptation = types.KeyboardButton('Все для адаптации')
        howToEntry = types.KeyboardButton('Как поступить?')
        language = types.KeyboardButton('Сменить язык')
        markup.add(chooseProfession, specialize, adaptation, howToEntry, language)
        bot.send_message(message.chat.id,
                         'Здравствуй, дорогой абитуриент! Это специальный бот для предоставления информации недавно поступившим студентам и абитуриентам.',
                         reply_markup=markup)
    elif message.text == "Kz":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        chooseProfession = types.KeyboardButton('Мамандықтарды таңдау')
       # studentsList = types.KeyboardButton('Талапкерлер тізімі')
        specialize = types.KeyboardButton('Мамандықтар')
        adaptation = types.KeyboardButton('Барлығы бейімделу үшін')
        howToEntry = types.KeyboardButton('Қалай түсуге болады?')
        language = types.KeyboardButton('Тілді өзгерту')
        markup.add(chooseProfession, specialize, adaptation, howToEntry, language)
        bot.send_message(message.chat.id,
                         'Сәлем, қымбатты талапкер! Бұл жақында қабылданған студенттер мен талапкерлерге ақпарат беруге арналған арнайы бот.',
                         reply_markup=markup)
    elif message.text == "Все для адаптации":
        bot.send_message(message.chat.id,
                         "Я помогу тебе адаптироваться к студенческой жизни, понажимай на кнопки, там много интересной информации!",
                         parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        marks = types.KeyboardButton('Система оценок')
        rings = types.KeyboardButton('Звонки')
        buildings = types.KeyboardButton('Корпуса')
        cabinet = types.KeyboardButton('Как найти аудиторию?')
        back = types.KeyboardButton('Вернуться')
        markup.add(marks, rings, buildings, cabinet, back)
        bot.send_message(message.chat.id, 'Кнопки доступны в меню!', reply_markup=markup)

    elif message.text == "Барлығы бейімделу үшін":
        bot.send_message(message.chat.id,
                         "Мен сізге студенттік өмірге бейімделуге көмектесемін, батырмаларды басыңыз, көптеген қызықты ақпарат бар!",
                         parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        marks = types.KeyboardButton('Бағалау жүйесі')
        rings = types.KeyboardButton('Қоңыраулар')
        buildings = types.KeyboardButton('Корпустар')
        cabinet = types.KeyboardButton('Аудиторияны қалай табуға болады?')
        back = types.KeyboardButton('Оралу')
        markup.add(marks, rings, buildings, cabinet, back)
        bot.send_message(message.chat.id, 'Түймелер мәзірде қол жетімді!', reply_markup=markup)

    elif message.text == "Как поступить?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        marks = types.KeyboardButton('Список основных документов')
        rings = types.KeyboardButton('Расчет конкурсных баллов')
        back = types.KeyboardButton('Вернуться')
        markup.add(marks, rings, back)
        bot.send_message(message.chat.id, 'Кнопки доступны в меню!', reply_markup=markup)

    elif message.text == "Қалай түсуге болады?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        marks = types.KeyboardButton('Негізгі құжаттар тізімі')
        rings = types.KeyboardButton('Конкурстық балдарды есептеу')
        back = types.KeyboardButton('Оралу')
        markup.add(marks, rings, back)
        bot.send_message(message.chat.id, 'Түймелер мәзірде қол жетімді!', reply_markup=markup)

    elif message.text == "Списки абитуриентов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        marks = types.KeyboardButton('Выбрать специальность!')
        back = types.KeyboardButton('Вернуться')
        markup.add(marks, back)
        bot.send_message(message.chat.id, 'Кнопки доступны в меню!', reply_markup=markup)

    elif message.text == "Талапкерлер тізімі":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        marks = types.KeyboardButton('Мамандық таңдаңыз!')
        back = types.KeyboardButton('Оралу')
        markup.add(marks, back)
        bot.send_message(message.chat.id, 'Түймелер мәзірде қол жетімді!', reply_markup=markup)

    # СПИСКИ АБИТУРИЕНТОВ
    elif message.text == "Выбрать специальность!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        design = types.KeyboardButton('дизайнеры_2022')
        builders = types.KeyboardButton('строители_2022')
        tourism = types.KeyboardButton('туристы_2022')
        progers = types.KeyboardButton('программисты_2022')
        infsys = types.KeyboardButton('информационные системы_2022')
        infsec = types.KeyboardButton('информационная безопасность_2022')
        con = types.KeyboardButton('связисты_2022')
        gas = types.KeyboardButton('газовики_2022')
        vehicle = types.KeyboardButton('механики_2022')
        hotel = types.KeyboardButton('гостиничный бизнес_2022')
        econom = types.KeyboardButton('экономисты_2022')
        back = types.KeyboardButton('Вернуться')
        markup.add(design, builders, tourism, progers, infsys, infsec, con, gas, vehicle, hotel, econom, back)
        bot.send_message(message.chat.id, 'Просмотрите списки профессий', reply_markup=markup)

    elif message.text == "Мамандық таңдаңыз!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        design = types.KeyboardButton('дизайнерлер_2022')
        builders = types.KeyboardButton('құрылысшылар_2022')
        tourism = types.KeyboardButton('туристер_2022')
        progers = types.KeyboardButton('бағдарламашылар_2022')
        infsys = types.KeyboardButton('ақпараттық жүйелер_2022')
        infsec = types.KeyboardButton('ақпараттық қауіпсіздік_2022')
        con = types.KeyboardButton('байланысшылар_2022')
        gas = types.KeyboardButton('газшылар_2022')
        vehicle = types.KeyboardButton('механиктер_2022')
        hotel = types.KeyboardButton('қонақ үй бизнесі_2022')
        econom = types.KeyboardButton('экономистер_2022')
        back = types.KeyboardButton('Оралу')
        markup.add(design, builders, tourism, progers, infsys, infsec, con, gas, vehicle, hotel, econom, back)
        bot.send_message(message.chat.id, 'Мамандықтар тізімін қарап шығыңыз', reply_markup=markup)

    elif message.text == "дизайнеры_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "строители_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "туристы_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "программисты_2022":
        bot.send_message(message.chat.id, 'Введите фамилию')
        COUNT += 1
    elif COUNT == 1:
        stre = message.text
        print(stre)
        count = 0

        mycursor = mydb.cursor()

        mycursor.execute('select * from users order by scorefull desc, scoreprof desc')

        users = mycursor.fetchall()

        for user in users:
            count += 1
            if user[1] == stre:
                messageStr = "Ты находишься на " + str(count) + " месте"
                bot.send_message(message.chat.id, messageStr)

    elif message.text == "информационные системы_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "информационная безопасность_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "связисты_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "газовики_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "механики_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "гостиничный бизнес_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "экономисты_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')


    # кз
    elif message.text == "дизайнерлер_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "құрылысшылар_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "туристер_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "бағдарламашылар_2022":
        bot.send_message(message.chat.id, 'Фамилияңызды енгізіңіз')
        COUNT += 1
    elif COUNT == 1:
        stre = message.text
        print(stre)
        count = 0

        mycursor = mydb.cursor()

        mycursor.execute('select * from users order by scorefull desc, scoreprof desc')

        users = mycursor.fetchall()

        for user in users:
            count += 1
            if user[1] == stre:
                messageStr = "Сіз " + str(count) + "-орындасыз."
                bot.send_message(message.chat.id, messageStr)

    elif message.text == "ақпараттық жүйелер_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "ақпараттық қауіпсіздік_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "байланысшылар_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "газшылар_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "механиктер_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "қонақ үй бизнесі_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')
    elif message.text == "экономистер_2022":
        bot.send_message(message.chat.id, 'Находится в разработке =)')

    # КНОПКИ ДЛЯ ВЫБОРА СПЕЦИАЛЬНОСТЕЙ
    elif message.text == "дизайнеры":
        photo = open('pic\graduates info\design.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\graduates info\дизайнер.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "строители":
        photo = open('pic\graduates info\guilder.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\graduates info\строитель1.png', 'rb')
        photo1 = open('pic\graduates info\строитель2.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1)
    elif message.text == "туристы":
        photo = open('pic\graduates info\dourism.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\graduates info\туризм1.png', 'rb')
        photo1 = open('pic\graduates info\туризм2.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1)
    elif message.text == "программисты":
        photo = open('pic\graduates info\progers.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "информационные системы":
        photo = open('pic\graduates info\infsys.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "информационная безопасность":
        photo = open('pic\graduates info\infsec.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "связисты":
        photo = open('pic\graduates info\cadio.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "газовики":
        photo = open('pic\graduates info\gas.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "механики":
        photo = open('pic\graduates info\mashina.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "гостиничный бизнес":
        photo = open('pic\graduates info\ogh.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "экономисты":
        photo = open('pic\graduates info\econom.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)


    # КНОПКИ ДЛЯ ВЫБОРА СПЕЦИАЛЬНОСТЕЙ на казахском
    elif message.text == "дизайнерлер":
        photo = open('pic\peticlkz\design.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\graduates info\дизайнер.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "құрылысшылар":
        photo = open('pic\peticlkz\guilder.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\graduates info\строитель1.png', 'rb')
        photo1 = open('pic\graduates info\строитель2.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1)
    elif message.text == "туристер":
        photo = open('pic\graduates info\dourism.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\graduates info\туризм1.png', 'rb')
        photo1 = open('pic\graduates info\туризм2.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1)
    elif message.text == "бағдарламашылар":
        photo = open('pic\peticlkz\progers.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "ақпараттық жүйелер":
        photo = open('pic\peticlkz\infsys.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "ақпараттық қауіпсіздік":
        photo = open('pic\peticlkz\infsec.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "байланысшылар":
        photo = open('pic\peticlkz\cadio.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "газшылар":
        photo = open('pic\graduates info\gas.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "механиктар":
        photo = open('pic\peticlkz\mashina.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "қонақ үй бизнесі":
        photo = open('pic\peticlkz\ogh.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "экономистер":
        photo = open('pic\graduates info\econom.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

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

    elif message.text == "Бағалау жүйесі":
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

    elif message.text == "Қоңыраулар":
        photo = open('pic\Odaptation\online.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\Odaptation\offline.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Үлкен үзіліс 2-ші және 5-ші парадан кейін 30 минуттан.",
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

    elif message.text == "Корпустар":
        photo = open('pic\Odaptation\corp.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Асханаларды орналастыру:\n"
                         "1 ғимарат – подвал кіреберістің оң жағында\n"
                         "2 ғимарат – кіреберіс жағынан дәліз бойымен солға қарай\n"
                         "Столоffка - жолдың арғы жағында 2 корпустың артында",
                         parse_mode='html')

    elif message.text == "Как найти аудиторию?":
        photo = open('pic\Odaptation\cabkaz.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Произносится сначала первое число из двух цифр, потом второе: 23|18 - двадцать три восемнадцать ",
                         parse_mode='html')

    elif message.text == "Аудиторияны қалай табуға болады?":
        photo = open('pic\Odaptation\cabrus.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Екі цифрдың бірінші саны алдымен айтылады, содан кейін екіншісі: 23 | 18 - жиырма үш он сегіз",
                         parse_mode='html')

    # КАК ПОСТУПИТЬ?
    elif message.text == "Список основных документов":
        photo = open('pic\entrance\docs.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Документы можно сдать как оффлайн, так и онлайн!"
                         "Telegram-бот приемной комиссии - http://t.me/GoAstanaPolytechBot",
                         parse_mode='html')

    elif message.text == "Негізгі құжаттар тізімі":
        photo = open('pic\entrance\docskaz.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Құжаттарды офлайн және онлайн түрде жіберуге болады!"
                         "Қабылдау комиссиясының Telegram боты - http://t.me/GoAstanaPolytechBot",
                         parse_mode='html')

    elif message.text == "Расчет конкурсных баллов":
        photo = open('pic\entrance\srball.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\entrance\srballdesign.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Приоритетные баллы - баллы по профильным предметам!\n"
                         "Telegram-бот приемной комиссии - http://t.me/GoAstanaPolytechBot",
                         parse_mode='html')

    elif message.text == "Конкурстық балдарды есептеу":
        photo = open('pic\entrance\srball.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo = open('pic\entrance\srballdesign.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         "Басымдық ұпайлар – негізгі пәндер бойынша ұпайлар!\n"
                         "Қабылдау комиссиясының Telegram боты - http://t.me/GoAstanaPolytechBot",
                         parse_mode='html')

    elif message.text == "Вернуться":
        Ru(message)

    elif message.text == "Оралу":
        Kz(message)

    else:
        bot.send_message(message.chat.id, f'Убедитесь, что команда введена верно!', parse_mode='html')


bot.polling(none_stop=True)