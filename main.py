# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
#     def __str__(self):
#         return f"{self.data} -> {self.next}"
#
#
# class DoubleLinkedList:
#     """
#     Клас двозв'язного списку.
#     """
#
#     def __init__(self):
#         """
#         Ініціалізація порожнього списку.
#         """
#         self.head = None
#         self.tail = None
#
#     def __str__(self):
#         return str(self.head)
#
#     def push_end(self, data):
#         """
#         Додає елемент у кінець списку.
#         :param data: Дані для додавання
#         """
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#
#     def push_start(self, data):
#         """
#         Додає елемент на початок списку.
#         :param data: Дані для додавання
#         """
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#
#     def pop_end(self):
#         """
#         Видаляє останній елемент зі списку.
#         :return: Дані видаленого елемента або None, якщо список порожній
#         """
#         if not self.tail:
#             return None
#
#         data = self.tail.data
#
#         if self.head.next is None:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#
#         return data
#
#     def pop_start(self):
#         """
#         Видаляє перший елемент зі списку.
#         :return: Дані видаленого елемента або None, якщо список порожній
#         """
#
#         if not self.head:
#             return None
#
#         data = self.head.data
#
#         if self.head.next is None:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#         return data
#
#
# # черги
# class Queue:
#     def __init__(self):
#         self.queue = DoubleLinkedList()
#         self.item_count = 0
#
#     def push(self, item):  # append\enqueue\put
#         self.queue.push_end(item)
#         self.item_count += 1
#
#     def pop(self):   # get\dequeue
#         item = self.queue.pop_start()
#         self.item_count -= 1
#
#         return item
#
#     def __len__(self):
#         return self.item_count
#
#     def __str__(self):
#         return str(self.queue)
#
#
# queue = Queue()
#
# # добавити елементи
# queue.push('Mary')
# queue.push('John')
# queue.push('Mark')
# queue.push('Anna')
#
# print(queue)
#
# # дістати елементґ
#
# person = queue.pop()
# print(person)
# print(queue)

# # те саме, через вбудований клас
# from queue import Queue
#
# # help(Queue)
#
# queue = Queue()
#
# # добавити елементи
# queue.put('Mary')
# queue.put('John')
# queue.put('Mark')
# queue.put('Anna')
#
# print(queue)
#
# # дістати елементґ
#
# person = queue.get()
# print(person)
# print(queue)

# from queue import Queue
# import datetime
# import time
#
#
# class Message:
#     def __init__(self, text):
#         self.text = text
#         self.time = datetime.datetime.now().time()  # теперішній час
#
#     def __str__(self):
#         return f"[{self.time.strftime('%H:%M:%S')}] {self.text}"
#
#
# # Простий месенджер
# class Messanger:
#     def __init__(self):
#         self.messages = Queue()
#
#     def add_message(self, text):
#         message = Message(text)
#         self.messages.put(message)
#
#         print('повідомлення додано')
#
#     def read_message(self):
#         # перевірити чи черга порожня
#         if self.messages.empty():
#             print('Повідомлень немає')
#             return
#
#         message = self.messages.get()
#         print(message)
#
#         return message
#
#
# messanger = Messanger()
#
# messanger.add_message('Hello')
# messanger.add_message('How are you?')
# messanger.add_message('Fine')
# messanger.read_message()
# messanger.add_message('Thx')
#
# messanger.read_message()
# messanger.read_message()
# messanger.read_message()
# messanger.read_message()
# messanger.read_message()

# черга з пріоритетом
# Основна структура даних -- купа

from queue import PriorityQueue


queue = PriorityQueue()

# добавити елемент з пріоритетом
# queue.put((priority, item))
queue.put((3, 'John'))  # добавити John з пріоритетом 3
queue.put((2, 'Sophy'))
queue.put((1, 'Anna'))
queue.put((1, 'Mark'))
queue.put((2, 'Mary'))
queue.put((3, 'Mike'))

# в межах одного пріоритету, елементи зберігаються у відсортованому вигляді

item = queue.get()  # отримуємо елемент з пріоритетом 1
print(item)

item = queue.get()
print(item)

item = queue.get()
print(item)

item = queue.get()
print(item)

item = queue.get()
print(item)

item = queue.get()
print(item)