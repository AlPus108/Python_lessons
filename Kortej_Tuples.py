# КОРТЕЖ / TUPLES
# Очень похож на List / Список, но в отличии от Листа, он неизменяемый.
# Если он создан, вы не можете изменить его содержимое.
# За счет его неизменяемости удается достичь многих положительных характеристик в скорости и в объеме памяти, которые
# занимаем Кортеж. То есть, те же самые объекты, которые храняться в списке, будут занимать гараздо меньше памяти,
# а доступ к ним будет осуществляться гараздо бустрее, если хранить их в Кортежах.
# Для Тапл применяеются ф-и и методы, аналогичные Листу. Все ф-и Листа можно применять и к Тапл.

# Различия между Тапл и Списками
# КАРТЕЖ                                                    СПИСОК
# Хранит неизменяемые объекты                               Хранит изменяемые объекты
# Объекты не могут быть изменены после создания             Объекты могут быть изменены после создания
# Занимает мало памяти                                      Занимает много памяти
# Хранится единым блоком в памяти                           Хранится в двух блоках памяти (Один с неизменяемым размером,
#                                                           и второй с изменяемым для добавления данных)
# Создание Талп заниммет меньше времени чем Лист            Создание листа занимает многоо времени, которое требуется
#                                                           для доступа к двум блокам памяти
# Элементы в Тапл не могут быть изьяты или перемещены       Элементы в Листе могут быть изъяти или перемещены
# Тапл хранит данные в круглых скобках ()                   Лист хранит данные в квадратных скобках []

# В отличии от Списка Тапл инициализируется круглыми скобкамми
tuple_0 = (1)  # получим не tuple. это int
print(type(tuple_0))  # <class 'int'>
# Чтобы получить int, надо поставить ','
tuple_0 = (1,)  # получаем tuple
print(type(tuple_0))  # <class 'tuple'>

tuple_1 = (1, 2, 3)
tuple_2 = ('obe', 'hello', 'car')
# Тапл также может содержать элементы разных типов
tuple_3 = (3, 1.2, 'tree')

# Вывод Тапл на печать
print(tuple_1)
print(tuple_2)
print(tuple_3)
# Вывод:
# (1, 2, 3)
# ('obe', 'hello', 'car')
# (3, 1.2, 'tree')

# Хотя общепринятая структура создания Тапл, это внешние круглые скобки, но можно создавать Тапл и без скобок

tuple_4 = 10, 20, 30
print("Вывод Тапл без скобок ", tuple_4)  # Вывод:  (10, 20, 30)
# Скобки подставляются автоматически, так как это все равно класс tuple
print('Проверяем тип Тапл', type(tuple_4))  # Вывод: <class 'tuple'>  - даже без скобок это все равно класс tuple
# Скобки подставляют для визуализации типа, чтобы было более понятно, что это Тапл.
# Поэтому рекомедуется всегда использовать скобки.
# Но, если вы увидите объект без скобок, вы должны понимать, чо это Тапл

# Тапл не изменяемый, то есть мы не можем присвоить ему новое значение.
# Обращение к элементам Тапл происходит также, как и в Листе - по индексу. Ничем не отличается.
# Тапл - это упорядоченая последовательность. Нумерация индексов в Тапл начинается также с 0.
print('Получаем значение второго элемента Тапл', tuple_1[1])  # Получаем значение второго элемента, указывая индекс 1
# Но, если мы захотим изменить этот элемент
# tuple_1[1] = 3 - получим сообщение об ошибке: TypeError: 'tuple' object does not support item assignment
# Это та же ошибка, которую мы получали и в Строках при попытке изменить их содержимое.
# Для изменения содержимого, нужно создавать новую переменную типа Тапл и, извлекая из существующего Тапл элементы,
# присваивать их новому Тапл
new_tuple = (tuple_1[0], 3, tuple_1[2])  # таким образом вставляем новый элемент
print('Выводим новый список Тапл ', new_tuple)  # Вывод:  (1, 3, 3)  - вставили новый элемент
# То есть, мы не изменили tuple_1, а создали новый объект new_tuple

# В Тапл можно обращаться и по отрицательому индеусу, считать с конца, как в Листах
new_tuple = (tuple_1[0], 3, tuple_1[2], tuple_1[-1])  # добавляем в конец саиска новое значение
print('Добавляем в Тапл новое значене по отлицательому индексу ', new_tuple)  # Вывод: (1, 3, 3, 3)

# Возникает вопрос: зачем же нужны объекты Тапл, если можно испльзовать Лист, которые на много удобнее?
# Дело в том, что иногда надо, чтобы какие-то данные были не подвержены изменениям, чтобы какой-то набор данных
# не был нарушен. В этом случае применяется тип Тапл

