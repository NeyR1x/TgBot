import telebot
from telebot import types

bot = telebot.TeleBot('5274440057:AAHN-kRiYFtmA90WJvPtJ0ajlPSwiuEuKUk')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("МТУСИ", "youtube", "Котики")
    bot.send_message(message.chat.id,
                     "Привет, я бот Zhdan_Artyom_Bot!\nИспользуйте команду '/help', чтобы узнать возможности бота!",
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.reply_to(message,
                 "Отправьте сообщение, либо используйте кнопку:\n\n'МТУСИ' чтобы получить ссылку на сайт "
                 "университета\n'youtube' "
                 "чтобы получить ссылку видеохостинга yotube\n"
                 "'Котики' чтобы получить фотографию котика\n\n"
                 "Список команд бота:\n\n"
                 "/cat - получить фотографию кота\n"
                 "/dog - получить фотографию собаки\n"
                 "/help - информация о возможностях бота")


@bot.message_handler(commands=['cat'])
def start_message(message):
    bot.send_photo(message.chat.id,'https://lifehacker.ru/wp-content/uploads/2018/12/Kak-fotografirovat-kotikov-19'
                                   '-sovetov-ot-professionala_1544744286.jpg')


@bot.message_handler(commands=['dog'])
def start_message(message):
    bot.send_photo(message.chat.id,'https://cdnn21.img.ria.ru/images/07e4/02/1a/1565220007_0:0:2986'
                                   ':1681_1920x0_80_0_0_329e068fc6fa170ddccb8ff7e34717c1.jpg')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'мтуси':
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "youtube":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://www.youtube.com/')
    if message.text.lower() == "котики":
        bot.send_message(message.chat.id,'Тогда тебе сюда – https://pixabay.com/ru/images/search/%D0%BA%D0%BE%D1%82'
                                         '%D1%8F%D1%82%D0%B0/')


bot.polling()
