import requests

# https://api.github.com/search/repositories?q=language:python&sort=stars
# Отсюда брали API данные

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Сохранение ответа API в переменной.
response_dict = r.json()

# Обработка результатов
print(response_dict.keys())