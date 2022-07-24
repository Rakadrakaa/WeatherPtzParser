import telebot
from parser import send_tg

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, send_tg)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
