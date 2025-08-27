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


class Dog:
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def make_sound(self):
        print('Гав')

    def grow(self):
        self.age += 1
        self.speed -= 2


class Hamster:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Пі-пі')

    def grow(self):
        self.age += 1


cat = Cat('Murchick', 3, 'black')
dog = Dog('Barsik', 2, 10)
hamster = Hamster('Benny', 4)

pets = [cat, dog, hamster]

# кожна тварина видає звуки
for pet in pets:
    pet.make_sound()


# model = NeuralNetwork()
#
# model.train(data)


