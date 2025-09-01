# манічні методи

nums = [1, 2, 3, 4]

# явний метод(звичайний)
nums.append(5)

# магічній(викликається не явно(без прямої назви))
10 in nums
nums.__contains__(10)

# num1 = 10
# num1 + 5
# res = num1.__add__(5)
# print(res)


# class Person:
#     def __init__(self, name, age):
#         print('hello from init')
#         self.name = name
#         self.age = age
#
#     def __str__(self):  # заміняє операцію str(self)
#         return f"{self.name}, {self.age} years"
#
#     def __eq__(self, other):  # self == other
#         if isinstance(other, Person):
#             print('Перевірка з Person')
#             return self.name == other.name and self.age == other.age
#
#         elif isinstance(other, str):
#             print('Перевірка з str')
#             return self.name == other
#
#         else:
#             return False
#
#     def __gt__(self, other):  # self > other
#         if isinstance(other, Person):
#             return self.age > other.age
#
#         else:
#             return False
#
#     # def __lt__(self, other): # self < other
#     #     pass
#
#     def grow(self):
#         self.age += 1
#
#
# # метод __init__
# person1 = Person('Jhon', 37)
# person2 = Person('Sophie', 40)
#
# # # __str__
# # print(person1)
# #
# # info = str(person2)
# # print(info)
# #
# # # __eq__
# # print(person1 == person2)
# #
# # person3 = Person('Sophie', 40)
# # print(person3 == person2)
# #
# # print(person1 == 'Jhon')
# # # user = 'Jhon'
# # # user.name
# #
# # print(person1 == 12)
# #
# #
# # nums = [1, 2, 3]
# # name = 'Jhon'
# # print(nums == name)
#
# # __gt__
#
# if person1 > person2:
#     print(f"{person1} старший/а за {person2}")
# else:
#     print(f"{person2} старший/а за {person1}")
#
#
# person3 = Person('Mike', 21)
#
# people = [person1, person2, person3]
#
# # отримати найстаршк людину
# max_person = max(people)
# print(f"Найстарша людина: {max_person}")
#
# min_person = min(people)
# print(f"Наймолодша людина: {min_person}")



class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Cart with {self.items}"

    def __contains__(self, item):  # item in self
        return item in self.items

    def __getitem__(self, index):  # self[index]
        return self.items[index]

    def __len__(self):   # len(self)
        return len(self.items)

    def generator(self):
        for item in self.items:
            yield item

    def __iter__(self):
        return iter(self.items)



cart = Cart()

cart.add_item("Milk")
cart.add_item("Bread")
cart.add_item("Butter")

# print(cart)
#
#
# # item in cart
# print('Milk' in cart)
# print('milk' in cart)
#
# # cart[2]
# print(cart[1])
#
#
# # len(cart)
# print(len(cart))

#print(cart == cart)

range(10)
'ghghjghkgj'
[1, 2, 3, 4]
{1, 2, 3, 4}
{'one': 1, "two": 2}

# звичайна функція
def func(n):
    for k in range(n):
        return 2 ** k

# фунція з багатьма результатами(генератор)
def power2(n):
    for k in range(n):
        yield 2**k  #  повертає результат для for і працює далі


# степені двійки
# for num in power2(10):
#     print(num)

# print(cart)   #  str(cart)

for item in cart:  # iter(cart)
    # код для однієї ітерації
    print(item)

print(iter(cart))
