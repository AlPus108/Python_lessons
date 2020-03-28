# В Пайтоне есть два вида ф-й: Встроенные и личные ф-и пользователей
# Все они реализуют какой-то функционал. Ф-я print() реализует функцию вывода на печать,
# ф-я set() реализует функционал создания нового множества.

# Кроме кроме этого, в Пайтоне есть и встроенные методы. Метод, это еще одно назавние ф-и.
# Методы, это ф-и, которые существуют у объектов. Если у нас есть какой-то объект
my_list = [1, 2, 3]
# мы можем вызывать для него различные методы в зависимостит от типа объекта
# Если поставить точку рядом с именем объекта, появится список ф-й, которые можно к нему применить
my_list.append(4)  # в скобках мы передаем параметр/аргумент, который эта ф-я обрабатывает
print(my_list)  # [1, 2, 3, 4]

# Также у объектов есть методы без параметров. Они не принимют никакие аргументы,
# а просто выоплняют какие-то действия над объектами
my_list.clear()
print(my_list)  # []

# В Пайтоне есть огромное количество встроенных ф-й и методов.
# С ними можно ознакомиться в документации на сайте docs.python.org
# Или набрать в браузере: python documentation built in functions (документация по встоенным функциям)
# Здесь всегда самая свежая информация. А документация для программиста является священным писанием.

# ----------------------- Создание собственных функций ------------------------------

# Мы также можем создавать свои ф-и, реализовывая функционал, нужный нам.
# Ф-и существенно упрощают жизнь программистам
# С помощью ф-и можно структурировать свою программу, разбив ее на логически завершенные части.
# Каждый раз, когда у вас в программе встречаесят код, который выполняет какое-то действие и которое вы можете описать,
# имеет смысл это действие выделить в отдельную функцию. И дальше эту функцию можно переиспользовать.
# Благодаря ф-ям можно понять свою программу. С помощью ф-и можно создать какие-то новые примитивы, операторы
# внутри вашей программы. При этом, когда у вас появляется ф-я, вы можете абстрогироваться от того, как эта ф-я
# реализована, так как один раз вы ее уже реализовали и дальше вы просто помните, что она делает, что она получает
# в качестве аргументов, что она возвращает в качестве значений. После единожды описанного случая, вы можете уже
# использовать эту ф-ю в программе много раз. То есть появляется возможность переиспользования кода.

# Функция объявляется с помощью ключевого слова def (define - определять)
# Имя ф-и должно нести какую-то смысловую нагрузку
# После имени выставляем круглые скобки. Именно это указывает на то, что это ф-я.
# Ф-я может получать параметры, а може и не получать.

# Ф-я без параметров
# def print_greeting():
#     print('Запускаем ф-ю ', 'Hello!')  # Запустив эту ф-ю, мы ничего не получим.
# # Дело в том, что мы пока только определили ф-ю. Чтобы ее запустить, надо ее вызвать. То есть, написать ее имя в строке.
# print_greeting()

# Эта ф-я простая и мы знаем, что она делает. Но, обычно для ф-и пишут docstring - документацию к ф-и для того,
# чтобы другие программисты могли разобраться в ее работе. (Но, это не обязательно)
# Делается это при помощи тройных кавычек. Если их поставить в тело ф-и

def print_greeting():
    '''
    Print 'Hello!' text
    :return:  None
    '''
    print('Запускаем ф-ю ', 'Hello!')
    # в конце описания слово return вставляется автоматически, и, если ф-я ничего не возращает, ставим слово None
print_greeting()
# Далее мы можем посмотреть этот docstring в нашей программе. Это делается при помощи встроенной в Пайтоне ф-и help()
help(print_greeting)  # Внутри указываем имя ф-и, но без скобок
# Вывод:
# print_greeting()
#     Print 'Hello!' text
#     :return:  None
# Это удобно, когда мы создаем какие-то сложные ф-и. Человек, который хочет воспользоваться ф-ей, может для начала
# вызвать ф-ю help() для этой ф-и, просмотреть документкию. Если ему подходит эта функциональность,
# он может ее использовать.

# Некоторые ф-и возвращают какое-то значение. Результать работы такой ф-и мы можем присвоить какой-то переменной
# либо как-то использовать в программе.

def print_greeting_with_name(name):
    '''
    :param name:   # подставляется автоматически. Подсказывает, какие параметры мы можем передать ф-и.
    :return: None  # ф-я ничего не возвращает
    '''
    print('Hello, ' + name + '!')
# Вызываем ф-ю
print_greeting_with_name('Alex')

