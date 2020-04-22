import csv

# Основные ф-и и классы этого пакета:
# ф-я csv.reader
# ф-я csv.writer
# Производят чтение и записть из листа в лист
# класс csv.DictWriter
# класс csv.DictReader
# Более мощные по функционалу. Это чтение и запись в объект типа Словарь/Dict

# -------------------------- Открытие и чтение ----------------------------------------

# В файле cars.csv содержатся данный о машиннах в табличном формате

with open('cars.csv') as file:
    csv_reader = csv.reader(file)  # в переменную csv_reader мы получаем итератор.
    # теперь мы моежм перебирать каждую строку из переданного файла и они будут выводиться в форме списка.
    # каждая строка, это запись об автомобиле,
    # перебираем их в цикле
    for car in csv_reader:
        # print(car)
        # ['Year', 'Make', 'Model', 'Description', 'Price']
        # ['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00']
        # ['1999', 'Chevy', 'Venture "Extended Edition"', '', '4900.00']
        # ['1999', 'Chevy', 'Venture "Extended Edition, Very Large"', '', '5000.00']
        # ['1996', 'Feep', 'Grand Cherokee', 'MUST SELL! air, moon roof, loaded', '4799.00']

        # Такая форма вывода в виде списков намного удобнее, чем получать данные в одну строку и затем ее парсить.
        # Теперь мы можем обращаться к любой записи по индексу и считывать нужные нам значения.
        # Например, мы можем вывести для каждого автомобиля название, модель и цену.
        print(f'{car[0]} {car[1]} {car[4]}')
        # Year Make Price
        # 1997 Ford 3000.00
        # 1999 Chevy 4900.00
        # 1999 Chevy 5000.00
        # 1996 Feep 4799.00

        # При этом у нас извлекаются и заголовки столбцов. В данном случае нам это не надо. Мы можем это обойти.
        # В csv_reader находится итератор
        # Если мы еще раз повторим этот код, и запустим его, и попробуем вывести то же самое,
    for car in csv_reader:
        print(f'{car[0]} {car[1]} {car[4]}')
        # то второй раз на вывод мы ничего не получим. Вывод будет только один
        # потому что итератор полностью закончил перечисление всех элементов и, вызывая второй раз для этого итератора
        # тот же самый код, мы ничего не получаем, так как все элементы итератора были перебраны в верхнем коде.

        # Чтобы пропустить первую строку, мы можем, перед тем, как распечатывать, выхвать ф-ю next()
        # и передать в нее наш итератор
with open('cars.csv') as file:
    csv_reader = csv.reader(file)  # в переменную csv_reader мы получаем итератор.
    next(csv_reader)  # с помощью ф-и next() мы пропускаем первую строку.
    for car in csv_reader:
        print(f'{car[0]} {car[1]} {car[4]}')
        # 1997 Ford 3000.00
        # 1999 Chevy 4900.00
        # 1999 Chevy 5000.00
        # 1996 Feep 4799.00
        # Теперь без заголовок строк.

        # Конечно, если мы не хотим перебирать построчно все элементы, мы можем легко получить список из итератора
with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    data_list = list(csv_reader)  # создаем переменную лист и передаем в нее csv_reader в формате списка
    print(data_list)
    # [['Year', 'Make', 'Model', 'Description', 'Price'], ['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00'],
    # ['1999', 'Chevy', 'Venture "Extended Edition"', '', '4900.00'], ['1999', 'Chevy', 'Venture "Extended Edition,
    # Very Large"', '', '5000.00'], ['1996', 'Feep', 'Grand Cherokee', 'MUST SELL! air, moon roof, loaded', '4799.00']]
    # Здесь мы получаем данные в виде списка списков. Внутри списка находятся списки. Первый список, это заголовок,
    # затем первая строка данных, вторая и тд.
    # То есть, мы можем получать данные и в таком формате. Все зависит от контекста, для чего нам эти данные.

# ----------------------------- Чтение с помощью  DictReader -------------------------------------

    # Есть один момент. Обращаться по числовым индексам не очень удобно. Можно просто ошибиться.
    # Было бы удобней обращаться к данным по имени поля, то есть по ключу, как в словаре.
    # Это можно сделать при помощи DictReader(), который также существует в модуле csv
    # Так же, как мы читали при помощи reader(), это же можжно сделать при помощи DictReader()
    # Этот класс также находится в модуле csv, поэтому пишем через точку
