# СТРОКИ

# Строка, это объект, хранящий текстовые данные. Он представляет собой массив символов
# str = 'HELLO' - это массив с нумерацией букв от 0 до 4
# К каждой букве мы можем обратиться по индексу
# str[0] = 'H'
# str[1] = 'E'
# str[2] = 'L'
# str[3] = 'L'
# str[4] = 'O'
# Строки имеют НЕИЗМЕНЯЕМЫЙ тип данных
# При попытке заменить букву в строке, будет выдана ошибка.
# Пробелы и знаки препинания также учитываются, как элементы строки

# С помощью инструмента "Срез" можно получать как часть строки, так и отдельный ее элемент
# [] - в скобках указываем, откуда начинается срез
# str[:] = 'HELLO' - получаем всю строку
# str[0:] = 'HELLO' - вывод строки с первого элемента до конца строки (также, получаем всю строку)
# str[:5] = 'HELLO' - вывод строки от первого до пятого (последнего по индексу) элемента (также, получаем всю строку)
# str[:3] = 'HEL' - вывод с первого до 3-го элемента (сам 3-й элемент не включается)
# str[0:2] = 'HE' - вывод строки с 1-го по 3-й элемент (3-й элемент не включается)
# str[1:4] = 'ELL' - вывод строки со 2-го по 4-й элемент (3-й элемент не включается)

# ------------------------------------------------------------------------
# ИНИЦИАЛИЗАЦИЯ СТРОКИ
# temp_str = ''
# temp_str = ""
#
# Если используем кавычки внутри текста, они долджны отличаться от кавычек снаружи.
temp_str = 'Машина марка "Вольво"'
# Или с помощью экранинрования, если кавычки повторяются
# auto_m = 'Машина марка \'Вольво\' '
# Все специальные символы в Питоне экранируются с помощью обратного слэша "\", в том числе и сам обратный слэш \\

# ------------------ ОБРАЩЕНИЕ К СИМВОЛАМ ------------------
# Вывод одной буквы
# print(temp_str[0])
#
# Вывод всей строки посимвольно в цикле
# for i in range(len(temp_str)):
#     print(temp_str[i])
# Здесь каждая буква будет выведена на отдельной строке
#
# -------------------- Обращение к символам через срезы --------------
# print(temp_str[1:4]) # получим 'аши'

# Обратная нумерация

# print(temp_str[1:])  # выводим все символы от 1 до конца
# print(temp_str[:4])  # выводим символы с начала до 4-го символа
# print(temp_str[1:-1])  # выводим все символы от 1 до -1(последний символ не включается)
# print(temp_str[1:-3])  # выводим все символы от 1 до -3(три последних символа не включаются)

# -------------------------- Функции строки ---------------------
# Их всего две:
#
# Вывод строки и Длина строки
print(temp_str, len(temp_str))

# ------------------------- ОПЕРАЦИИ СО СТРОКАМИ ------------------
temp_str_2 = 'Mersedes'  # переменная, с которой будем работать

# ------------------- Сложение строк -----------------------
print(temp_str + temp_str_2)
# Вообще не рекомендуесят пользоваться плюсом. Нужно пользоваться фарматированием (описано ниже).
# Так как "+" это трудоемкая операция
# ------------------ Умножение строк ----------------------
print(temp_str_2 * 2)  # данная строка сконкотирируется два раза

# ------------------- Форматирование строк ---------------------
# Строка, это неизменяемый тип данны. Поэтому, чтобы в строке что-то поменять, а иногда это требуется,
# необходимо фактически создавать новую строку. Форматирование, это создание новой строки.
brend = 'Volovo'
price = 1.5
car = 'Марка: {} цена: {}'.format(brend, price)  # используем ф-ю format()
print(car)  # выводим на экран
# в фигурные скобки будут вставлены значения, которые указываются дальше по строке
# Или же вместо имен переменных туда можно сразу подставить их значения.
# Если нам надо разместить элементы строки в поределенном порядке, можно в фиг.скобках (плейсхолдеры)
# указать их порядковые номера
week_days = 'В неделе 7 дней: {3}, {2}, {0}, {4}, {1}.'.format("Среда", "Пятница", "Вторник", "Понедельник", "Четверг")
print(week_days)  # В фигурных скобках указывается порядковый индекс элементов.
# Но, если значений очень много, их положение предтся высчитывать. Поэттому можно присвоить им ключи
week_days = 'В неделе 7 дней: {pn}, {vt}, {sr}, {ct}, {pt}.'.format(sr="Среда", pt="Пятница", vt="Вторник",
                                                                    pn="Понедельник", ct="Четверг")
