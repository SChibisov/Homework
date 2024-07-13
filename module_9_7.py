# -*- coding: utf-8 -*-

from math import sqrt


def is_prime(func):
    def wrapper(a, b, c):
        x = func(a, b, c)
        prime = True
        i = 2
        while i <= sqrt(x) and prime is True:
            if x % i == 0:
                prime = False
            i += 1
        if prime:
            return f'Число {x} простое'
        else:
            f'Число {x} составное'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