with open('cars.csv') as file:
    csv_reader = csv.DictReader(file)  # применяем DictReader.
    # next(csv_reader)  # с помощью ф-и next() мы пропускаем первую строку. Здесь пропускать строку не нужно
    # так как здесь автоматически извлекюатся название столбцов в качестве ключей
    for car in csv_reader:
        # print(car, type(car))

        # {'Year': '1997', 'Make': 'Ford', 'Model': 'E350', 'Description': 'ac, abs, moon', 'Price': '3000.00'} <class 'dict'>
        # {'Year': '1999', 'Make': 'Chevy', 'Model': 'Venture "Extended Edition"', 'Description': '', 'Price': '4900.00'} <class 'dict'>
        # {'Year': '1999', 'Make': 'Chevy', 'Model': 'Venture "Extended Edition, Very Large"', 'Description': '', 'Price': '5000.00'} <class 'dict'>
        # {'Year': '1996', 'Make': 'Feep', 'Model': 'Grand Cherokee', 'Description': 'MUST SELL! air, moon roof, loaded', 'Price': '4799.00'} <class 'dict'>Year': '1996', 'Make': 'Feep', 'Model': 'Grand Cherokee', 'Description': 'MUST SELL! air, moon roof, loaded', 'Price': '4799.00'}

        # Мы получаем данные объекта OrderDict - упорядоченных словарей.
        # По сути, это такой же словарь, как и обычный, с парами ключ-значение,
        # но в OrderDict запоминается порядок помещения в него значений и извлекаются они в том же порядке.

        # И, дальше мы можем обращаться к данным по ключам
        print(f'{car["Make"]} {car["Model"]} {car["Price"]}')
        # Ford E350 3000.00
        # Chevy Venture "Extended Edition" 4900.00
        # Chevy Venture "Extended Edition, Very Large" 5000.00
        # Feep Grand Cherokee 4799.00
        # Здесь мы получаем только те данные, которые нам нужны, и в том формате, который нам нужен.

        # Рассмотрим случай, когда у нас есть данные, которые разделены не запятой, а другми знаками, например ';'
        # cars_1.csv

        # Для такого формата записи мы можем пользоваться тем же кодом, но немного видоизмененным.
with open('cars_1.csv') as file:
    # Если в файле другой разделитель, кроме ',', в DictReader мы добавляем параметр
    csv_reader = csv.DictReader(file, delimiter=';')
    for car in csv_reader:
        print(f'Вывод из файла cars_1 (c ";") {car["Make"]} {car["Model"]} {car["Price"]}')
        # Вывод из файла cars_1 (c ";") Ford E350 3000,00
        # Вывод из файла cars_1 (c ";") Chevy Venture "Extended Edition" 4900,00
        # Вывод из файла cars_1 (c ";") Chevy Venture "Extended Edition; Very Large" 5000,00
        # Вывод из файла cars_1 (c ";") Feep Grand Cherokee 4799,00

        # То же самое мы можем сделать и при помощи обычного reader()
with open('cars_1.csv') as file:
    csv_reader = csv.reader(file, delimiter=';')
    next(csv_reader)  # с помощью ф-и next() мы пропускаем первую строку - заголовки столбцов.
    for car in csv_reader:
        # Но в случае с reader() мы должны уже обращаться к значениям по числовым индексам
        print(f'Вывод из файла cars_1 (c ";") {car[1]} {car[2]} {car[3]}')
        # Вывод из файла cars_1 (c ";") Ford E350 ac; abs; moon
        # Вывод из файла cars_1 (c ";") Chevy Venture "Extended Edition"
        # Вывод из файла cars_1 (c ";") Chevy Venture "Extended Edition; Very Large"
        # Вывод из файла cars_1 (c ";") Feep Grand Cherokee MUST SELL! air; moon roof; loaded

        # Также, мы можем использвать в качестве разделителей любые другие символы.
        # Все, что в этом случае меняем в коде, это delimiter='' в параметрах reader()
        # Но, с этим нужно быть осторожным, так как если вы используете символ, который испльзуется так же в значениях
        # Можно получить некорректный результат.