person = ('John', 'Smith', 1986)  # Здесь записаны личные данные человека и они не будут меняться в течении
# всего периода работы программы. Поэтому есть смысл записать их в тип Тапл.
# Структура Тапл повзволяет сохранять данные целостными.

# ----------------- Приведение типов --------------------------
# Из Листа можно создать Тапл
list_1 = [1,2,3]
tuple_6 = tuple(list_1)  # Создаем новую переменнюу Тапл и присваиваем ей значения из Листа с приведением типов
print('Преобразование Лист в Тапл', type(tuple_6))  # Вывод: <class 'tuple'>

# ------------------- !!!!!! ТРЮК !!!!!! -----------------------------------
# Если возникает необходимость поменять что-то в Картеже, его преобразовывают в Лист
# То есть та же операция, только обратная
tuple_7 = (1,2,3)
list_2 = list(tuple_7)
print('Преобразование Тапл в Лист', type(list_2))  # Вывод: <class 'list'>
# Затем уже изменненный Лист конвертируют обратно в Тапл

# ----------------- Извлечение данных ------------------------------

# Есть один очень удобный способ извлечения данных из объектов Тапл
# Это называется "Распаковка данных в Талп"
# В Питоне есть такая фича, как присваивание нескольким переменым несколько значений.

x = y = z = 12
print('Вывод нескольких параметров одновременно ', x, y, z)  # Вывод: 12 12 12

# Если мы хотим назначить переменным разные значения?
# Обычно мы делаем это построчно - каждой перменной отдельно присвоить по значению.
# А можно сделать в одной строке, только через запятую присвоить значения.

x, y, z = 12, 13, 14  # Таким образом происходит множественное присваивание значений в одной строке.
# Это удобная фича языка Питон. Имено это мы можем использовать при распакове - извлечения данных из объектов Тапл.
# У нас есть имя, фамилия и год рождений в объекте person. Мы можем создать переменные для извлечения этих данных.
first_name, last_name, year_of_birth = person

# Далее выводим переменные на экран
print(first_name, last_name, year_of_birth)  # Вывод: John Smith 1986
# Теперь мы имеем в этих переменных данные, которые были извлечены из объекта Тапл.
# То есть, мы распаковали этот объект Тапл в переменные.

# Еще пару методов, которые можно применять к Тапл.

# ----------------------------- Метод count() ----------------------------

t1 = (1, 2, 5, 1, 7, 9)
# Мы можем посчитать количество элементов в Тапл с помощью метода count().
# Этот метод возвращает количество элементов, которые мы укажем в параметрах этого метода.
print(t1.count(1))  # Мы хотим знать, сколько раз встречается в этом объетке Тапл цифра 1

# То же самое можно проделать и для строк.
greetings_tuple = ('hello', 'hi', 'hey', 'hi')
print(greetings_tuple.count('hi'))  # Вывод: 2
# Если мы укажем объект, которого нет в Тапл, в выводе получим 0

# ---------------------------------- Метод index() -----------------------------

# Позволяет вычислить индекс указанного элемента

print('Индекс элемента Тапл \'5\' - ', t1.index(5))  # Вывод: 2
print('Индекс элемента Тапл \'hey\' - ', greetings_tuple.index('hey'))  # Вывод: 3

# Что будет на выходе, если элемент встречается в строке несколько раз?

print('Индекс повторяющегося элемента Тапл \'1\' - ', t1.index(1))  # Вывод: 0
print('Индекс повторяющегося элемента Тапл \'hi\' - ', greetings_tuple.index('hi'))  # Вывод: 1
# На выходе мы получаем идекс только первого элемента из повторяющихся.
# Если нам надо получить сумму всех повторяющихся элементов, это можно получить с помощь. циклов.

# ------------------------ Итерация по Тапл ------------------------

temp_tuple = (1, 2, 3)
for i in range(len(temp_tuple)):
    print(temp_tuple[i])

# Перевод вводимых цифр типа int в тип tuple
numbers = tuple(int(n) for n in input().split())

# ------------------- Функции Тапл ------------------

# Те же, что и в Списках

# ------------------ Операции c Тапл ---------------

# Те же, что и в Списках

# ------------------ Методы Тапл ------------------

# Те же, что и в Списках

# --------------------- Нюансы -------------------
# Хранение в памяти
# Имеем совершенно два одинаковых по содержанию объекта: Лист и Тапл

t_list = [1,2,3]
t_tuple = (1,2,3)

# С помощью атрибута __sizeof__() проверим объем памяти, которые они занимают

print(t_list.__sizeof__())   # Вывод: 32 байта
print(t_tuple.__sizeof__())  # Вывод: 24 байта
# Видим, что Тапл занимает меньше памяти в сравнении с Листом.







