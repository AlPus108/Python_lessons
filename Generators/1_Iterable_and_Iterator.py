# Здесь разберем принцип работы итераторов(переборщиков)
# Iterate - перебирать
# Iterable - объект, элементы которого можно перебирать
# К таким объектам относятся строки, списки, словари, тьюпл, сеты
# Так же мы можем создавать свои собственные классы, которые также могут быть итереблс.

# Iterator - переборщик
# Существуют конструкции для перебора элементов.
# Самые известные, это циклы.

number_list = [1, 2, 3, 4, 5]

for number in number_list:
    print(number)

for letter in 'my_string':
    print(letter)

# Также, существует специальный метод для перебора элементов iter(), в аргументы которого передается объект для перебора

number_list_iterator = iter(number_list)
print(type(number_list_iterator))  # <class 'list_iterator'> - это отдельный класс list_iterator

# Также для строки
string_iterator = iter('my string')
print(type(string_iterator))  # <class 'str_iterator'> - это отдельный класс str_iterator

# Для чего нужны итераторы?
# Дело в том, что в циклах, например, не явно используются итераторы.
# Для итератора можно вызвать метод next(). Именно этот метод переходит к следующему элементу объекта Iterable
# При помощи него мы перебираем все элементы объекта Iterable
# То есть, элементы объекта Iterable перебираются с помощью итератора, а для итератора вызывается метод next()

# print(number_list_iterator.__next__())  # вызываем для объекта метод next и выводим на печать
# Вывод: 1
# То есть, мы получаем первый элемент этой последовательности
# Если повторить это несколько раз, каждый раз мы будем переходить к следующей последовательности
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# 1
# 2
# 3
# 4
# 5
# Если вызовем этот метод еще раз - получим ошибку StopIteration, так как в объекте закончились элементы для перебора.
# Как раз это не явно происходит в циклах

# Если же мы попробуем метод iter() вызвать для неперебираемого объекта, например для числа
# iter(1)
# Получим ошибку: TypeError: 'int' object is not iterable
# То же самое и для float, bool, char и тд

# Вместо метода next мы можем использовать функцию next(), передавая ею итератор в качестве параметра
print(next(number_list_iterator))  # 1
print(next(number_list_iterator))  # 2
print(next(number_list_iterator))  # 3
print(next(number_list_iterator))  # 4
print(next(number_list_iterator))  # 5


# Попробуем воспроизвести функциональность цикла for в функции


def my_for_loop(iterable):  # в качестве параметра передаем объект Iterable
    # в этой ф-и мы будем получать итератор и помещать его в одноименную переменную Iterator
    # итератор получается из Iterable при помощи ф-и iter()
    iterator = iter(iterable)
    # теперь мы можем вызывать для этого итератор либо метод, либо ф-ю next
    print(iterator.__next__())  # в результате мы будем получать первый элемент этого объекта Iterable



my_for_loop('hello')  # h - получаем первую букву


# Чтобы перебрать таким образом все элементы объекта, нам нунжо каждый раз вызывать iterator.__next__()
# Ну, или ф-ю next(number_list_iterator) с итератором в качестве параметра
# Но, мы не знаем, какая длина у объетка, поэтому, мы можем сделать, как это делается в цикле for
# при помощи блока try - except

# def my_for_loop_2(iterable):
#     iterator = iter(iterable)
#     while True:  # создаем бесконечный цикл
#         print(iterator.__next__())

# при запуске такого цикла получим ошибку StopIteration, потому что этот цикл бесконечный
# my_for_loop_2('hello')

# Чтобы эту ошибку обработать, помещаем в ф-ю блок try

def my_for_loop_2(iterable):
    iterator = iter(iterable)
    while True:  # создаем бесконечный цикл
        try:
            print(iterator.__next__())
        except StopIteration:  # здесь будем выходить из цикла в случае ошибки StopIteration
            print('Итерация закончена')
            break


my_for_loop_2('hello')
# Теперь в эту ф-ю мы можем передавать любой итеребл-объект.
my_for_loop_2([1, 2, 3, 4, 5])  # список

# Этот код, конечно, мы не будем использовать, так как у нас есть готовый цикл for
# На его примере мы разобрали, как работает итератор.