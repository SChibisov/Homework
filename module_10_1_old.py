import time
from threading import Thread


def thr_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)


def thr_character_set():
    character_set = [chr(i) for i in range(97, 107)]
    for chr_set in character_set:
        print(chr_set)
        time.sleep(1.01)  # Если установить одинаковый интервал в обоих функциях,
        # то вывод на консоль не будет соответствовать домашнему заданию


thr_num = Thread(target=thr_numbers)
thr_char = Thread(target=thr_character_set)

thr_num.start()
thr_char.start()
thr_num.join()
thr_char.join()
