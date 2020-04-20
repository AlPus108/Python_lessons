# Еще один пример использования декораторов

# При помощи декораторов мы можем ограничивать аргументы каких-то ф-й.
# Мы можем сделать такой декоратор, который будет, при передачи аргументов какого-то типа, вызывать какую-то ошибку
# Либо просто выходить из этой ф-и. То есть, давать какую-то нужную нам реакцию.

# Декораторы, это всегда wraps, поэтому сразу же его импортируем

from functools import wraps

# Например, создадим декоратор, который будет запрещать передавать аргументы **kwargs

def profibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('Аргументы ключей запрещены')
        return func(*args, **kwargs)
    return wrapper

# Создадим ф-ю для проверки декоратора
# @profibit_kwargs
def print_hello(name):
    print(f'Hello {name}!')

print_hello('Alex')  # Hello Alex!

#  Передадим параметр в стиле Словаря
print_hello(name='Alex')  # получаем то же самое Hello Alex!
# Но если ф-ю задекорировать, то декоратор не пропустит такой параметр
# ValueError: Аргументы ключей запрещены

# Таким образом можно проверять и ограничивать аргументы передаваемые в ф-ю.


# Создадим декоратор, который будет запрещать числовые аргументы

def prohibit_int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if type(value) == int:
                raise ValueError('Числовые аргументы запрещены')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Числовые аргументы запрещены')
        return func(*args, **kwargs)
    return wrapper


# Проверяем ее на той же, но слегка измененной ф-и и уже с числовым аргументом
@prohibit_int_args
def print_digit(name):
    print(f'Hello {name}!')


print_digit('sdf')  # если передать число, выдаст ошибку
# Hello 3! - вывод без декоратора
# ValueError: Числовые аргументы запрещены






