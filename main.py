import redis
import base64


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


    # ■ видалити користувача;
    # ■ редагувати інформацію про користувача;
    # ■ пошук користувача за ПІБ;
    # ■ перегляд інформації про користувача;
    # ■ перегляд усіх друзів користувача;
    # ■ перегляд усіх публікацій користувача

app = SocialApp()
app.add_user('Anton', 'qwerty123')

app.login('Jhon', 'qwerty123')
app.login('Anton', 'qwerty1234')
app.login('Anton', 'qwerty123')