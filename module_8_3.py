from string import ascii_letters

class person_age_er_diapozon(Exception):
    def __init__(self, age, min_age, max_age):
        self.age = age
        self.min_age = min_age
        self.max_age = max_age

    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
               f"Возраст должен быть в диапозоне от {self.min_age} до {self.max_age}."


class person_age_er_name(Exception):
    def __init__(self, name_person):
        self.name_person = name_person

    def __str__(self):
        return f"Недопустимое значение: {self.name_person}. " \
               f"Имя должно быть написано английскими буквами."


class Person:
    def __init__(self, name, age):
        self.__name = name
        min_age, max_age = 1, 110
        if min_age < age < max_age:
            self.__age = age
        else:
            raise person_age_er_diapozon(age, min_age, max_age)
        if all(map(lambda c: c in ascii_letters, name)):
            self.__name = name
        else:
            raise person_age_er_name(name)

    def display_info(self):
        print(f"Имя: {self.__name}  Возраст: {self.__age}")


try:
    name_1 = Person("Don", -28)
    name_1.display_info()
    denis = Person("Denis", 35)
    denis.display_info()
except person_age_er_name as n:
    print(n)
except person_age_er_diapozon as e:
    print(e)
else:
    print(f'Данные введы корректно.')
