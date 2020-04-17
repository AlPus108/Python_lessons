# Связан с:
# 4_mane_main
# second

# 2 Пришли из файла 4_name_main
# При запуске этого файла, запуститься весь код, который находится в этом файле.

# print(1)
# print('string')

# Так же будут запущены классы, функции и методы, которые будут содержаться в этом файле.
# Дело в том, что в Пайтоне, в отличии от других языков программирования, нет функции main(), которая инициализирует
# запуск файла. В ПАЙТОНЕ ЗАПУСКАЕТСЯ ВЕСЬ КОД, КОТОРЫЙ ЗАПИСАН В ФАЙЛЕ.
# Но, в Пайтоне есть предопределенная встроенная переменная __name__
# которая является одной из многих таких технических (для служебного пользования) переменных Пайтона.
# Чтобы их все просмотреть, надо вызвать специальную встроенную ф-ю globals()
print(globals())
# Эта ф-я возвращает словарь, заполенный теми объектами, которые были нами определены, и служебными объектами.
# В ней также мы найдем и служебную переменну __name__, которой было присвоено значение __main__.
# Этой переменной присваивается строковое значение в зависимости от того, как запущен файл.
# Если мы запускаем файл напрямую, без импорта, то этой переменной автоматически присваивается значение main
# Служебная встроенная переменная хранит имя модуля, из которого был произведен импорт
# __name__ == '__main__'
# Если сейчас вывести эту переменную на печать, то получим значение main, хотя мы его не присваивали
# print(__name__)  # __main__
# Значение main оно приобретает, когда скрипт запускается из родного модуля, в котолром он находится.


# Обычно это используется следующим образом.
# Сначала определяются какие-то ф-и

# def function1():
#     pass


# def function2():
#     pass


# Могут быть определены какие-то классы

# class MyClass:
#     pass


# И в конце идет проверка: действительно ли этот файл запущен самотоятельно, а не импортирован (то есть запущен
# через другой модуль и поэтому он не главный (main)
# if __name__ == "__main__":
#     # в этом случае мы запускаем ф-и
#     function1()
#     function2()


# Давайте исследуем это более детально.
# Создадим ф-ю

def function_1():
    print('function_1() from first.py')

# И далее, на верхнем уровне (то есть с самого начала строки) выводим сообщение:

print('Top level in first.py')

# Итак, на этом этапе, мы имеем в этом файле first.py определение ф-и и вызов команды print на верхнем уровне
# этого файла.

# Далее пишем:

if __name__ == '__main__':  # если переменная name имеет значение 'main'
    # Эта конструкция определяет точку входа в скрипт
    print('first.py is being run directly')   # файл был запущен непосредстенно, на прямую
else:  # если переменн name не имеет значение 'main'
    print('first.py has been imported')  # тогда этот файл импортирован.

# --> 3 second.py

# 4 Пришли из second
# Запускаем этот файл first

# Вывод:
# Top level in first.py
# first.py is being run directly

# Так как мы запустили этот файл first непосредственно, а не импортировали, то вывелась строка
# first.py is being run directly
# и это означает, что встроенная переменная __name__ получила автоматически значение __main__

# --> 5 second.py
