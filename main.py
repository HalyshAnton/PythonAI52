# серверне програмування

# https://www.google.com/search&q=java


from fastapi import FastAPI


# застосонук для сервера
# допомагає позначити як отримати доступ до окремих функцій на сервері

# коли робитиметься виклик до серверра
# http:our_ip/шлях до функції
app = FastAPI()

# створення функцій
@app.post('/message')
def message():
    print("виклик функції message")


@app.post('/function')
def func():
    print("Виклик функції func")


# функція яка повертає результат
# формат Json

# @app.post("/data")
# def get_data():
#     return {"result": "Привіт від сервера"}


# передача параметрів
# параметри як чатина шляху
# як правило працює для одного параметра

@app.post("/mult2/{num}")
def mult2(num: int):
    result = 2 * num
    return {'result': result}


# функція для реєстрації користувачів
# отримує щось типу
{
    'user_name': 'Jhon',
    "login": "jhon45678",
    'password': '123qwer',
    'age': 45
}