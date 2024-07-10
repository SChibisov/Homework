# class EvenNumders:
#     def __init__(self, start=1, end=0):
#         self.start = start
#         self.end = end
#         self.i = start - 1
#
#     def __iter__(self):
#         self.i = self.start - 1
#         return self
#
#     def __next__(self):
#         if self.i < self.end:
#             self.i += 1
#             return self.i
#         else:
#             raise StopIteration
#
#
# en = EvenNumders(10, 25)
# for i in en:
#     if i % 2 == 0:
#         print(i)
#################################################

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

res_first = [len(x) for x in first]
res_second = [len(y) for y in second]
first_result = ((len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
second_result = ((len(first[i]) == len(second[i])) for i in range(len(first)))

print(res_first)
print(res_second)
print(list(first_result))
print(list(second_result))
