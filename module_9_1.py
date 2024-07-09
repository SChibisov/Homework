# Старое домашнее задание
# def square(x):
#     return x ** 2
#
#
# def is_sort(x):
#     return x % 2
#
#
# num_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
#
# result = map(square, filter(is_sort, num_list))
#
# print(list(result))


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
