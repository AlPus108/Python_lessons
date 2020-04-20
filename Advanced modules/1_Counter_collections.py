# Модуль Collections

# Это встоенный модуль. Он имплементирует специальные контейнерные типы данных, которые предоставляют альтернативы
# общим встроенным контейнерам языка Пайтон, таким, как dict, list, set, tuple
# Список его типов данных можно найти в интернете в документации к Пайтон по адресу
# docs.python.org/3/library/collections.html

# namedtuple() - factory function for creating tuple subclasses with named fields
# deque - list-like container with fast appends and pops on either end
# ChainMap - dict-like class for creating a single view of multiple mappings
# Counter - dict subclass for counting hashable objects
# OrderedDict - dict subclass that remembers the order entries were added
# defaultdict - dict subclass that calls a factory function to supply missing values
# UserDict - wrapper around dictionary objects for easier dict subclassing
# UserList - wrapper around list objects for easier list subclassing
# UserString - wrapper around string objects for easier string subclassing

# Counter
# Мы начнем рассмотрения с Counter
# Counter - субкласс класса dict. Используется для подсчета hashable-объектов.
# Это коллекция, где элемент сохраняются как ключи словаря,
# и их счетчик, который отображает количество этих объектов в последовательности.


# Ипортируем из модуля collections этот класс

from collections import Counter

# Создадим список
number_list = [1, 2, 2, 5, 6, 7, 7, 12, 14, 22, 25, 25, 48, 54, 24, 24, 24, 24, 24]

# Что же делает Counter?
# Создадим объект Counter
print(type(Counter()))  # Тип: <class 'collections.Counter'>
print(Counter(number_list))
# Counter({24: 5, 2: 2, 7: 2, 25: 2, 1: 1, 5: 1, 6: 1, 12: 1, 14: 1, 22: 1, 48: 1, 54: 1})
# Получаем Словарь, в котором содержатся пары: ключ и значение.
# Ключи - сами элементы
# Значения - сколько раз элемент встречается в этой последовательности
# Порядок вывода: чем чаще элемент встречается в последовательности, тем раньше он выводится.

# Counter также может работать и со строками
string = 'kkkkkrrrriiiiissssshhhhnnnnaaa'
# Помещаем эту строку в Counter
print(Counter(string))
# Counter({'k': 5, 'i': 5, 's': 5, 'r': 4, 'h': 4, 'n': 4, 'a': 3})
# Здесь он подсчитывает, сколько раз встречается каждая буква в этой строке.
# Сортировка от большего к меньшему.

# Подсчитываем количество слов в строке.
sentence = 'Харе Кришна Харе Кришна Кришна Кришна Харе Харе Харе Рама Харе Рама Рама Рама Харе Харе'

print(Counter(sentence.split()))
# Counter({'Харе': 8, 'Кришна': 4, 'Рама': 4})

# В документации находим список распространенных патернов для работы с объектами Сounter:

# sum(c.values())                 # total of all counts / подсчет количества элементов

c = Counter(sentence.split())
print(sum(c.values()))  # 16

# c.clear()                       # reset all counts / очищение списка

# c.clear()
# print(sum(c.values()))  # 0

# list(c)                         # list unique elements / Список уникальных элементов

print(list(c))  # ['Харе', 'Кришна', 'Рама'] # получаем все уникальные элементы в форме списка без повторений

# set(c)                          # convert to a set

print(set(c))  # {'Рама', 'Харе', 'Кришна'}

# dict(c)                         # convert to a regular dictionary

print(dict(c))  # {'Харе': 8, 'Кришна': 4, 'Рама': 4}  # само значение : сколько раз оно встречается

# c.items()                       # convert to a list of (elem, cnt) pairs

print(c.items())  # dict_items([('Харе', 8), ('Кришна', 4), ('Рама', 4)])
# список из пар элементов в форме Тапл : сам элемент и сколько раз он встречается. Все это в списке

# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c = c.items()  # создали словарь предыдущей ф-ей
# Здесь вовзращаем обратно из словаря в лист
c = Counter(dict(c))
print(c)  # Counter({'Харе': 8, 'Кришна': 4, 'Рама': 4}) -  получаем обратно то, что было до этого

# c.most_common()[:-n-1:-1]       # n least common elements / список самых часто встречающихся элементов
print(c.most_common())  # [('Харе', 8), ('Кришна', 4), ('Рама', 4)] - при выводе без параметров получаем такие пары
print(c.most_common(2))  # [('Харе', 8), ('Кришна', 4)] - два самых часто встречающихся элементов
print(c.most_common()[:-1-1:-1])  # [('Рама', 4)] - самый редко встречающися элемент или несколько - регулируя первой -1
print(c.most_common()[:-2-1:-1])  # [('Рама', 4), ('Кришна', 4)]

# +c                              # remove zero and negative counts / удаление нулей и

# Counter может пригодиться, если вы распознаете какой-то текст, создаете приложение для распознования речи,
# то можно таким образом разбивать текст по словам и проводить какие-то манипуляции при помощи объекта класса Counter
