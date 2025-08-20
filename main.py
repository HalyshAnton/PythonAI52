# # класи
#
# class Dog:
#     # опис атрибутів та методів
#     # name
#     # breed
#     pass
#
#
# # створення об'єкта класу(конкретного песика)
# dog1 = Dog(name='bethowen')  # викликається метод __init__
# dog2 = Dog(name='tuzik')
#
# dog1.eat('bone')
#
#
# nums = [1, 2, 3, 4]
# nums.append()

# snake_case
# CamelCase

# class [НазваКласу]:
#     def [назва методу 1]:
#          [код]

#     def [назва методу 2]:
#          [код]


class Dog:
    def __init__(self, name, age, breed='labrador'):
        print('hello from Dog.__init__')
        # self -- це об'єкт класу(конкретний песик)

        # створення атрибуту name
        self.name = name

        self.age = age
        self.breed = breed

    def eat(self, food):
        print(f'{self.name} is eating {food}')

    def grow(self):
        """
        Пес подорослішав на 1 рік
        """
        self.age += 1

    def get_name(self):
        return self.name


# dog1 = Dog('tuzik')

# dog1.eat('bone')  # Dog.eat(dog1, 'bone')
# nums.append(10)   # list.append(nums, 10)


# # створення конкретного пса
# dog1 = Dog(name='tuzik', age=5)
#
# print(dog1.name)
# print(dog1.age)
# print(dog1.breed)
#
# # створення інщого пса
# dog2 = Dog(name='barsik', age=2, breed='haski')
#
# print(dog2.name)
# print(dog2.age)
# print(dog2.breed)
#
# print()
#
# dog1.eat('bone')
# dog2.eat('meat')
#
# print()
#
# print(dog1.age)
# dog1.grow()
# print(dog1.age)
#
#
# print()
#
# name = dog1.get_name()
# print(name)

# # атрибути можна змінювати але небажано
# dog = Dog(name='tuzik', age=5)
# dog.age += 2
# dog.color = 'brown'
