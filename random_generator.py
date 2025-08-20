import random
import datetime

import pandas as pd


students = [
    # "Ірина Греча",
    # "Адєлартей Еммануель Адевунмі",
    "Бондаренко Олексій Анатоліович",
    "Вельможний Тарас Володимирович",
    # "Возна Евеліна",
    # "Володенков Владислав Олександрович",
    "Марущак Давид Сергеевич",
    "Мовчан Захар Олександрович",
    # "Нашкородов Артем",
    # "Патора Олексій Валерійович",
    "Пентюхов Никита Владимирович",
    "Потерейко Володимир Іванович",
    "Рекуненко Микола Миколайович",
    "Ткачук Владислав Максимович",
    "Токар Сергій Володимирович",
    # "Хайлов Євген Олександрович",
    "Шапошников Олександр Сергiйович"
]

#print(len(students))

for i in range(len(students)):
    students[i] = f"{students[i]:<35}"

df = pd.read_csv('students.csv', index_col=0)

current_df = df.loc[students]
now = datetime.datetime.now().date()
now = str(now)

summa = current_df.sum(axis=1)
min_value = summa.min()
ids = summa[summa == min_value].index
student = random.choice(ids)

print(student)

if now not in df.columns:
    df[now] = 0

df.loc[student, now] = 1
df[now] = df[now].astype(int)

df.to_csv('students.csv')