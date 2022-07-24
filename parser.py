from bs4 import BeautifulSoup
import requests

url = 'http://pogoda-karelia.ru/'
response = requests.get(url)

bs = BeautifulSoup(response.text, 'lxml')


title_dis = bs.find('h4', class_='title')  # Получение названия района
temp = bs.find('span', class_="t-value")  # Получение температуры
date = bs.find('h5', class_="date")  # Получение даты
time = bs.find('h5', class_="time")  # Получение времени


print(
    f'Район {title_dis.text}',
    f'Текущая температура {temp.text} градусов по Цельсию',
    f'Дата {date.text} г.',
    f'Время {time.text}', sep='\n')
