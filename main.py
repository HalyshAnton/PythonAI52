# підключення до бази даних в postgresql через sqlalchemy
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker

import json


with open('credentials.json') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

DATABASE_URL = f"postgresql+pg8000://{login}:{password}@localhost/hospital"
engine = create_engine(DATABASE_URL)

# клас для створення сесій
Session = sessionmaker(bind=engine)

#конкретна сесія
session = Session()

# отримання таблиць з бази даних

metadata = MetaData()
metadata.reflect(bind=engine)

tables = metadata.tables # словник з таблицями бази даних

# for table_name in tables:
#     print(table_name)
#     print(tables[table_name].columns)
#     print('-'*20)

# виконання простого запиту

# query_text = """
# SELECT *
# FROM DOCTORS
# WHERE SALARY > 90000
# """
#
# # insert_query = f"""
# # INSERT INTO DOCTORS (FIRST_NAME, LAST_NAME, SPECIALTY, SALARY)
# # VALUES ('{user}', '{surname}', 'Терапевт', 85000)
# # """
#
# # переведення запиту в правильний формат
# query_text = text(query_text)
#
# query = session.execute(query_text)
#
# # вказуємо які результати(рядки) ми хочемо отримати
# # всі результати
# # первий результат
# # перші n результатів
# # останні n результатів
#
# results = query.all()
#
# # приклад отримання назв колонок таблиці doctors
# doctors = tables['doctors']
# column_names = doctors.columns.keys()
# print(column_names)
#
# for row in results:
#     print(row)
#
# print(results)

# Завдання 1
# Для бази даних «Лікарня», яку ви розробляли в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії з
# базою даних, який дозволяє:
# ■ Вивести назви всіх таблиць у базі даних.
def show_table_names():
    print("Таблицi:")
    for table_name in tables:
        print('*', table_name)

# ■ Показати всю таблицю
def show_table(table_name):
    query_text = f"""
        SELECT *
        FROM {table_name.upper()}
    """

    query_text = text(query_text)
    query = session.execute(query_text)
    results = query.all()

    table = tables[table_name]
    column_names = table.columns.keys()

    for column in column_names:
        print(f"{column:<15}", end='\t')
    print()

    for row in results:
        for data in row:
            print(f"{data:<15}", end='\t')
        print()

# ■ Вставляти рядки в таблиці бази даних.
# ■ Оновлення рядків у таблицях бази даних. При спробі
# оновлення усіх рядків в одній таблиці надайте запит на
# підтвердження користувачеві. Оновлювати усі рядки
# можна лише після підтвердження користувачем.
# ■ Видалення рядків з таблиць баз даних. При спробі видалити
# усі рядки в одній таблиці потрібно видавати користувачу
# запит на підтвердження. Видаляти усі рядки, можна тільки
# після підтвердження користувачем.