import redis
import base64
import json


class SocialApp:
    def __init__(self):
        self.server = redis.Redis(host='localhost', # адреса бази даних
                                  port=6379,   #  порт
                                  decode_responses=True  # не повертати байти
                                  )

        # активний користувач(поки невідомий)
        self.current_user = None

    # ■ додати користувача;
    def _get_password_key(self, username):
        return f'password:{username}'

    def add_user(self, username, password):
        # отримати ключ для сервера
        password_key = self._get_password_key(username)

        # перевірка чи користувач вже є
        if self.server.exists(password_key):
            print('такий користувач вже є')
            return

        # кодування пароля для безпеки
        encoded_password = base64.b64encode(password.encode("utf-8"))

        self.server.set(password_key, encoded_password)

        # password:Anton - 86435145
        # password:Sophie - 78643134

    # вхід за логіном і паролем;
    def login(self, username, password):
        password_key = self._get_password_key(username)

        if not self.server.exists(password_key):
            print('такого користувача немає')
            return

        true_password = self.server.get(password_key)
        true_password = base64.b64decode(true_password).decode('utf-8')

        if password == true_password:
            print(f"Вхід у систему. Вітаємо {username}")
            self.current_user = username
        else:
            print("Пароль невірний")

    # ■ добавити інформацію про користувача;
    def _get_data_key(self):
        return f"data:{self.current_user}"

    def add_user_data(self, user_data):
        """
        user_data повинна міститти дані які кодуються в json

        :param user_data:
        :return:
        """
        # user_data = {
        #     'name': 'Anton',
        #     'age': 23,
        #     'articles': ['article1', 'article1', 'article1']
        # }
        if self.current_user is None:
            print("Ввійдіть у систему")
            return

        data_key = self._get_data_key()

        for key, value in user_data.items():
            #переводимо дані у json(str рядок)
            value = json.dumps(value)

            self.server.hset(data_key, key, value)

    # ■ добавити друзів;
    def _get_friend_key(self, username):
        return f"friends:{username}"

    def add_friend(self, friend_name):
        if self.current_user is None:
            print("Ввійдіть у систему")
            return

        #перевірка чи friend_name зареєстрований
        friend_key = self._get_password_key(friend_name)
        if not self.server.exists(friend_key):
            print(f"Такої людини не існує {friend_name}")
            return

        key1 = self._get_friend_key(self.current_user)
        self.server.sadd(key1, friend_name)

        key2 = self._get_friend_key(friend_name)
        self.server.sadd(key2, self.current_user)

    # ■ видалити користувача;
    # ■ редагувати інформацію про користувача;
    # ■ пошук користувача за ПІБ;
    # ■ перегляд інформації про користувача;
    # ■ перегляд усіх друзів користувача;
    # ■ перегляд усіх публікацій користувача

app = SocialApp()
app.add_user('Anton', 'qwerty123')
app.add_user('Jhon', 'kygkhgkhghs35445')

app.login('Jhon', 'qwerty123')
app.login('Anton', 'qwerty1234')
app.login('Anton', 'qwerty123')

# user_data = {
#             'name': 'Anton',
#             'age': 23,
#             'articles': ['article1', 'article1', 'article1']
#         }
# app.add_user_data(user_data)

app.add_friend("Maria")
app.add_friend("Jhon")