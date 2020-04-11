# 3 Пришли из файла first.py

# С самого начала делаем импорт модуля first

import first

print('Top level is second.py')

# вызываем ф-и из импортированного модуля first

first.function_1()

# копируем блок if_else из модуля first и вставляем сюда и меняем в тексте first на second

if __name__ == '__main__':  # если переменн name имеет значение 'main'
    print('second.py is being run directly')   # файл был запущен непосредстенно, на прямую
else:  # если переменн name не имеет значение 'main'
    print('second.py has been imported')  # тогда этот файл импортирован.

# --> 4 first.py
# 5 Пришли из first.py

# Запускаем этот модуль second.py
# Вывод:

# Top level in first.py
# first.py has been imported
# Top level is second.py
# function_1() from first.py
# second.py is being run directly

# Так как мы импортировали first, у нас запускается print в файле first и мы получаем эту строку:
# Top level in first.py
# Далее в файле first продолжает выполняться код, а именно if __name__ == '__main__':
# присвоено ли переменной name значение main
# и в данном случае при импорте этого не случилось, поэтому эта ф-я из файла first выводит сообщение:
# first.py has been imported
# Когда выполнение кода в модуле first.py закончилось, начинает выполняться код в этом модуле second.py:
# Выводится строка: Top level is second.py,
# Далее запускается function_1 из модуля first, который выводит сообщение:
# function_1() from first.py, что эта ф-я запущена из модуля first.py
# Затем выполняется проверка значения встроенной переменной __name__ данного модуля second.py
# Так как мы его запустили непосредственно, то есть он не был импортирован, то здесь переменная __name__
# получает значение main и срабатывает первая ветка кода: second.py is being run directly

# 6 --> 4_name_main