help(print_greeting_with_name)
# Запустив help для этой ф-и, получаем инфу, что у нее параметр name и она ничего не возвращает.
# :param name:
# :return: None
# Что значит не возвращает?
# Если мы попробуем присвоить какой-то переменной результат этоф ф-и
# x = print_greeting_with_name('Alex')
# и затем попробовать вывести ее на экран: print(x)
# результатом будет None

# Если выведем эту ф-ю без параметров, получим сообщение об ошибке - не хватает одного аргумента.
# Чтобы обезопасить себя от таких ошибок, мы можем создать для этой ф-и аргумент по умолчанию:
# def print_greeting_with_name(name = 'Name'):
# После этого, если ф-ю выведем без параметра, получим в выводе: Hellow Name! То есть, ошибки не возникает.
# При введении параметра, он будет подставляться вместо дефолтного параметра.

# Это были простейшие ф-и, которые выводят что-то на экран. Но, очень часто ф-и должны возвращать
# результат вычислений каких-то выражений, либо результат произведения каких-то действий, которые мы можем
# поместить либо в переменную, либо передать в какую-то другую ф-ю

# Создадим ф-ю с возвращаемым результатом

def min2(a, b):  # имя ф-и может быть произвольной, первый символ не должен быть цифрой
    # аргументов у ф-и может быть произвольное количество
    if a < b:
        return a  # ключевое слово return возволяет завершить выполнение ф-и и вернуться в место вызова ф-и
    else:
        return b

# Вызов ф-и
# Функция должна быть объявлена раньше ее первого вызова!
# Обычно описание всех ф-й помещают в начало программы и дальше идет код с их использованием

m = min2(42, 54)  # пишем имя ф-и и передаем ей два аргумента.
# Аргументами могут быть не только числа, но и выражения a*b-5 b т.д. Программа подставит эти выражения
# в качестве значений параметров.
print(m)

# Вызов ф-и можно использовать несколько раз

m = min2(min2(42, 30), 25)  # в аргументах можно вызывать любую другую ф-ю
print(m)


# Функция сложения двух чисел
def sum_of_two_numbers(a = 0, b = 0):  # Вводим парамптры по умолчанию
    '''

    :param a: Первое слагаемое
    :param b: Второе слагаемое
    :return: Сумма двух чисел
    '''
    return a + b  # складываем два переданных числа и используем return для возврата значения

# Через присвоение переменной вызываем эту ф-ю
x = sum_of_two_numbers(150, 372)  # передаем в ф-ю два аргумента
print(x)  # выводим на экран
# Эта ф-я возвращает результат
# Выводим через help() описание этой ф-и
help(sum_of_two_numbers)
# sum_of_two_numbers(a=0, b=0)
#     :param a: Первое слагаемое
#     :param b: Второе слагаемое
#     :return: Сумма двух чисел
# Если мы вызовем эту ф-ю без параметров, мы получи нулевой результат, но не ошибку.


# ------------------- Ньансы ----------------------

# Функция может не возвращать никакого значения. В привычном понимании, это скорее не ф-я, а процедура.
# Мы выделяем некий логически завершенный фрагмент программы в ф-ю и даем ей какое-то имя
# и эта ф-я выполняет некий набор действий. Напрммер, она может выводить какое-то справочное сообщение.
# В этом случае ф-я может в принципе не содержать слово return,
# или может содержать, но после него никакого значения не ставится. Она не возвращает никакого значения.

# Есть ф-и, которые не принимают никаких параметров. В этом случае в круглых скобках ничего не будет.
# def fun():

# Функция может иметь произвольное число параметров. Например print(a, b, c....).


# ------------------- Реализация собственых функций -----------------------------------

# Обычнго ф-и решают какие-то проблемы.
# Например, мы хотим узнать, находится ли какая-то строка в каком-то тексте
def is_hello_in_text(text):
    if 'hello' in text.lower():  # переводим переданный текс в нижний регистр
        return True
    else:
        return False
print(is_hello_in_text('Say hello everyone'))  # True

# Здесь все работает правильнро, но это можно записать намного короче
# Оператор in возвращает True или False в зависимости от того, содержится ли какой-то элемент в последовательности
# или нет. Поэтому, нам не обязательно использовать оператор if. Можно сразу писать 'hellow' in text.
# Если элемент содержится в тексте, мы получим True, если же нет - False

def hello_in_text(text):
    return 'hello' in text.lower()  # Мы сразу же возвращаем результат проверки
print(hello_in_text('hello everyone!'))  # True

