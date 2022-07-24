from operator import delitem    # TODO: Прикрутить телеграмм бота
from os import sep
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

file = ('weather_data.txt')

# Пиздец уебищный способ записи конечно, но я пока по другому не умею.
with open(file, 'a', encoding='utf-8') as f:
    f.write(title_dis)
    f.write('\n')
    f.write(temp)
    f.write('\n')
    f.write(date)
    f.write('\n')
    f.write(time)
    f.write('\n')
    f.write('-' * 10)
    f.write('\n')
