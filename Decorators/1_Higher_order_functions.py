# Higher order functions
# 1
# Перед разбором декараторов мы должны разобрать концепцию Higher order functions
# Переводится, как 'Функции высшего порядка'
# Это те ф-и, которые могут принимать в качестве аргументов другие ф-и, либо возвращать после return другую ф-ю.

# --------------------- Использование собственной ф-и в качестве аргумента ------------------------

# Рассмотрим такую ф-ю
def product(n, func):  # здесь одним из аргументов является ф-я -> 1/1
    # 2
    result = 1
    for number in range(1, n):  # для всех чисел из диапазона n (range от 1, т.к. если будет от 0, то result обнулиться)
        result *= func(number)  # к каждому числу диапазона n применяем ф-ю func,
        # т.е. будут перемножаться квадраты чисел диапазона n
    return result  # -> 3


# 4
# Создадим еще одну ф-ю
def cube(x):
    return x * x * x  # -> 5


# 1/1
# Так как мы принимаем в качестве параметра другую ф-ю, мы должны ее создать
# Например, мы перемножаем квадраты каких-то чисел

def square(x):
    return x * x


# Теперь мы можем передать эту ф-ю в качестве параметра -> 2

# 3
# Вызываем ф-ю и передаем ей параметры
print(product(3, square))  # здесь мы передаем имя ф-и square без скобок.
# Мы ее здесь не вызываем, а передаем в качестве параметра, чтобы затем использовать ее внутри ф-и product,
# где она уже вызывается.
# Получаем 4
# Почему?
# Первое число из этого диапазона 1, второе число - 2, третьего числа у нас нет.
# То есть, перемножаются квадрат единицы = 1 и квадрарт 2 = 4, 1 + 4 = 4
# Если передадим в качестве параметра число 4
print(product(4, square))  # получаем 36, потому что еще добавляется 3. 1, 2, 3
# Ф-я работает правильно.
# То есть, мы можем передать сюда любое имя ф-и и использовать внутри нашей ф-и  -> 4

# 5
# Вызываем ф-ю cube
print(product(4, cube))  # 216 - это уже произведение трех произведений x


# Также, мы можем использовать для передачи в качестве аргумента ф-ю не только созданную нами, но и встроенную ф-ю

# ----------------------- Встроенная ф-я в качестве аргумента -------------------------------

def my_function(a, b, func):
    result = func([a, b])  # передаем аргументы в форме листа (iterable) для ф-и sum
    return result


print(my_function(2, 3, sum))  # передаем встроенную ф-ю sum()

# Итак, мы рассмотрели, как можно передавать другие ф-и в качестве аргумента.
# Теперь рассмотрим случай, когда можно использовать внутри одной ф-и другую вложенную ф-ю.

# ----------------------------------- Использвание вложенной ф-и ---------------------------------------

# Возвращаем результат вложенной ф-и -> 5/1

# 6
from random import choice  # -> 7


# 5/1
def colorize(thing):  # в качестве параметра передаем какой-то предмет
    # внутри этой ф-и будем использовать другую ф-ю
    def get_color():
        colors = ('red', 'green', 'yellow')
        # далее будем использовать ф-ю choice() для случайного выбора. Для этого ее импортируем из модуля random -> 6
        # 7
        color = choice(colors)  # случайный выбор цвета
        return color

    result = get_color() + ' ' + thing
    return result


# Теперь что-нибудь окрасим
print(colorize('apple'))


# Возвращаем саму вложенную ф-ю

# Также, мы можем возвращать не какой-то результат, а саму ф-ю
def make_color():
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)  # случайный выбор цвета
        return color

    return get_color  # здесь возвращаем ф-ю, причем без скобок. То есть, здесь мы ее не вызываем.


first_color = make_color()  # в эту переменную будет помещено возвращаемое значение ф-и get_golor
print(first_color())  # здесь мы неявно вызываем ф-ю get_color таким немного странным образом

second_color = make_color()
print(second_color())

third_color = make_color()
print(third_color())


# Мы можем получать доступ из внутренней ф-и к параметрам внешней ф-и.

def colorize_1(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing  # параметр вшенней ф-и передаем во внутренюю ф-ю.
    return get_color  # возвращаем ф-ю без вызова (без скобок), но, можно и со скобками, тогда вызов будет сразу.


print(colorize_1('apple')())  # чтобы вызвать ф-ю, добавляем круглые скобки в конце
# (так как она не вызвана при возвращении).

# Либо, в начале, перед вызовом, присвоить ее значение переменной
colorize_dog = colorize_1('dog')
print(colorize_dog())  # здесь, применяя скобки запускаем ф-ю.

# Что здесь важно.
# Параметр 'thing' неопределен внутри ф-и get_color, там мы его не имеем, но мы его имеем
# из внешнего скоупа ф-и colorize_1

# Мы рассмотрели все эти концепции построения ф-й для того, чтобы было легче понять декораторы.
# Так как декораторы, это те же ф-и, которые испльзуют все эти рассмотренные выше концепции.

