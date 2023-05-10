import telebot

bot = telebot.TeleBot('6263478357:AAEjFZN2nXCLxk4LUfr_EZX_GIlKAJ_cI5k')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


bot.polling(none_stop=True)
