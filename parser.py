from bs4 import BeautifulSoup
import requests
import csv
import telebot

bot = telebot.TeleBot(
    '5449903974:AAH6E3-sgSSDVlw49eUA3W0zhbYUkiTGiXQ')  # API бота

url = 'http://pogoda-karelia.ru/'  # Ссылка на сайт
response = requests.get(url)

bs = BeautifulSoup(response.text, 'lxml')

title_dis = bs.find('h4', class_='title').text  # Получение названия района
temp = bs.find('span', class_="t-value").text  # Получение температуры
date = bs.find('h5', class_="date").text  # Получение даты
time = bs.find('h5', class_="time").text  # Получение времени

# Данные по погоде для бота
tg_weather = 'Район: ' + title_dis + '\nТемпература: ' + \
    temp + '\nДата: ' + date + '\nВремя: ' + time


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, показать погоду?')


@bot.message_handler(content_types=['text'])
def send_weather(message):
    bot.send_message(message.chat.id, "Погода на сейчас: ")
    bot.send_message(message.chat.id, tg_weather)


if __name__ == '__main__':
    bot.infinity_polling()


with open("weather.csv", mode="a", encoding='utf-8') as w_file:  # Запись рез. парсинга в csv файл
    headers = ["District", "Temperatue", "Date", "Time"]
    file_writer = csv.DictWriter(w_file, delimiter=",",
                                 lineterminator="\r", fieldnames=headers)
    file_writer.writerow(
        {'District': title_dis, 'Temperatue': temp, 'Date': date, 'Time': time})

    file_writer = csv.writer(w_file, delimiter="\t")