# Эта ф-я немного ограничена, так как она проверяет только наличие в тексте слова 'hello'
# Мы можем создать подобие такой ф-и, но с двумя параметрами. Первый параметр - строка, наличие которой будет
# проверяться в тексте, а второй параметр - сам текст.

def is_string_in_text(string, text):
    return string in text
print(is_string_in_text('he', 'The apple'))  # строка, которую ищем и текст, в котором ищем
# Получаем True, так как в тексте содержится эта строка.


# Ф-и так же могут не только либо возвращать аргумент, либо производить какие-то действия
# Ф-и могут делать и то и другое одновременно

# Создадим ф-ю, которая будет выводит на экран нужное приветствие, в зависимости от пола М или Ж, который мы будем
# передавать в качесте параметра. И также будет возвращать пол.

def greeting_depends_on_gender(name, gender):
    if gender == 'male':
        print('Hello ', name, '! You look great!')
        return gender
    elif gender == 'female':
        print('Hello ' + name + 'You are so nice!')
        return gender
    else:
        print('Hello! ' + name + 'Ive never seen the creatur like you!')
        return gender
returned_value_1 = greeting_depends_on_gender('Jack ', 'male')
returned_value_2 = greeting_depends_on_gender('Jane', 'female')
returned_value_3 = greeting_depends_on_gender('Ja ', 'cemale')
# Вывод:
# Hello  Jack  ! You look great!
# Hello JaneYou are so nice!
# Hello! Ja Ive never seen the creatur like you!

# Однажды записав эту ф-ю, мы можем вызывать ее многократно, в любом месте программы через короткий вызов.
# Это намного урощает написание и чтение кода.

# Если в ващей ф-и, помимо ключевого слова return есть еще какой-то код, он должен быть написан до слова return
# Так как return прерывает выполнение ф-и и передает выполнение программы следующему за ф-ей коду.

# Теперь посмотрим, что возвращают эти ф-и

print(returned_value_1)
print(returned_value_2)
print(returned_value_3)
# Вывод:
# male
# female
# cemale


# Функция поиска минимального значения в последовательности

def min(*a):  # - "звезда" означает, что ф-я принимает произвольное число аргументов.
    # все эти аргументы будут накапливаться в последовательности с именем 'a'
    # к этой последовательности мы можем обращаться с помощью инддексов
    # и можем итерироваться в этой последовательности с помощью цикла for, также, как в списке
    m = a[0]  # запоминаем первое значение последовательности и далее в цикле сравниваем его с остальными
    for x in a:
        if m > x:
            m = x
        return m


# Эту ф-ю можно вызывать с произвольным числом аргументов

# Функции могут иметь значения параметров по умолчанию.
# Например, print(). end=''

# Здесь рассмотрена модификация ф-и range(). Однако стандартная ф-я range(), в отличии от этой, не возвращает список,
# она хранит в себе специальное значение, по которому можно итерироваться.
# В данном случае наша ф-я возвращает список.
# Вызывая ф-ю с параметрами my_range(2, 5), ожидаем увидеть список [2, 3, 4].
# Вызывая ф-ю с шагом my_range(2, 15, 3), ожидаем увидеть список [2, 5, 8, 11, 14].
# Также с отрицательным шагом my_range(15, 2, -3), на выходе [15, 12, 9, 6, 3]
def my_range(start, stop, step=1):  # здесь указывается диапазон значений (start - stop) - обязательные аргументы
    # step - необязательный аргумент. Это размер шага, который по умолчанию = 1
    # таким образом все аргументы ф-и проинициализированны. Реализация ф-и не зависит от значения step
    res = []  # пустой список, в который накаливаются элементы, которые нужно будет вернуть.
    # далее рассматриваются две ситуации: step > 0 и step < 0
    if step > 0:  # если степ положительный
        x = start  # инициализируем стартовое значение
        while x < stop:  # идем от старта к стопу
            res += [x]  # добавляем текущий элемент в список
            x += step  # увеличиваем значение х на величину шага
    elif step < 0:  # если степ отрицательный
        x = start
        while x > stop:  # идем от стопа к старту
            res += [x]
            x += step
    return res  # получаем результат


# Неявный вызов ф=и
my_range(5, 20)

# Явный вызов ф-и
my_range(stop=20, start=5)


# Здесь порядок аргументов нарушен, но, благодаря явному указанию аргументов, все будет передано верно.


# ------------------ Локальные переменные ------------------------------

# Переменные, объявленные внутри ф-и, называются локальными. Их невозможно использовать вне функции.

def int_values():
    a = 100
    b = 200


# Значения переменных а и b могут быть использованы только внутри функции.

