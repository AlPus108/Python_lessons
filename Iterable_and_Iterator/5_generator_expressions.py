# Как создавать выражения генераторов
# До этого мы свами это делали при помощи функций генераторов
# Здесь научимся это делать при помощи generator expressions

# generator expressions по стилю записи очень похожи на List Comprehension, почти один в один.
# только List Comprehension записывается в квадратных скобках [], а generator expressions - в круглых ()

# Для начала создадим простую ф-ю генератора

def get_number_from_range():
    for number in range(10):
        yield number


# далее создаем переменную и присваиваем ей результат работы ф-и
counter = get_number_from_range()
# и дальше можем вызывать для этой переменной метод next() или ф-ю next
# для разнообразия вызовем ф-ю
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print(next(counter))  # 5
print(next(counter))  # 6
print(next(counter))  # 7
print(next(counter))  # 8
print(next(counter))  # 9
print(next(counter))  # 10
# пока не выйдем за пределы диапазона
# print(next(counter))  # StopIteration

# то же самое мы можем записать при помощи более короткой записи generator expressions

counter_1 = (number for number in range(10))
print(next(counter_1))  # 0
print(next(counter_1))  # 1
print(next(counter_1))  # 2
print(next(counter_1))  # 3
print(next(counter_1))  # 4
print(next(counter_1))  # 5
print(next(counter_1))  # 6
print(next(counter_1))  # 7
print(next(counter_1))  # 8
print(next(counter_1))  # 9
# пока не выйдем за пределы диапазона
# print(next(counter_1))  # StopIteration

# Если эту же запись мы повторим в кдваратрных скобках, мы получим список из диапазона
print([number for number in range(10)])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Но, при такой форме записи
print(number for number in range(10))
# мы можем получать генератор, который выдает одно число из этого диапазона.

# То есть, в counter у нас генератор, созданный при помощи ф-и генератора
counter = get_number_from_range()
print(counter)  # <generator object get_number_from_range at 0x036D0F40>
# В counter_1 у нас генератор, созданный при помощи generator expressions
counter_1 = (number for number in range(10))
print(counter_1)  # <generator object <genexpr> at 0x0356EAE0>
# здесь выводится, что этот counter_1 был создан <genexpr>  - генератором выражений.


