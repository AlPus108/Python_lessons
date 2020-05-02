# Покрытие кодом

import coverage


# Пишем простую ф-ю, которая будет возвращать из двух строк самую большую.
# def longest_str(str_1, str_2):
#     if len(str_1) > len(str_2):
#         return str_1
#     else:
#         return str_2
#
#
# # Напишем простейшие тесты.
#
# assert longest_str('Volvo', 'Audi') == 'Volovo'  # по результатам теста ожидаме возврат значения 'Volvo'
# assert longest_str('BMW', 'Audi') == 'Audi'  # по результатам теста ожидаме возврат значения 'Audi'

# Давайте подумаем, почему мы написали такие тесты?
# В нашей ф-и 5 действующих строк и две ветки: условие if разветвляет логику работы программы
# То есть, у нас должно быть покрыто тестами 5 строчек кода и две ветки
# Чтобы это сделать, мы применяем специальный пакет coverage
# После установки этого пакета, переходм в дирректорию урока в терминале и набрать код:
# coverage run coverage_example_7.py (указываем модуль, который тестируем) и запускаем
# Модуль coverage анализирует код, его работа похожа на работу компилятора. Он проверяет, какие строки были пройдены
# в процессе тестирования и делает некоторый отчет
# Чтобы просмотреть этот отчет, необходимо набрать в терминале: coverage report

# (venv) D:\PycharmProjects\Python_lessons\exceptions_16>coverage report
# Name                    Stmts   Miss  Cover
# -------------------------------------------
# coverage_example_7.py       7      2    71%

# Насчитал 7 строчке кода, 2 строки пропущено, покрытие - 71%

# Далее попробуем покрыть по веткам.
# coverage run --branch coverage_example_7.py

# (venv) D:\PycharmProjects\Python_lessons\exceptions_16>coverage report
# Name                    Stmts   Miss Branch BrPart  Cover
# ---------------------------------------------------------
# coverage_example_7.py       7      2      2      1    67%

# Из отчета: две ветки покрыты, одна не покрыта, покрытие 67%

# Добавляем новую ветку

def longest_str(str_1, str_2):
    if len(str_1) > len(str_2):
        return str_1
    elif len(str_1) == len(str_2):
        return 'Equal!'
    else:
        return str_2


assert longest_str('Volvo', 'Audi') == 'Volovo'  # по результатам теста ожидаме возврат значения 'Volvo'
assert longest_str('BMW', 'Audi') == 'Audi'  # по результатам теста ожидаме возврат значения 'Audi'

# Результат
# (venv) D:\PycharmProjects\Python_lessons\exceptions_16>coverage report
# Name                    Stmts   Miss Branch BrPart  Cover
# ---------------------------------------------------------
# coverage_example_7.py       9      4      4      1    46%

# Здесь он нашел четыре ветки. Одна пропущена

# Добавляем тест

assert longest_str('BMW', 'KIA') == 'Equal!'  # по результатам теста ожидаем возврат значения 'Equal'

# (venv) D:\PycharmProjects\Python_lessons\exceptions_16>coverage report
# Name                    Stmts   Miss Branch BrPart  Cover
# ---------------------------------------------------------
# coverage_example_7.py      10      5      4      1    43%

# Но эти тесты не покрывают всю ф-ю.Лишь на 43%





