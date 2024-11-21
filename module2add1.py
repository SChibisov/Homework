num = int(input('Введите любое число = '))

import random

rand_num = random.randrange(1, num)

res_square = []

for i in range(1, num + 1):
    if i % 2 == 0:
        res_square.append(i ** 2)

print(res_square)
