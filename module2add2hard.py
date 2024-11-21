import random
import math

rand_num = [random.randint(1, 10000) for _ in range(10000)]

multiple_5 = []
res_ = []

for i in rand_num:
    if i % 5 == 0:
        multiple_5.append(i)
    else:
        continue

for j in rand_num:
    if j > (sum(multiple_5) / len(multiple_5)):
        res_.append(math.sqrt(j))
    else:
        continue

print(res_)

