# # формат JSON(словники)
#
# # data = {
# #     "name": "Anton",
# #     "age": 23
# # }
# #
# # data['age']
#
# user1_name = 'Jhon'
# user1_data = {
#     'wins': 4,
#     'loses': 2
# }
#
# user2_name = 'Mary'
# user2_data = {
#     'wins': 6,
#     'loses': 0
# }
#
# user3_name = 'Mike'
# user3_data = {
#     'wins': 1,
#     'loses': 5
# }
#
# data = [
#     {
#         'name': 'Jhon',
#         'game_results': {
#             'wins': 4,
#             'loses': 2
#         }
#     },
#
#     {
#         'name': 'Mary',
#         'game_results': {
#             'wins': 6,
#             'loses': 0
#         }
#     }
# ]
#
# # отримати кількість перемог  для гравця з індексом 0
# print(data[0]['game_results']['wins'])
#
# data = {
#   "gt_parse": {
#     "menu": [
#       {
#         "nm": "Nasi Campur Bali",
#         "cnt": "1 x",
#         "price": "75,000"
#       },
#       {
#         "nm": "Bbk Bengil Nasi",
#         "cnt": "1 x",
#         "price": "125,000"
#       },
#       {
#         "nm": "MilkShake Starwb",
#         "cnt": "1 x",
#         "price": "37,000"
#       },
#       {
#         "nm": "Ice Lemon Tea",
#         "cnt": "1 x",
#         "price": "24,000"
#       },
#       {
#         "nm": "Nasi Ayam Dewata",
#         "cnt": "1 x",
#         "price": "70,000"
#       },
#       {
#         "nm": "Free Ice Tea",
#         "cnt": "3 x",
#         "price": "0"
#       },
#       {
#         "nm": "Organic Green Sa",
#         "cnt": "1 x",
#         "price": "65,000"
#       },
#       {
#         "nm": "Ice Tea",
#         "cnt": "1 x",
#         "price": "18,000"
#       },
#       {
#         "nm": "Ice Orange",
#         "cnt": "1 x",
#         "price": "29,000"
#       },
#       {
#         "nm": "Ayam Suir Bali",
#         "cnt": "1 x",
#         "price": "85,000"
#       },
#       {
#         "nm": "Tahu Goreng",
#         "cnt": "2 x",
#         "price": "36,000"
#       },
#       {
#         "nm": "Tempe Goreng",
#         "cnt": "2 x",
#         "price": "36,000"
#       },
#       {
#         "nm": "Tahu Telor Asin",
#         "cnt": "1 x",
#         "price": "40,000."
#       },
#       {
#         "nm": "Nasi Goreng Samb",
#         "cnt": "1 x",
#         "price": "70,000"
#       },
#       {
#         "nm": "Bbk Panggang Sam",
#         "cnt": "3 x",
#         "price": "366,000"
#       },
#       {
#         "nm": "Ayam Sambal Hija",
#         "cnt": "1 x",
#         "price": "92,000"
#       },
#       {
#         "nm": "Hot Tea",
#         "cnt": "2 x",
#         "price": "44,000"
#       },
#       {
#         "nm": "Ice Kopi",
#         "cnt": "1 x",
#         "price": "32,000"
#       },
#       {
#         "nm": "Tahu Telor Asin",
#         "cnt": "1 x",
#         "price": "40,000"
#       },
#       {
#         "nm": "Free Ice Tea",
#         "cnt": "1 x",
#         "price": "0"
#       },
#       {
#         "nm": "Bebek Street",
#         "cnt": "1 x",
#         "price": "44,000"
#       },
#       {
#         "nm": "Ice Tea Tawar",
#         "cnt": "1 x",
#         "price": "18,000"
#       }
#     ],
#     "sub_total": {
#       "subtotal_price": "1,346,000",
#       "service_price": "100,950",
#       "tax_price": "144,695",
#       "etc": "-45"
#     },
#     "total": {
#       "total_price": "1,591,600"
#     }
#   },
#   "meta": {
#     "version": "2.0.0",
#     "split": "train",
#     "image_id": 0,
#     "image_size": {
#       "width": 864,
#       "height": 1296
#     }
#   }
# }
#
# # отримати список ключів
# print(list(data.keys()))
#
# # отриати дані парсингу
# parse_data = data['gt_parse']
#
# print(list(parse_data.keys()))
#
# # дані про зігільну ціну
# sub_total_data = parse_data['sub_total']
#
# print(list(sub_total_data.keys()))
#
# # податки
# print(sub_total_data['tax_price'])
#
# # теж саме але одразу
# print(data['gt_parse']['sub_total']['tax_price'])
#
# # pydantic

# pickle
# import json
#
#
# data = {
#     'name': 'Sophie',
#     'age': 42
# }
#
# with open('data.json', 'w') as file:
#     json.dump(data, file)
#
#
# with open('data.json', 'r') as file:
#     new_data = json.load(file)
#
#
# print(new_data)
#
#
# # дані зберігаються як str рядки
# encoded = json.dumps(data)
# print(encoded)
# print(type(encoded))


#pickle зберігання даних як байти

import pickle


# data = {
#     'name': 'Sophie',
#     'age': 42
# }
#
# encoded = pickle.dumps(data)
# print(data)
# print(encoded)
# print(type(encoded))
#
#
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person = Person('Jhon', 35)
# encoded = pickle.dumps(person)
# print(person)
# print(encoded)
# print(type(encoded))

# робота з файлами
import json


data = {
    'name': 'Sophie',
    'age': 42
}

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Person: {self.name}, {self.age} yr")

person = Person('Mike', 16)



with open('data.pkl', 'wb') as file:
    pickle.dump(person, file)


with open('data.pkl', 'rb') as file:
    new_data = pickle.load(file)


print(new_data.info())
