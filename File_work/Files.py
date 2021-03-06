import os
import sys

# РАБОТА С ФАЙЛАМИ

# Чтение файлов
# Для интерпетатора существует текущая папка. И, чтобы узнать, какая папка считается текущей, можно испльзовать
# команду getcwd(). Это ф-я находится в библиотеке os, которую надо предварительно импортировать
dirpath = os.getcwd()
print(dirpath)
# C:\Users\Lenovo 330s\PycharmProjects\Python_lessons

# Создание файлов
# Файлы создаются с помощью команды open('file_name', 'w') as file: file.write('data')

# Ф-я open возвращает специальный объект
# file = open(text.txt)  # если не указывать путь, то ф-я open будет искать файл в текущей дирректории
#

s = open("C:/Users/Lenovo 330s/Documents/UII/text.txt",  encoding='utf-8')
str = s.read()
s.close()
print(type(str), str)

# -------------------- Строки и байты: str, bytes, bytearray -------------------------------

# Как узнать таблицу нашей кодировки
print(sys.getdefaultencoding())  # utf-8  - представление юникода в 8-битном виде (1 байт)

# Ф-я ord выдает код любого символа
print(ord('a'))   # 97
# Если надо преобразовать к символу по коду, испльзуем ф-ю chr()
print(chr(97))  # a
# Наши буквенные символы находятся в диапазоне от 0 до 127, дальше уже разные странные символы
print(chr(128))  # 
print(chr(198))  # Æ
# Нам нужен способ, чтобы переводить символьное представление в байты и наоборот.
# Для этого используются кодировочные таблицы.
# Переведем строку в байты. Для этого вызываем ф-ю encode(), в которую передаем кодировочную табилцу.
# Эти таблицы все именованные. В документации можно найти все эти имена.
s = 'hello'
enc_ascii = s.encode('ascii')  # передаем кодировочную таблицу ascii
enc_utf_8 = s.encode('utf_8')  # передаем кодировочную таблицу utf_8
enc_utf_16 = s.encode('utf_16')  # передаем кодировочную таблицу utf_16

# Выводим тип и значения переменных
print(type(enc_ascii))  # <class 'bytes'>  - метод encode возвращает тип bytes
# то есть с помощью метода encode мы переводим символы с помощью определенной таблицы кодировок в raw bites
# непосредственно в байтовое представление в памяти
print(enc_ascii)   # b'hello'  - ghtabrc 'b' обозначает, что представление байтовое.
print(enc_utf_8)   # b'hello'
print(enc_utf_16)  # b'\xff\xfeh\x00e\x00l\x00l\x00o\x00'

# Посмотрим, какое количество байтов используется для представления этих строк.
print(len(enc_ascii))  # 5   - на каждый символ 1 байт
print(len(enc_utf_8))  # 5   - на каждый символ 1 байт
print(len(enc_utf_16))  # 12 - utf_16 использует два байта на символ

# Кодировочные таблицы в случае Пайтона важны, когда мы говорим о передаче символов
# через какой-то канал информации (сеть или файл)
# Когда строчка загружена в память, понятия кодировки не существует, а есть просто последовательность символов unicode
# По сути дела, строчка, загруженная в память Пайтона, безшовная и нам нужны все эти кодировки только тогда,
# когда мы все это укладываем в файлы и передаем через сеть

# Чтобы перевести строку в байты, можно сразу на прямую использовать строковый литерал
str_in_bites = b'hello'
# или, это будет то же самое - воскользоваться методом encode(), которой мы передаем кодировочную таблицу
str_in_bites_1 = s.encode('utf-8')

# строка в текстовом виде. Последовательность символов в ней в юникоде задается так:
str_in_text = 'hello'
# Выводим тип
print(type(str_in_bites))  # <class 'bytes'>
print(type(str_in_text))  # <class 'str'>

# Ф-ю encode() мы можем вызвать на живую и передать ей кодовую таблицу
print(('bytes'.encode('utf-8')))  # b'bytes'
print(('байты'.encode('utf-8')))  # b'\xd0\xb1\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'  - вывод непосредственно в байтах

# можно обратиться к символам строки по индексу
print(str_in_bites[0])  # 104 -  у буквы h код - 104
print(str_in_text[0])  # h

# Важно понимать, что типы str и bites являются неизменяемыми.
# если попробуем в строке типа bytes что-то поменять, то получим ошибку
# str_in_bites[0] = 1
# TypeError: 'bytes' object does not support item assignment

# Если надо получить изменяемый тип bytes, можно воспльзоваться типом bitearray и его конструктором
ba = bytearray(b'hello')  # передаем в его конструктор строку hello
# Это тот же bytes, только изменяемый
# В нем мы можем менять символы по индексу
ba[0] = 87
print(ba)  # bytearray(b'Wello')  - сразу видим тип bytearray

# Ни в коем случае не конвертируйте байты обратно в строку с помщью конструктора str,
# по крайней мере без указания кодировки
# Посмотрим что будет.
# result = str(str_in_bites)  # теоретически здесь должны получить слово hello
# print(result)  # b'hello'  - в данном случае кавычки стали чайтью строки с литером b
# print(len(result))  # 8  - 8  байт на 8 символов
# Это дико, потому что мы хотим получить hello
# Поэтому обязательно, при использовании конструктора, надо передать utf-8
# (кодировку, в которой были загодированы символы при отправке в байт)
# result = str(str_in_bites, 'utf-8')  # теоретически здесь должны получить слово hello

# Не все кодировочные таблицы между собой совместимы. По большей части они таблицы являются подмножеством других
# Поэтому надо кодировать и декодировать в одной кодировочной таблице.
# Либо, что касается перевода в байты, всегда вызывать ф-ю decode()
result = str_in_bites.decode('utf-8')  # она вообще не отработает, если ей не передали кодировочную таблицу.
print(result)  # hello

# также важным моментом здесь является тот факт, что писать байты в файл нужно специальным образом.
# В байтовой репрезентации может быть не только строка, но и большое количество различных данных.
# например, изображение. Это все по сути raw bytes. Допустим, jpeg у нас закодирован в такие байты
jpeg = [120, 3, 255, 0, 100]
# Чтобы все это записать в файл, в репрезентации байтов, при чтении файла, чтобы читайть байты, нужно передать режим b
with open("C:/Users/Lenovo 330s/Documents/UII/text.txt", 'w+b') as file:
#  и это b комбинируется с теми режимами, которые мы обсуждали. Без b вы не прочитаете файл.
    file.write(bytes(jpeg))
# это исполнили
# теперь прочитаем
with open("C:/Users/Lenovo 330s/Documents/UII/text.txt", 'rb') as file:
    data = file.read()
    for b in data:
        print(b)
# 120
# 3
# 255
# 0
# 100
# Байты в файле могут быть совершенно не читаемыые людским глазом. Но программисты знают, что собой представляют
# те или иные байты и способны их кодировать, декодировать из одной системы в другую.
# И это могут быть не только строковые кодировки.

# Работая со строками, при переводе их в raw bytes (в бинарное представление), испльзуются таблицы кодировок.
# И для декодирования также используются таблицы кодировок.
# Если вы будете испльзовать несовместимые таблицы кодировок, то запросто может возникнуть такая ситуация,
# что вы закодировали одно, а раскодировали совсем другое.
# И не забывайте, что raw bytes, а именно байты в файле, это репрезентация некоторого состояния в памяти,
# именно в байтах, если вы хотите сложить ее в файл, она складывается именно в режиме b  - w+b или rb
# Если забудите 'b' - байты будут прочитаны как текст, но не как байты

