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

query_text = """
SELECT *
FROM DOCTORS
WHERE SALARY > 90000
"""

# переведення запиту в правильний формат
query_text = text(query_text)

query = session.execute(query_text)

# вказуємо які результати(рядки) ми хочемо отримати
# всі результати
# первий результат
# перші n результатів
# останні n результатів

results = query.all()

# приклад отримання назв колонок таблиці doctors
doctors = tables['doctors']
column_names = doctors.columns.keys()
print(column_names)

for row in results:
    print(row)

print(results)
