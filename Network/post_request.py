import requests

url = 'https://randomall.ru/api/gens/1955'
x = requests.post(url)

print(x.text)
