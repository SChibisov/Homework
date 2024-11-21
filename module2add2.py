import random
import math

spec_num = int(input('Задайте любое число = '))
rand_num = [random.randint(1, 10000) for _ in range(200)]

num_sqr = []
res_ = []
for i in rand_num:
    if i < spec_num:
        num_sqr.append(i)
        res_.append(math.sqrt(i))
print('Числа меньше заданного: ', num_sqr)
print('Квадратный корень чисел меньше заданного: ', res_)