# Если у нас есть две переменные с одинаковым названием, изменения с переменной внутри ф-и происходят внутри
# этой функции и они не влияют на переменную вне ф-и, так как это две разные переменные
# Получается, что внутри ф-и мы не можем изменить значение переменной, которая снаружи
# Это не свосем так. Если у нас есть переменная с изменяемым значением, например список, мы можем изменять
# значение списка, если создать и запустить ф-ю, которая будет изменять значения переданного ей списка.

def append_zero(xs):
    xs.append(0)


# Имеем изначально пустой список а
a = []
append_zero(a)  # Вызываем ф-ю и передаем ей на вход пустой список. Она добавляет в него элементы
print(a)  # в списке появится один элемент с значением 0


# В общем случае надо всегда понимать, каким образом вы изменяете значение переменной.
# Одно дело, если вы берете объект и как-то изменяете его, например, добавляете значение 0,
# как в выше описанном способе.
# При создании переменной 'а' мы связываем ее с пустым объектом - список.
# Переменная xs ф-и, при выполнении этой ф-и, связывается с тем же самым объектом, что и переменая 'a'.
# и xs добавляет в список переменную 0. То есть мы изменили объект, с которым связана наша переменная 'а'.
# При выводе переменной на экран, увидим, что значение 'а' изменилось на 0.
# Но затем, если мы переменную xs внутри ф-и связываем с новым объектом

def append_zero(xs):
    xs.append(0)
    xs = [100]


# xs сначала добавляет 0 в ф-ю 'а', и затем связывается с новым списком (объектом), то старая связь уже нарушается,
# ее уже нет.
# Если мы такую ф-ю вызовем для списка 'а', то увидим, что подобное изменение внутри ф-и никак не повлияло на нашу
# переменную 'а'. При выводе на экран 'а', увидим, что она будет иметь значение 0.


# ------------------------ Глобальные переменные ----------------------------

# Переменные, объявленные вне ф-й, называются глобальными. Они могут использоваться во всей программе.
# У нас есть ф-я, внутри которой мы никак не инициализируем переменную 'а'

def print_value():
    print(a)


# Такое может работать, если мы перед вызовом этой ф-и, проинициализируем глобальную переменную 'а'

a = 5  # инициализируем переменную
print_value()  # вызываем ф-ю.


# Так как внутри ф-и зашита переменная 'а', интерпретатор будет искать ее снаружи ф-и,
# и найдя, выведет ее значение на экран

# Создавая конструкцию подобную этой, мы увидим сообщение об ошибке
# def print_value2():
#     print(x)  # х подчеркнута красным
#     x = 10
#     print(x)
# x = 5
# print_value2()

# Почему так происходит? Если мы внутри ф-и пытаемся изменить значение переменной x = 10 - присваиваем ей новое значение
# в этом случае переменная считается локальной, так как она находится внутри ф-и. Поскольку она считается локальной,
# поиск этой переменной не будет происходить среди глобальных переменных, поиск будет происходить внутри ф-и
# среди локальных переменных. А к этому моменту print(x) мы еще ее не проинициализировали.
# И это не смотря на то, что мы в дальнейшем при вызове функции, проинициализировали переменную 'а'.


def f(n):
    return n * 10 + 5


print(f(f(f(10))))  # На выходе: 10555


# ----------------- ЗАДАЧИ ----------------------

# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
# При x <= -2 --> 1 - (x + 2) ** 2
# При -2 < x <= 2 --> -x / 2
# При 2 > x --> (x - 2) ** 2 + 1

# Sample Input 1:
# 4.5
#
# Sample Output 1:
# 7.25
#
# Sample Input 2:
# -4.5
#
# Sample Output 2:
# -5.25
#
# Sample Input 3:
# 1
#
# Sample Output 3:
# -0.5

def f(x):
    # put your python code here
    if x <= -2:
        x = 1 - (x + 2) ** 2
        return x
    elif -2 < x <= 2:
        x = -x / 2
        return x
    else:
        x = (x - 2) ** 2 + 1
        return x


n = 4.5

print(f(n))


# --------------------------------------------------

# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два. Функция не должна ничего возвращать,
# требуется только изменение переданного списка, например:
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.

def modify_list(lst):
    # lst_2 = list(filter(lambda x: x % 2 == 0, lst))
    # print(lst_2)
    # lst = list(map(lambda x: x / 2, lst_2))
    for i in range(len(lst)-1):
        if lst[i] % 2 != 0:
            del lst[i]
    lst_3 = [int(i / 2) for i in lst]  # Возвращает тип float, поэтому переводим в int
    print(lst_3)

c = [10, 5, 8, 3]

modify_list(c)