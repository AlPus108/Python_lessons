# Простейший for

# Конструкция range(start, stop, step)
# start - число с которого начинаем,
# stop - число, которым заканчиваем,
# step - шаг, через какой интервал будут браться числа

# for i in range(0, 10, 1):  # здесь будем брать все числа
#     print(i)

# for i in range(0, 100, 15):  # от 0 до 100 с шагом 15
#     print(i)

# обратный порядок
# for i in range(10, 0, -1):  # от 10 до 0 с шагом -1(отнимаем)
#     print(i)

# Краткая запись
# for i in range(10):  # от нуля до числа в скобках
#     print(i)

# Добавляем в цикл проверку условия
# for i in range(10):  # от нуля до числа в скобках
#     print(i)
#     if i == 5: break # если i равен 5, цикл прерывается

# Количество повторений
# for i in range(10):
#     answer =input('Какая лучшая марка автомобиля?')
#     if answer == 'Volvo':
#         print('Вы абсолютно правы!')
#         break

# Continue
for i in range(10):
    if i == 9:
        break
    if i < 3:
        continue
    else:
        print(i)
