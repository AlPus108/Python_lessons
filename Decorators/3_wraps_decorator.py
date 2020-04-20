# Декоратор wraps

# Этот декоратор предназначен для того, чтобы сохранять методанные ф-и.
# Рассмотрим это на примере.


# Имеем ф-ю, которая вычисляет сумму квадратов
def squares_sum(a, b):  # принимает два аргумента
    '''

    :param a: Первое число
    :param b: Второе число
    :return: Сумма квадратов первого и второго числа: (a * a + b * b)
    '''
    return a * a + b * b  # возвращает сумму квадратов двух чисел.


# Делаем вызов ф-и с передачей параметров
print(squares_sum(2, 3))  # 13


# Далее, создадим ДЕКОРАТОР функций, который будет описывать любую ф-ю, к которой его подключат.
# Он будет передавать имя подключенной ф-и и ее документацию.
# Декоратор, значит, что его можно влкючить и отключить, когда это надо.
def print_function_data(function):
    '''

    :param function: Это декоратор функции
    :return:
    '''
    def wrapper(*args, **kwargs):
        print(f'Вы используете функцию {function.__name__}')
        print(f'Документация по функции: {function.__doc__}')
        return function(*args, **kwargs)
    return wrapper


# Для начала выведем документацию нашей ф-и без декоратора
print(squares_sum(2, 3))  # 13
print(squares_sum.__name__)  # squares_sum
print(squares_sum.__doc__)
#     :param a: Первое число
#     :param b: Второе число
#     :return: Сумма квадратов первого и второго числа: (a * a + b * b)


# Теперь задекорируем нашу ф-ю, то есть подключим к ней декоратор
@print_function_data  # подключили декоратор
def squares_sum_1(a, b):
    '''

    :param a: Первое число
    :param b: Второе число
    :return: Сумма квадратов первого и второго числа: (a * a + b * b)
    '''
    return a * a + b * b  # возвращает сумму квадратов двух чисел.


# Делаем вызов ф-и с подкюченным к ней декоратором
print(squares_sum_1(2, 3))  # 13
# Благодаря использованию декоратора, мы получаем полную информацию о ф-и, которую используем:
# Вы используете функцию squares_sum_1
# Документация по функции:
#
#     :param a: Первое число
#     :param b: Второе число
#     :return: Сумма квадратов первого и второго числа: (a * a + b * b)
#
# 13


# Но, что будет, если мы теперь захотим напрямую обратиться к документации ф-и?

@print_function_data  # подключили декоратор
def squares_sum_2(a, b):
    '''

    :param a: Первое число
    :param b: Второе число
    :return: Сумма квадратов первого и второго числа: (a * a + b * b)
    '''
    return a * a + b * b  # возвращает сумму квадратов двух чисел.

# Допустим, мы разработчики и хотим использовать ф-ю, разработанную кем-то.
# Для этого надо ознакомиться с ее доками ЕЩЕ ДО ЕЕ ВЫЗОВА

# print(squares_sum_2(2, 3))  # ф-я не вызвана
print(squares_sum_2.__name__)  # squares_sum
print(squares_sum_2.__doc__)
help(squares_sum_2)
# Получили:
# wrapper
# None
# Help on function wrapper in module __main__:
#
# wrapper(*args, **kwargs)

# То есть, мы не получаем по нашей ф-и то, что нам нужно, а получаем информацию по внутренней ф-и декоратора - wrapper
# И это нас не устраивает, так как нам нужа информация по нашей подключенной к декоратору ф-и.
# Это очень важно, так как, если мы разрабатываем библиотеку для других разработкиков, нужно, чтобы люди получали
# корректную информацию о нашей ф-и.
# К счастью, в Пайтоне есть модуль functools, который содержит ф-ю wraps
# Импортируем ее

from functools import wraps
# И, теперь, мы можем использовать эту ф-и в наших декораторах.
# Мы обораиваем этим wraps внутреннюю ф-ю wrapper декоратора, чтобы наши данные нашей исходной ф-и не терялись

def print_function_data_2(function):
    '''

    :param function: Это декоратор функции
    :return:
    '''
    @wraps(function)  # подключаем wraps к wrapper и в аргументы передаем аргументы ф-и print_function_data_2
    def wrapper(*args, **kwargs):
        print(f'Вы используете функцию {function.__name__}')
        print(f'Документация по функции: {function.__doc__}')
        return function(*args, **kwargs)
    return wrapper

# Теперь смотрим вывод

@print_function_data_2  # подключили декоратор
def squares_sum_3(a, b):
    '''

    :param a: Первое число
    :param b: Второе число
    :return: Сумма квадратов первого и второго числа: (a * a + b * b)
    '''
    return a * a + b * b  # возвращает сумму квадратов двух чисел.

# print(squares_sum_3(2, 3))  # ф-я не вызвана
print(squares_sum_3.__name__)
# squares_sum

print(squares_sum_3.__doc__)
#     :param a: Первое число
#     :param b: Второе число
#     :return: Сумма квадратов первого и второго числа: (a * a + b * b)

help(squares_sum_3)
# Help on function squares_sum_3 in module __main__:
#
# squares_sum_3(a, b)
#     :param a: Первое число
#     :param b: Второе число
#     :return: Сумма квадратов первого и второго числа: (a * a + b * b)



# Получаем полную информакцию о нашей исходной ф-и и документацию из нее.
# То есть, при помощи простой записи в декораторе @wraps(function) мы можем сохранять мета-данные нашей ф-и
# и свободно получать к ним доступ.