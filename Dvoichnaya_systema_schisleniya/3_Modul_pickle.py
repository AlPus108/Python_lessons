

# ---------------------- Работа с модулем pickle --------------------------------

# pickle переводистя, как маринованый, законсервированный.
# Этот способ позволяет консервировать, стерилизовать объект со всеми его данными, состоянием помещать в двоичный файл
# и затем извлекать, дестерилизовать и восстанавливать все его данные и состояния.
# Для испльзования этого модуля, его сначала надо импортировать

import pickle

# Давайте создадим сложный Тьюпл, описывающий автомобиль.
honda = (
    'civic',
    'grey',
    '2009',
    # в этом Тюпл могут содержаться вложенные Тюпл с именами и фамилиями владельцев машины.
    (
        (1, 'James Brown'),
        (2, 'Jane White'),
        (3, 'Jack Green')
    )
)

# Вот такой сложный объект Тюпл у нас есть и теперь нам нужно сохранить его в двоичнй файл.
with open('honda.pickle', 'wb') as honda_file:
    # указываем название файла с расширение через точку, 'w' - запись, 'b' - формат
    # Далее вызываем метод dump(), который передает наш объект в файл.
    pickle.dump(honda, honda_file)  # указываем объект и файл, в который будем помещать наш объект.

# То есть, при помощи двух строчек кода, мы записываем в файл довольно сложный объект.
# При запуске этого кода, у нас в левом окне появляется файл honda.pickle
# Если открыть его в текстовом режиме, он будет выглядеть очень странно:
# ��P       (�civic��grey��2009�K�James Brown���K�
# Jane White���K�
# Jack Green�����t�.
# Потому что это все таки не текстовый, а двоичный файл.

# Для извлечения информации из двоичного файла используется метод load()
with open('honda.pickle', 'rb') as honda_retrieved:  # 'r' - чтение и название переменно, по которой будет обращаться
    honda_from_file = pickle.load(honda_retrieved)  # сразу присваиваем переменной
    # здесь используем метод load с одним параметром - переменная, из которой выгружаем.
print(honda_from_file)
# ('civic', 'grey', '2009', ((1, 'James Brown'), (2, 'Jane White'), (3, 'Jack Green')))

# и сразу же можно сделать распаковку Тьюпл
model, color, year, owner_list = honda_from_file
# и дальше данные выводим на экран
print(model)
print(color)
print(year)
# Следующий элемент является Тьюплом, поэтому для распаковки используем цикл
for owner in owner_list:
    owner_number, owner_name = owner
    print((owner_number, owner_name))
# civic
# grey
# 2009
# (1, 'James Brown')
# (2, 'Jane White')
# (3, 'Jack Green')

# Таким образом можно извлечь из двоичного файла довольно сложный объект.

# Мы можем помещать несколько объектов в файл и извлекать несколько объктов.
# То есть, по мимо объектк 'honda' мы можем поместить в файл еще что-нибудь

honda = (
    'civic',
    'grey',
    '2009',
    # в этом Тюпл могут содержаться вложенные Тюпл с именами и фамилиями владельцев машины.
    (
        (1, 'James Brown'),
        (2, 'Jane White'),
        (3, 'Jack Green')
    )
)

# Создадим еще саписки моделей Хонда и их владельцев, и поместим их в тот же файл.

models = ['civic', 'accord', 'pilot']
owners = ['James Brown', 'Jane White', 'Jack Green']

with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)
    pickle.dump(models, honda_file)
    pickle.dump(owners, honda_file)
    # Ну, и для примера, поместим еще какое-то число
    pickle.dump(99999999999999999, honda_file)

# Далее, для извлечения из файла информации, также используем ф-ю load()

with open('honda.pickle', 'rb') as honda_retrieved:  # 'r' - чтение и название переменно, по которой будет обращаться
    # Извлечение происходит в том же порядке, в каком происходила запись
    honda_from_file = pickle.load(honda_retrieved)
    models_from_file = pickle.load(honda_retrieved)
    owners_from_file = pickle.load(honda_retrieved)
    n = pickle.load(honda_retrieved)

# Выводим на экран
print(honda_from_file)
print(models_from_file)
print(owners_from_file)
print(n)
# ('civic', 'grey', '2009', ((1, 'James Brown'), (2, 'Jane White'), (3, 'Jack Green')))
# ['civic', 'accord', 'pilot']
# ['James Brown', 'Jane White', 'Jack Green']
# 99999999999999999

# Если мы вдруг поменяем порядок вывода, то информация в переменных вывода не будет соответствовать их назначению.
# Так что порядок вложения и порядок извлечения должне совпадать.





