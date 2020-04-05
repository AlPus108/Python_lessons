# ВЛОЖЕННЫЕ ЦИКЛЫ

#  Мой вариант

smile = '\U0001f600'  # Код смайлика

x = 0
y = 0
for i in range(0, 9):
    x += 1
    print(smile)
    for j in range(x):
        y += 1
        print(smile, end='')
print(smile)


# Учитель

# Вариант с 2-мя for
for number in range(10):
    emoticons = ''
    for count in range(number + 1):
        emoticons += '\U0001f600'  # с каждой итерацией цикла смайлики прибавляются в переменную emoticons
    print(emoticons)

# Вариант с for и while
for number in range(10):
    count = 0
    emoticons = ''
    while count <= number:  # пока это условие истинно
        emoticons += '\U0001f600'  # с каждой итерацией цикла смайлики прибавляются в переменную emoticons
        count += 1
    print(emoticons)


# Более элегантный способ. Без помощи вложенных циклов.
# Мультиприкация или умножение строк

for number in range(1, 11):  # Если диапазон будте начинастья с 0, то число * 0 = 0. У нас будет на одну итера меньше
    print('\U0001f600' * number)  # При умножении строки на число, получаем эту же строку несколько раз

# Цикл while с умножением строк

count = 1
while count < 11:
    print('\U0001f600' * count)
    count += 1