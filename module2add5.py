def func_nod(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b


list_values = [[5, 15], [5, 7], [21, 111], [63, 49], [78, 12], [56, 89], [123, 4], [98, 56], [2, 234], [32, 67]]

nod_result = []

for i in list_values:
    nod_result.append(func_nod(i[0], i[1]))

print(nod_result)
