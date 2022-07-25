# TODO: Прикрутить телеграмм бота
from bs4 import BeautifulSoup
import requests
import csv


url = 'http://pogoda-karelia.ru/'
response = requests.get(url)

bs = BeautifulSoup(response.text, 'lxml')


title_dis = bs.find('h4', class_='title')  # Получение названия района
temp = bs.find('span', class_="t-value")  # Получение температуры
date = bs.find('h5', class_="date")  # Получение даты
time = bs.find('h5', class_="time")  # Получение времени

title_dis = title_dis.text
temp = temp.text
date = date.text
time = time.text

print(
    f'Район {title_dis}',
    f'Текущая температура {temp} градусов по Цельсию',
    f'Дата {date} г.',
    f'Время {time}', sep='\n')

with open("weather.csv", mode="a", encoding='utf-8') as w_file:
    headers = ["Район", "Температура", "Дата", "Время"]
    file_writer = csv.DictWriter(w_file, delimiter=",",
                                 lineterminator="\r", fieldnames=headers)
    file_writer.writerow(
        {'Район': title_dis, 'Температура': temp, 'Дата': date, 'Время': time})


file_writer = csv.writer(w_file, delimiter="\t")