# то есть, в качестве ключей созданы переменные, которым присвоины значения.
print(week_days)


# Вставка значения в формате float
float_rez = 1000 / 7
print(float_rez)  # Получаем на выходе: 142.85714285714286
# Явно, что нам не нужно такое большое количество дробных знаков. Нам хватит и трех. Как убрать остальные?
print('Результат флрматирования типа float: {0:10.3f}'.format(float_rez)) # На выходе:    142.857
# В фигурных скобках указываем количество знаков после точки с типом f. Перед точкой цифра 10 указываем на количество
# пробелов от последнего знака в строке. Цифра выведется с некоторым отступом. Это нужно для форматирования вывода,
# например в виде таблицы, чтобы выровнять цифры на одном уровне. Первая цифра 0 - индекс элемента.

print('''
{} {} {}
{} {} {}
{} {} {}
'''.format(1.215, 2.45525, 1.6326545, 53.3215, 564.32145, 32.21447, 987.3254, 98.214, 57.624))
# вывод на экран:
# 1.215 2.45525 1.6326545
# 53.3215 564.32145 32.21447
# 987.3254 98.214 57.624
# Видим, что цифры не выровнены.

# Поставим индексы
print('''
{0:10.2f} {1:10.2f} {2:10.2f}
{3:10.2f} {4:10.2f} {5:10.2f}
{6:10.2f} {7:10.2f} {8:10.2f}
'''.format(1.215, 2.45525, 1.6326545, 53.3215, 564.32145, 32.21447, 987.3254, 98.214, 57.624))
# Получаем выравнивание цифр по правому краю
#       1.22       2.46       1.63
#      53.32     564.32      32.21
#     987.33      98.21      57.62

# Форматирование строковых литералов (Появилось в версии Python 3.6)
# Это второй, более удобный способ форматирование строк - через декоратор f
car = f'Марка: {brend} цена: {price}'
# Вывод букв строки каждую в отедльности на отедельных строках
print('Вывод букв строки каждую в отдельности на отедельных строках', car)

name = 'Jack'
age = 23
name_and_age = f'My name is {name}. I\'m {age} years old.'
print(name_and_age)

# Еще одни старый способ форматирования, который применялся в Python 2
# Это форматирование с помощью оператора форматирования
print("Мое имя %s. Мне %d лет" % (name, age))   # s - указывает, что это строка, d - числовой формат
# Здесь также можно использовать не только переменные, но и значния
print("%s имя %s. %s %d лет" % ("Мое", name, "Мне", age))   # s - указывает, что это строка, d - числовой формат
# Но сейчас этот способ уже deprecated - не рекомендован к использованию. Но, он может еще встерчаться в старых кодах.

# Фарматирование строк гараздо эффективней метода сложения или умножения



# -------------------- МЕТОДЫ СТРОК -------------------------------

# Методов у строк достаточно много
# Часто требуется для парсинга строк разбиение строки на подстроки. Для этого создали метод split()
print(temp_str.split())
# Если не указывать какой-то конкретный знак разбиения, split разобьет строку по пробелам.
# Если вместо пробелов в стоке стоят, например, запятые, то этот метод не сработает, потому что нет пробелов
cars = 'Volvo,Audi,Lada'
print(cars.split())  # Здесь ничего не будет разбито
print(cars.split(','))  # но, если в аргументах указать разделитель ',', тогда все сработает

# --------------------- Методы форматирования строк ---------------
print(cars.upper())  # все буквы переводятся в верхний регист
print(cars.lower())  # все буквы переводятся в нижний регист
print(cars.title())  # все Первые Буквы слов в верхнем регистре

# Метод замены подстроки в строке методом replace()
email_adress = 'Mail: _mail_'  # _mail_ - это заглушка, которую надо поменять на реальный адрес
email = 'my_email@gmail.com'  # реальный адрес
print(email_adress.replace('_mail_', email))  # подстроку mail заменяем на emil

