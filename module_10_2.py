import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        count_days = 0
        quantity_enemy = 100
        print(f'{self.name}, на нас напали!')
        for i in range(quantity_enemy):
            if quantity_enemy != 0:
                count_days += 1
                quantity_enemy -= self.power
                print(f'{self.name} сражается {count_days}..., осталось {quantity_enemy} воинов.')
                time.sleep(1)
        return self, print(f'{self.name} одержал победу спустя {count_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
