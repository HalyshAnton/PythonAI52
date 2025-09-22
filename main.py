# # дерева
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None  # корінь дерева
#
#     def add(self, data):
#         node = Node(data)
#
#         # дерево порожнє
#         if self.root is None:
#             self.root = node
#             return
#
#         # вузол де робимо перевірку
#         current_node = self.root
#
#         while True:
#             # йдемо наліво
#             if data < current_node.data:
#                 # зліва вільне місце(вузла немає)
#                 if current_node.left is None:
#                     current_node.left = node
#                     break
#                 else:
#                     # зліва зайнято(повторити перевірку знову)
#                     current_node = current_node.left
#
#             elif data > current_node.data:  # йдемо направо
#                 # справа вільне місце(вузла немає)
#                 if current_node.right is None:
#                     current_node.right = node
#                     break
#                 else:
#                     current_node = current_node.right
#
#             else: # не можна добавляти дублікати
#                 break
#
#
#     def search(self, data):
#         current_node = self.root
#
#         while current_node is not None:
#             # вузол знайдено
#             if current_node.data == data:
#                 return True
#
#             elif data < current_node.data:
#                 current_node = current_node.left
#
#             elif data > current_node.data:
#                 current_node = current_node.right
#
#         # цикл зупинився -- значить даних в дереві немає
#         return False
#
#     def min(self):
#         current_node = self.root
#
#         while current_node.left is not None:
#             current_node = current_node.left
#
#         return current_node.data
#
#     def print_inorder(self):
#         self._inorder(self.root)
#         print()
#
#     def _inorder(self, node):  # _ -- приватний метод класу
#         if node.left:
#             self._inorder(node.left)
#
#         print(node.data, end=' ')
#
#         if node.right:
#             self._inorder(node.right)
#
#
#
# tree = BinaryTree()
#
# tree.add(5)
# tree.add(7)
# tree.add(3)
# tree.add(8)
# tree.add(4)
# tree.add(6)
#
# print(tree.search(8))
# print(tree.search(2))
#
# print(tree.min())
#
# tree.print_inorder()
import bintrees


# # AVL дерева
# import bintrees
#
# tree = bintrees.AVLTree()
#
# # сортує значення по параметру key
# tree.insert(key=8, value='John')
# tree.insert(key=10, value='Maria')
#
#
# tree.remove(8)
#
# # отримати значення(перевірка)
#
# if 10 in tree:
#     print(tree[10])



# Завдання:
#
# Створити бінарне дерево для каталогу книг у бібліотеці.
#
# Операції:
#
# Insert: Додавання нової книги в каталог з вказаною назвою та іншою інформацією (автор, рік видання, жанр тощо).
#
# Search: Пошук книги за назвою або іншими параметрами. Пошук повинен повертати усю інформацію, що стосується цієї книги.
#
# Delete: Видалення книги з каталогу за назвою або іншими параметрами.
#
# Display: Виведення всього каталогу книг за зростанням або спаданням алфавіту за назвою.
#
# Count: Підрахунок кількості книг у бібліотеці.
#
# Властивості:
#
# Зберігання: Книги зберігаються за алфавітом за назвою книги.
#
# Пошук: Користувач може шукати книгу за назвою або іншою інформацією про книгу.
#
# Видалення: Користувач може видаляти книгу з каталогу за назвою або іншими параметрами.
#
# Показ каталогу: Виведення всіх книг у вигляді списку, відсортованого за назвою книги.
#
# Статистика: Виведення загальної кількості книг у бібліотеці.
#
# Приклад використання:
#

class Book:
    def __init__(self, name, author, year, style):
        self.name = name
        self.year = year
        self.author = author
        self.style = style

    def __str__(self):
        return f"Book\n\tauthor\t{self.author}\n\tname\t{self.name}\n\tyear\t{self.year}\n\tstyle\t{self.style}"


class BinaryTreeLibrary():
    def __init__(self):
        self.books_tree = bintrees.AVLTree()

    # Insert: Додавання нової книги в каталог з вказаною назвою та іншою інформацією(автор, ріквидання, жанртощо).
    def insert(self, name, author, year, style):
        book = Book(name, author, year, style)
        self.books_tree.insert(key=name, value=book)

    # Search: Пошук книги за назвою або іншими параметрами. Пошук повинен повертати усю інформацію, що стосується цієї книги.
    def search(self, name):
        if name in self.books_tree:
            book = self.books_tree[name]
            print(book)

    # Delete: Видалення книги з каталогу за назвою або іншими параметрами.
    def delete(self, name):
        if name in self.books_tree:
            self.books_tree.remove(name)

    # Display: Виведення всього каталогу книг за зростанням або спаданням алфавіту за назвою.
    def display(self):
        for name in self.books_tree:
            print(self.books_tree[name])

    # Count: Підрахунок кількості книг у бібліотеці.
    def count(self):
        return len(self.books_tree)


library = BinaryTreeLibrary()

library.insert("1984", "George Orwell", 1949, "Dystopian Fiction")
library.insert("To Kill a Mockingbird", "Harper Lee", 1960, "Classic Fiction")
library.insert("Pride and Prejudice", "Jane Austen", 1813, "Romance")

print("Books in library:")
library.display()

print("\nSearching for '1984':")
library.search("1984")

library.delete("To Kill a Mockingbird")
print("\nBooks in library after deletion:")
library.display()

print("\nTotal number of books:", library.count())

