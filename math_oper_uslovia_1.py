# В Питоне нет понятия переменных. Есть понятие "Объект".
# Любая вещь, которая в Питоне создается, инициализируется, является объектом.
# Питон, это язык с диначическим определение типов переменных.
# То есть. в процессе выполнения кода тип переменных может меняться (происходит автоматически)
# То есть, нельзя сказать, что в Питоне переменая имеет какой-то тип. Она может меняться в процессе

# int - целые
# float - с плавающей запятой
# complex - комплексное число. Используется в научных целях и специализированных модулях.
# bool - Истина или Ложь
# str - строки. Но, это более сложнйы объект, чем просто строки.

'''
Многострочный
комментарий -
три одинарные ковычки подряд.
'''


# print('Hellow!')
# print('Hellow', 'student!')
# print('Hellow', 'student!', 12345,  sep='__')  # резделитель между словами
# print('Hellow', 'student!', 12345,  end='ххх')  # окончание строки

# Динамическая типизация

# temp_var1 = input('Напечатай что-нибудь')
# print('Переменная №1 =', temp_var1, type(temp_var1), id(temp_var1), ' - указатель на выделенный участок памяти')
# temp_var2 = input('Напечатай что-нибудь')
# print('Переменная №2 =', temp_var2, type(temp_var2), id(temp_var2))
# temp_var2 = int(temp_var2)
# # print('Меняем типизацию Переменной №2', int(temp_var2))
# print('После смены типизации Переменная №2 ', temp_var2, type(temp_var2), id(temp_var2))
# print('Переменную №2 переместили в новый участок памяти')
# print('\nПеременную №1 приравниваем к переменной №2')
# temp_var1 = temp_var2
# # temp_var1 = int(temp_var2)
#
# print('После операции приравнивания', '\nПеременная №1 = ', temp_var1, type(temp_var1), id(temp_var1))
# print('Приведение типов не следует делать часто, так как это сильно расходует память')

# -----------------------------------------------
# Функция для проверки ввода, что это действительно число

def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


temp_float = input('Введите число тепа float')
# В Питоне разделителем числа является '.' (точка)
print(temp_float, type(temp_float), id(temp_float))

if is_digit(temp_float):
    temp_float = float(temp_float)
    print('После приведения к типу float ')
    print(temp_float, type(temp_float), id(temp_float))
else:
    print('Это не число типа float!')

# # Переменные и их типы

# # Описание машины
# # Марка
# name = 'Ford'
# # Чтобы узнаять тип переменной, нужно использовать функцию type()
# print() # для переноса строки
#
# print('Выводим значения переменных с их типом')
# print(name, type(name))  # str
# # Возраст
# age = 3
# print(age, type(age))  # int
# # Объем двигателя
# volume = 3.5
# print(volume, type(volume))  # float
# # Есть ли люк
# hatch = False
# print(hatch, type(hatch))  # bool
#
# # Ввод с клавиатуры
# происходит через функцию input(). В нее можно передать параметр или строку приглашения
# name = input('Введите ваше имя')
# print(name, type(name))
# # Тип переменой, которую возвращаем input, это всегда строка
# # Если надо ввести какое-то число, надо привести эти число из типа str к типу int
# age = input('Введите ваш возраст')
# print(age, type(age)) # Здесь тип числа str
# print(int(age), type(int(age))) # Здесь тип числа str меняем на int с помощью функции приведения типа int()
#
#
# # Математические операции math_operations
#
# # Предлагаем сделать ввод двух числел
# a = input('First number')
# b = input('Second number')
#
# # Приводим их к типу int
#
# a = int(a)
# b = int(b)
# '''
# print(a + b)
# print(a - b)
# print(a * b)
# result = a / b
# print(result) # результат
# print(type(result)) # тип результата
#
# print(a ** 2)
# '''
# # Логические операции
# a = True
# b = False
#
# # Отрицание
# print(not a)
# # Логическое 'И'
# print(a and b)
# #  Логическое ИЛИ
# print(a or b)
#
# a = 10
# print(a > 10)
# print(a < 10)
# print(a >= 10)
# print(a <= 10)
# print(a == 10)
# print(a != 10)
#
