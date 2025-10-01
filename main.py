# # дз
#
# def add_album(bands: dict, band: str, album: str) -> None:
#     """Додати новий альбом до гурту."""
#     if band not in bands:
#         print(f"Гурт '{band}' не знайдено!")
#         return
#
#     if album in bands[band]:
#         print(f"Альбом '{album}' вже є у гурта '{band}'!")
#         return
#
#     bands[band].append(album)
#
#
# text = '   \n  '
# # text.strip() == ''
import threading
import time


# # багато потоковість
# import time
#
#
# def func1():
#     print("Початок функції 1")
#     time.sleep(0.5)
#     total = 0
#     for num  in range(1, 1000):
#         total += num
#
#     print(total)
#     print("Кінець функції 1")
#
#
# def func2():
#     print("Початок функції 2")
#     time.sleep(0.5)
#     count15 = 0
#     for num in range(1, 1000):
#         if num % 15:
#             count15 += 1
#
#     print(count15)
#     print("Кінець функції 2")
#
#
# # без потоків
# start = time.time()
# func1()
# func2()
# end = time.time()
#
# print(f"Час без потоків -- {end - start} сек")
# print()
#
#
# # з потоками
#
# import threading
#
# # потік для функції 1
# thread1 = threading.Thread(target=func1)
#
# # потік для функції 2
# thread2 = threading.Thread(target=func2)
#
# # запуск потоків
# start = time.time()
# thread1.start()
# thread2.start()
#
# # дочекатись  закінчення потоків
# thread1.join()
# thread2.join()
#
# end = time.time()
#
# print(f"Час з потоками -- {end - start} сек")


# # функції з параметрами
# def func1(text, num):
#     for _ in range(num):
#         print(text + '\n', end='')
#
#
# def func2(nums):
#     print(f"{sorted(nums)}\n", end='')
#
#
# nums = [1, 4, 3, 2, 5, 3, 5, 3, 4, 6, 4, 7, 8, 9, 0, 0]
#
# # потік для функції 1 з параметрами "hello" 20
# thread1 = threading.Thread(target=func1, args=("hello", 20))
#
# # потік для функції 2 з параметрами nums
# thread2 = threading.Thread(target=func2, args=(nums, ))
#
# # потік для функції 1 у форматі func1('long text', num=10)
# thread3 = threading.Thread(target=func1,
#                            args=("long text",),
#                            kwargs={"num": 10}
#                            )
#
# thread1.start()
# thread2.start()
# thread3.start()


# є список задач, які виконують декілька потоків
# результати треба записати у спільний файл
from threading import Lock

locker = Lock()


def do_task(tasks, thread_num, locker):
    while True:
        # кажемо іншим потокам зупинитися
        locker.acquire()

        if not tasks:
            print(f"Потік{thread_num} закінчив роботу")
            locker.release()
            return

        task = tasks.pop()

        # інші потоки можуть продовжувати
        locker.release()

        with open("logging.txt", 'a', encoding='utf-8') as file:
            print(f"Потік{thread_num} виконав задачу {task}", file=file)


tasks = list(range(1, 10))

threads = []
for i in range(20):
    thread = threading.Thread(target=do_task, args=(tasks, i, locker))
    threads.append(thread)

for thread in threads:
    thread.start()
