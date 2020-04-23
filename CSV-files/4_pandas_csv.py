# Работа с библиотекой Pandas

# Pandas, как правило, используют для анализа данных файлов .csv

import pandas as pd

# В Пандасе ключевым моментом являтся dataframe

DataFrame_from_csv = pd.read_csv('students_3.csv', sep = '&')
# используем модуль read_csv для чтения из файла с указанием разделителя
print(type(DataFrame_from_csv))  # <class 'pandas.core.frame.DataFrame'>
print(DataFrame_from_csv)  # ф-я header модуля Pandas указывает, сколько объектов надо вывести
#    Name  age
# 0  Dima   28
# 1  Kate   18
# 2  Mike   31

# Что теперь можно делать с объектом DataFrame?
# Массу полезных вещей. Сними можно познакомиться в презентации Пандаса на странице:
#  https://alexanderdyakonov.files.wordpress.com/2015/04/ama2015_pandas.pdf
# 10 трюков библиотеки Pandas
# https://proglib.io/p/pandas-tricks/

# Методы, нужные в первую очередь:
# select_dtypes()  - автоматическое определение типов
# value_counts() - подсчет значений, содержащихся в столбце
# map() - преобразование всего столбца в целом
# apply() - для преобразования столбца; в apply можно передавать собственные ф-и
# value_counts() - поиск пропущенных значений
# to_csv() - сохранение файла csv в разных форматах




