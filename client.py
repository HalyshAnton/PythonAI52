# код для клієнета
# який спілкується з сервером

import requests

# # виклик функції message на сервері
# response = requests.post("http://localhost:8000/message")
# print(response.status_code)  # чи вдався запит(код 200)
#
# # виклик функції func на сервері
# requests.post("http://localhost:8000/function")

# отримати дані від сервера
num = 24
response = requests.post(f"http://localhost:8000/mult2/{num}")

# якщо запит успішний
if response.ok:
    # отримати відповідь від сервера у json форматі
    data = response.json()
    print(data)
else:
    #виникла помилка
    print(response.text)