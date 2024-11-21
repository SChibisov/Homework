import random

rand_num = [random.randint(1, 10000) for _ in range(50)]
rand_num.sort()
multiple_41 = 0
for i in rand_num:
    if i % 41 == 0:
        multiple_41 += 1


z = (rand_num[0] + rand_num[49])/2
res_ = 0
for j in rand_num:
    if j > z:
        res_ += 1


print(rand_num)
print('Количество числе кратных 41 = ', multiple_41)
print('Количество чисел больще среднего арифметического наибольшего и наименьшего значений списка = ', res_)
