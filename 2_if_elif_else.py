# Операторы условия

brand = 'Volovo'
engine_volume = 1.5
horsepower = 140
sunroof = True

# Проверка условия if
# if horsepower < 80:
#     print('No Tax')

# Проверка условмия if/else

# if horsepower < 80: print('No Tax')
# else: print('Tax')

# Проверка услоия if/elif/elif/else

# tax = 0
# if horsepower < 80:
#     tax = 0
# elif horsepower < 100:
#     tax = 10000
# elif horsepower < 150:
#     tax = 20000
# else:
#     tax = 50000
# print(tax)

# Проверка условмия if для присваивания

# cool_car = 0
# cool_car = 1 if sunroof == 1 else 0
# print(cool_car)

# Проверим, что хотя бы одно из чисел a или b оканчивается на 0:

# a = int(input())
# b = int(input())
# if a % 10 == 0 or b % 10 == 0:
#     print('YES')
# else:
#     print('NO')

# Проверим, что число a — положительное, а b — неотрицательное:

#     if a > 0 and not (b < 0):

# Или можно вместо not (b < 0) записать (b >= 0)


# if 1:               # Если выражение True - будет выведен на экран текст (0/нет текста - False, 1/любой знак - True)
#     print('something')
#
# lucky_number = input("Введите ваше счастливое число: ")
# if lucky_number:     # Если пользователь ввел число (строка не пустая)
#     print('Это твое счастливое число: ', lucky_number)
#
# # Иногда удобно испльзовать True или False в каких-то значениях в вашем коде