# Если нужно что-то сделать со строкой, ищите уже готовые реализации. Их очень много.

# -------------------------------------------------

# a = "ABCD"
# for i in range(4): # перебор символов строки в цикле
#     print(a[i])

# # или более удачная конструкция
# a = "ABCD"  # здесь нет явной индексации, как в предыдущем примере
# for i in a:  # перебор символов строки в цикле
#     print(i)
# #  такая конструкция вообще хорошо работает с любыми последовательностями

# ----------------------------------------

# # Сколько раз встречается символ в строке?
# a = 'ABBCABCC'
# x = 0
# for i in a:
#     if i == 'C':
#         x += 1
# print("Символ \'C\' в строке встречается ", x, " раза.")
#
# # второй способ (более короткий)
# a = 'ABBCABCC'
# print(a.count('C'))

# Строки, это объекты, которые имеют методы.
# В данном случае применяется функция(метод) s.count(p) - сколько раз символ 'p' (или слово) встречается в строке 's'


# ----------------------------- МЕТОДЫ СТРОК ----------------------------------

# s = 'aTGCC'
# p = 'cc'
#
# s.upper()  # заменяет все буквы в строке на большие. Если есть символы, которые не являются буквами, они игнорируются
# s.lower()  # заменяет все буквы в строке на маленькие. При этом сама строка s остается неизменной
# # метод возвращает результат, который можно присвоить другой переменной res = s.lower()
# s.count(p)  # подсчитывает, сколько раз подстрока р встерчается в строке s.
# # Рассматриваются только не перекрываютщиеся значения сссс - 2 сс; внутренее сс не рассматривается
# s.find(p)  # находит позицию подстроки р в строке s. Возвращает индекс первой буквы (первое вхождение).
# # Если такой подстроки нет в строке s, то результат  -1
# # Если мы хотим проверить входит подстрока в строку или нет, лучше использовать конструкцию if 'TG' in s: ...
# s.replace('c', 'C') # заменяет одни буквы на другие. При этом сама строка s остается не изменной.
# # Результат нужно присваивать переменной
#
#
# #  --------------------- ПОСЛЕДОВАТЕЛЬНЫЕ ВЫЗОВЫ МЕТОДОВ -------------------------------------
#
# S = 'agTtcAGtc'
# s.upper().count('gt'.upper())
# #  Первым шагом - изменяем все буквы на большие.
# # Второй шаг - поиск уже в изменненой строке сочетания 'gt', измененные на большие. Результат: 2
# ---------------------------------------------


'''
Напишите программу, которая вычисляет процентное содержание символов G и C в введенной строке
(программа не должна зависеть от регистра вводимых символов).

Например, в строке "acggtgttat" процентное содержание символов G и C равно (4/10)*100 = 40.0
где 4 -- это количество символов G и C,  а 10 -- это длина строки.
'''

# s = input().lower()
# print(s)  # проверяем, что все буквы в нижнем регистре
# p1 = 'g'
# p2 = 'c'
#
# x = len(s)  # длина строки
# x1 = s.count(p1)
# x2 = s.count(p2)
#
# print(((x1 + x2)/x)*100)

# -----------------------------------

# Как брать диапазон символов у строк
# Для этого существует механизм Slicing

# s = 'ATGTVS'
# x = s[1]  # берем второй символ строки с индексом 1 -> T (первый символ - индекс 0)
# x2 = s[1:4]  # берем диапазон символов строки с 1 по 4. При этом 4-й (последний символ не включается!)
# # в Питоне всегда левая граница влчается в интервал, правая не включается!
# x3 = s[:4]  # при взятии диапазона можно не указывать явно начало. Последний символ не включается в интервал!
# x4 = s[4:]  # аналогично, можно не указывать правую границу. Берем символы с 4-го до последнего
# x5 = s[-4:] # берем отрицательный индекс. Делаем выборку начиная с 4-го символа с конца и остальные до конца строки
# x6 = s[1:-1] # указываем обе границы, при этом символы могут быть как положительные, так и отрицательные.
# # при этом последний символ не включается в интервал!
# x7 = s[1:-1:2] # указываем шаг, с которым мы берем символ: шаг - 2 (индексы: 1,3,5)
# # последний символ не включается в интервал!
# x8 = s[::-1] # отрицательный шаг. Выводим все символы в обратном порядке. То есть, переворачиваем слово наоборот.

