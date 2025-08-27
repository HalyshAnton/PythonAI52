# class Project:
#     def __init__(self, name: str, budget: int, tasks: list):
#         self.name = name
#         self.budget = budget
#         self.tasks = tasks
#
#         self.expenses = 0
#         self.is_finished = False
#         self.time = 0
#
#     def show_info(self):
#         """
#         Показує інформацію про проект
#         """
#
#         print()
#         print(f"Інформація по проекту {self.name}")
#         print(f'\t Бюджет -- {self.budget}грн')
#         print(f"\t Використано -- {self.expenses}/{self.budget}")
#         print(f"\t Час виконання -- {self.time} місяців")
#
#         if self.is_finished:
#             print(f'\t Статус -- Завершений')
#         else:
#             print(f'\t Статус -- Незавершений')
#
#         print('\t Список задач:')
#         for task in self.tasks:
#             print(f"\t\t {task}")
#
#     def add_task(self, new_task):
#         self.tasks.append(new_task)
#         print(f"Додано нове завдання {new_task}")
#
#     def create_subtasks(self, old_task, subtasks):
#         # чи є стара задачі в списку
#         if old_task not in self.tasks:
#             print(f"Такої задачі немає в списку")
#             return
#
#         # old_task є в списку
#         self.tasks.remove(old_task)
#         self.tasks.extend(subtasks)  # добавити всі елементи з subtasks в список self.tasks
#
#         # # спосіб де багато відступів
#         # if old_task in self.tasks:
#         #     # old_task є в списку
#         #     self.tasks.remove(old_task)
#         #     self.tasks.extend(subtasks)  # добавити всі елементи з subtasks в список self.tasks
#         # else:
#         #     print(f"Такої задачі немає в списку")
#
#     def do_task(self, task, price, time):
#         if task not in self.tasks:
#             print(f"Такої задачі немає в списку")
#             return
#
#         if price > (self.budget - self.expenses):
#             print('Не вистачає коштів')
#             return
#
#         # все добре, робимо задачу
#         self.tasks.remove(task)
#         self.expenses += price
#         self.time += time
#
#         self.is_finished = len(self.tasks) == 0
#
#     def deposit(self, price):
#         self.budget += price
import typing


# Інкапсуаляція

# nums = [1, 2, 3, 4]
# nums.append(5)


# Поліморфізм


class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        print('Мяу')

    def grow(self):
        self.age += 1

    def catch_mouse(self):
        pass
#
#
# class Dog:
#     def __init__(self, name, age, speed):
#         self.name = name
#         self.age = age
#         self.speed = speed
#
#     def make_sound(self):
#         print('Гав')
#
#     def grow(self):
#         self.age += 1
#         self.speed -= 2
#
#
# class Hamster:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def make_sound(self):
#         print('Пі-пі')
#
#     def grow(self):
#         self.age += 1
#
#
# cat = Cat('Murchick', 3, 'black')
# dog = Dog('Barsik', 2, 10)
# hamster = Hamster('Benny', 4)
#
# pets = [cat, dog, hamster]
#
# # кожна тварина видає звуки
# for pet in pets:
#     pet.make_sound()
#
#
# # model = NeuralNetwork()
# #
# # model.train(data)


# # typing
# import typing
#
# # typing.List[тип елементів]
#
# # якщо може бути різні типи даних
# # typing.List[тип1 | тип2 | тип3]
# typing.List[int | float]
#
#
#
# # def func(param1: int, param2: typing.List[str]):
# #     for item in param2:
# #         item.
#
# cat = Cat('Murchick', 3, 'black')
# num = 10
#
# print(type(num))
# print(type(cat))

# Завдання 5. Онлайн-магазин
# Створіть наступні класи:
#
# Product – атрибути name, price
# Customer – атрибути name, balance
# Cart – атрибути owner, items (список продуктів)
#
# Методи:
#
# add_product(product) – додає товар у кошик
# checkout() – знімає з балансу покупця вартість усіх товарів (якщо грошей вистачає)
# show_cart() – виводить список товарів і їх загальну вартість
#
# Напишіть функцію create_customer() та create_product(), які повертають об’єкти.
# Створіть кілька товарів, покупців і дайте їм зробити покупки.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"Продукт {self.name} -- {self.price}грн")


class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, total):
        self.balance += total

    def withdraw(self, total):
        self.balance -= total


class Cart:
    def __init__(self, owner: Customer, items: typing.List[Product]):
        self.owner = owner
        self.items = items

    def add_product(self, product: Product):
        self.items.append(product)

    def ckeckout(self):
        for product in self.items:
            price = product.price
            self.owner.withdraw(price)

        self.items = []

    def show(self):
        total = 0
        for product in self.items:
            price = product.price
            total += price
            product.show()

        print(f"Загальна вартість {total}грн")


#product = Product('milk', 70)

# product = {
#     "name": "milk",
#     "price": 70
# }

customer = Customer("Mary", 5000)

product1 = Product('milk', 70)
product2 = Product('bread', 30)

cart = Cart(customer, [product1, product2])

cart.ckeckout()

print(customer.balance)


