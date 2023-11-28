import telebot

bot = telebot.TeleBot('6457402606:AAEkP74EP7wOZO3bNY96lqVlv6M8IYEmR2w')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет друг. Хочешь получить от меня шутку, введи команду: */joke*. \n А так же можешь написать: */more_joke*',
                     parse_mode='Markdown')


@bot.message_handler(commands=['joke'])
def main(message):
    bot.send_message(message.chat.id,
                     'Программист звонит в библиотеку.\n— Здравствуйте, Катю можно?\n— Она в архиве.\n— Разархивируйте ее пожалуйста. Она мне срочно нужна!')


@bot.message_handler(commands=['more_joke'])
def main(message):
    bot.send_message(message.chat.id, '[Ссылка на авторские шутки](https://anekdoty.ru/pro-programmistov/)',
                     parse_mode='Markdown')


bot.infinity_polling()