import requests
import telebot

URL = 'https://randomall.ru/api/general/unexpected_event'
x = requests.post(URL)

print(x.text)