# -------------------------------------------------------

# Проверяем, является ли строка палиндромом (читается одинаково с обоих концов)

# s = input()
# i = 0
# j = len(s)-1  # измеряем длину строки исключая 0
# is_palindrom = True
# while i < j: # цикл крутиться, пока переменная i меньше переменной j
#     # для начала проверяем равность первого и последнего символов.
#     if s[i] != s[j]:   # Если они не равны -
#         is_palindrom = False  # строка точно не палиндром
#           break # досрочно прерываем цикл, так как уже понятно, что это не палиндром
#     # уменьшаем диапазон с двух сторон
#     i += 1  # переходим на следующий символ с начала
#     j -= 1  # переходим на следующий символ с конца
# if is_palindrom:   # если же эти два символа равны
#     print('YES')

# Короткий варинат решения задачи на Палиндром

# s = input()
# r = s[::-1]
# if s == r:
#     print('YES')
# else:
#     print('NO')
# Единственный недостаток в этом решении в том, что код использует дополнительную память, если строка очень длинная
# -------------------------------------------------

# s = 'abcdefghijk'
# x1 = s[3:6]
# x2 = s[:6]
# x3 = s[3:]
# x4 = s[::-1]
# x5 = s[-3:]
# x6 = s[:-6]
# x7 = s[-1:-10:-2]
#
# print(x1, x2, x3, x4, x5, x6, x7)

# ------------------------------------------------

'''
Реализуйте алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной строки заменяются на этот символ 
и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом 
и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
'''
# Мой недоделаный говнокод
# s = input().lower()
# i = -1
# x = 0
# ss = ''
#
# while i != len(s)-1:
#     if s[i] == s[i+1]:
#         x += 1
#         i += 1
#         ss = s[i] + str(x)
#
#     print(ss, end='')
#     x = 0
#     ss = ''

# Решение Вариант 1
# s = input().lower()
# k = 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         k += 1
#     # elif s[i] != s[i+1]:
#     else:
#         print(s[i], str(k), sep='', end='')
#         k = 1

# Решение Вариант 2

# s = input().lower()
# l = len(s)  # длина строки
# p = s[0]  # первый символ
# count = 1  # счетчик
# res = ""  # здесь будет результат
# for i in range(l - 1):
#     c = s[i + 1]  # следующий символ
#     if (c == p):  # если совпадает со следующим - увеличим счетчик
#         count += 1
#     else:  # иначе выведем пару
#         res += p + str(count)
#         count = 1
#     p = c  # текущий стал следующим
# res += p + str(count)  # вывод последней пары
# print(res)


# Решение вариант 3
# s = input().lower()
# count = 1  # счетчик
# out = s[0]  # запоминаем первый символ
# for i in s[1:]:  # листаем строку в цикле от первого индекса до конца
#     if out[-1] == i:  # если предыдущий равен первому
#         count += 1  # счетчик +1
#     else:  # иначе
#         out += str(count) + i  # прибавляем значение счетчика + текущий символ
#         count = 1  # счетчик скидываем до 1
# out += str(count)  # по окончанию цикла добавляем значение счетчика
# print(out)  # выводим

# Решение вариант 4

# dna = input()                    # считываем строку
# print(dna[0],end='')             # выводим первый символ
# cnt = 1                          # счетчик символов на единице
# for i in range(0,len(dna)-1):    # итератор проходит по всем индексам символов от первого до конца,
#                                    кроме предпоследнего
#     if dna[i] == dna[i+1]:       # сравниваем символ по текущему индексу со следующим
#         cnt+=1                   # если символы одинаковые, то увеличиваем счетчик
#     else :
#         print(cnt,end='')        # если разные, то выводим значение счетчика
#         print(dna[i+1],end='')   # выводим следующий символ
#         cnt = 1                  # счетчик текущего символа на единице
# print(cnt)                       # в конце распечатываем значение счетчика последнего символа


# Решение Вариант 5 (самый короткий)

# s = input()
# n = 0
# l = s[0]
# for i in s:
#     if l == i:
#         n += 1
#     else:
#         print(l + str(n), end="")
#         l = i
#         n = 1
# print(l + str(n))


a, b, c = map(int(), input().split())

print(a, end=' ')
print(b)
print(c)
