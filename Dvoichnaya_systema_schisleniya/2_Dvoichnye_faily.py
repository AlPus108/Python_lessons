# ДВОИЧНЫЕ ФАЙЛЫ

# Зпись двоичных файлов
# Создание двоичных файлов аналогично созданию обычных, только при этом добавляется буква 'b' - binary
# Строки и целые числа не могут быть на прямую переведены в двоичный код. В начале они должны быть сконвертированы
# в формат byse. Пайтон предоставляет несколько путей для этого и мы рассмотрим один из самых распространенных.
# Использвование встроенной ф-и bytes()
with open('test_binary', 'bw') as test_file:  # в скобках название файла, который открываем,
    # и далее название временной переменной
    # режим записи 'b' - бинарный, 'w' - запись. Без бувы 'b' будет записан обычный текстовый файл.
    for number in range(21):  # хотим записать все числа из этого диапазона в двоичном формате.
        test_file.write(bytes([number]))  # делаем преобразования целых чисел в двоичные при помощи ф-и bytes(),
        # чтобы поместить их в виде двоичного кода в файл.
# Мы передаем в ф-ю bytes число number в формате списка. Это список с одним числом. Почему?
# Эта ф-я немного странно работает. И, если мы передадим число без списка, она создаст количество байтов, сколько
# укзано в числе и все байты установит в 0.

# Для четния из этого файла
with open('test_binary', 'br') as test_file:  # буква 'r' - чтение.
    for number in test_file:
        print(number)
# Вывод:
# b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'  # значение 9 заменено на символ табуляции \t, а 10 на символ переноса \n
# это интерпретация в PyCharm этих символов
# b'\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14'    # символ \r заменил символ 'd' в 16-ричной системе счисления.
# Это резутат в формате 16-ричной системы счисления, так как в начале указан префикс 'x'
# Также в левом окне появлися файл test_binary

# Если мы хотим записать какие-то числа их диапазона в двоичной форме, то это можно делать короче, без цикла
with open('test_binary', 'bw') as test_file:
        test_file.write(bytes(range(21)))  # в ф-ю bytes() передаем диапазон цифр, который хотим записать.
# Получим тот же результат.

# Мы рассмотрели ручной режим записи информации в двоичный файл.
# Но, это не очень удобный способ для записи двоичных файлов, потому что если у вас достаточно сложные структуры данных,
# объекты с большим колиеством целых чисел или строк, которые также нужно приобразовывать в двоичный код, прежде,
# чем помещать в файл, то это крапотливая и сложная работа.
# Но, в Пайтоне есть модуль pickle, который это все упрощает.

# Переходим в файл 3_Modul_pickle
