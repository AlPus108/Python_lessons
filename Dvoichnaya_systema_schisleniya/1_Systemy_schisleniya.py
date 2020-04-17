# Двоичные файлы.
# Чтение и запись
# Двоичные файлы используются, когда необходимо сохранить, прочитать или передать изображение или видео.
# Мы привыкли пользоваться десятичной системой счисления. Что это такое? Допустим, число 127
x = 127
# Это число может быть представлено степенями числа 10
# В Пайтоне есть ф-я pow() - степень. При момощи этой ф-и мы можем возводить число в какую-то степень.
# У ф-и два аргумента: 1-й - основание или база. В случае с 10-й системой, это 10.
# 2-й - степень, в которую будет возводиться это основание - число 10.
print(pow(10, 2))  # Вывод: 100. вычисление 10 в степени 2. То есть, 10*10.
# Если укажем 3, значит 10 перемножается 3 раза - 10*10*10
# Любое число в 0-й степени будет давать 1.
print(pow(5, 0))  # 1
# Любое число в 1-й степени будет возвращать само это число
print(pow(3000, 1))  # 3000

# ДЕСЯТИЧНАЯ СИСТЕМА СЧИСЛЕНИЯ также относится к позиционной системе.
# Позиционная система счисления работает с позициями и разрядами числа.
# В числе 127 три разряда и три позиции.
# В позиционной системе счисление значений начинается с правой (последней) цифры.
# Последняя цифра - это нулевая стемень десятки.
# Вторая цифра - первая степень десятки.
# Третья цифра - вторая степень числа 10 и тд.
# pow(10, 2) pow(10, 1) pow(10, 0)
# Число 127 можно записать следующим образом:
print(1 * pow(10, 2) + 2 * pow(10, 1) + 7 * pow(10, 0))  # 127
y = 1035
print(1 * pow(10, 3) + 0 * pow(10, 2) + 3 * pow(10, 1) + 5 * pow(10, 0))

# В этом суть позиционной системы счисления, в которой позиции - степени числа 10.

# Существуют другие позиционные системы счисления, которые также используются в программировании.
# Конечно, они используются на низком уровне и в таких высокоуровневых языках, как Пайтон, Джава, Джава-Скрипт
# они используются редко. Но, тем не менее, не помешает знать, как работатет копьютер в своей основе.

# ДВОИЧНАЯ СИСТЕМА СЧИСЛЕНИЯ.
# Компьтер обрабатывает электирческие сигналы - повышение напряжения и понижение напряжения.
# И это всего лишь два состояния. Повышеное напряжение - 1, пониженое - 0. 1/0.
# При помощи лишь 1 и 0 кодируется вся компьютерная информация на низком уровне.
# То есть, высокоуровневая программа языка Пайтон затем интерпретируется для компьютера в набор 0 и 1.
# Двоичная система счисления работает точно также, как и десятичная - по позициям.
# Только в качестве базы вместо 10 там стоит 2.
# pow(2, 3) pow(2, 2) pow(2, 1) pow(2, 0)
# В десятичной системе счисления используются 10 цифр от 1 до 9
# В двоичной системе используются две цифры 0 и 1.
# Двоичные числа обозначаются с префиксом '0b'
# Разбиваются они точно также, как и десятичные, только в базе вместо 10 ставим 2
x_2 = 0b101
print(1 * pow(2, 2) + 0 * pow(2, 1) + 1 * pow(2, 0))  # 5. Пятерка в двоичной системе - 101
y_2 = 0b0110
print(0 * pow(2, 3) + 1 * pow(2, 2) + 1 * pow(2, 1) + 0 * pow(2, 0))  # 6. Шестерка в двоичной системе - 0110

# В принципе, даже не разбивая по разрядам, в двоичной системе мы получи то же самое:
print(x_2)  # 5
print(y_2)  # 6

# ШЕСТНАДЦАТИРИЧНАЯ СИСТЕМА СЧИСЛЕНИЯ
# Она также используется в программировании из-за того, что записи в двоичной системе при использовании больших цифр
# становятся очень длинной.
# Например, чтобы записать 6 в двоичной системе, понадобилось 4 разряда.
# Чтобы записать 255, понадобиться 8 разрядов.
# Поэтому, существует более короткий способ записи - шестнадцатиричная система счисления. Она тоже позиционная.
# Только вместо 10 в базе там используется 16
# Здесь используется 16 символов: от 0 до 9 + шесть первых букв латинского алфавита: a, b, c, d, e, f.
# В шестнадцатиричной системе используется префикс 0x
x_16 = 0x11
print(x_16)  # 17
print(1 * pow(16, 1) + 1 * pow(16, 0))  # 17

# Также, здесь можно использовать и буквы
y_16 = 0xa1
print(y_16)  # 161
print(10 * pow(16, 1) + 1 * pow(16, 0))  # 161  a = 10
# Самое большое значение у символа f = 15
z_16 = 0xf1
print(z_16)  # 241
print(15 * pow(16, 1) + 1 * pow(16, 0))  # 241  f = 15
# Конечно, здесь может быть какое угодно количество разрядов
a_16 = 0x2cf1
print(a_16)  # 11505
print(2 * pow(16, 3) + 12 * pow(16, 2) + 15 * pow(16, 1) + 1 * pow(16, 0))  # 11505

# Видно, что 16-ричная система очень краткая и небольшим количество символов можно записать большие числа.
# Например запишем все максимальные значения 16-ричной системы
b_16 = 0xffff
print(b_16)  # 65535
print(15 * pow(16, 3) + 15 * pow(16, 2) + 15 * pow(16, 1) + 15 * pow(16, 0))  # 65535
# Если бы мы захотели записть это число в двоичной системе, нам бы понадобилось большое количество знаков.
# Переведем b_16 в двоичный формат
print(format(b_16, '0>42b'))  # 000000000000000000000000001111111111111111
# Здесь 42 разряда. Знак > означает смещение, выравнивание в правой части.
# Если распечатать это в двоичном формате:
print(0b000000000000000000000000001111111111111111)  # 65535
# В двоичной системе понадобилось 16 значящих разряда, а в 16-ричной - четыре. Это ощутимая разница.
# Поэтому 16-ричная система иногда используется в программировании для записи больших чисел.