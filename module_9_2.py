# class Rect:
#     def __init__(self, a):
#         self.a = a
#
#     def __call__(self, b):
#         return f'Стороны: {self.a}, {b} \n' f'Площадь = {self.a * b}'
#
#
# def math_functions(operation):
#     if operation == "dividing":
#         def dividing(x, y):
#             if y == 0:
#                 raise ZeroDivisionError(f'Division by zero')
#             else:
#                 return x / y
#
#         return dividing
#     elif operation == "multiplication":
#         def multiplication(x, y):
#             return x - y
#
#         return multiplication
#
#
# square = lambda x: x ** 2
#
#
# def square_fun(x):
#     return x ** 2
#
#
# try:
#     print(f'Задача 1: Фабрика функций')
#     my_func_multiplication = math_functions("multiplication")
#     my_func_dividing = math_functions("dividing")
#     print(my_func_multiplication(7, 4))
#     print(my_func_dividing(18, 3))
#     print(my_func_dividing(18, 0))
# except ZeroDivisionError as e:
#     print(f'Error: {e}')
#
# print(f'Задача 2 лямбда')
# print(square(4))
# print(square_fun(4))
# print(f'Задача 3: Вызываемые объекты')
# rect = Rect(3)
# print(rect(4))
####################################################################

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

third_result = {name: len(name) for name in [*first_strings, *second_strings] if len(name) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)
