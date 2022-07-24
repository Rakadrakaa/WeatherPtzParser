import telebot
from parser import send_tg

bot = telebot.TeleBot('5449903974:AAH6E3-sgSSDVlw49eUA3W0zhbYUkiTGiXQ')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, send_tg)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
