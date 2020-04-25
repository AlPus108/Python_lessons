#  Запись в CSV-файл

# Есть два способа записи: writer() и DictWriter()

import csv

# ----------------------------- Запись в файл writer() ---------------------------

# Пример 1
# Запись из строки
# Имеем строку со списком, содержащий данные об автомобилях
car_data = [['Brand', 'Price', 'Year'],['Volvo', 1.5, 2000],['Ford', 2.5, 2005],['Tayota', 3.2, 2018],['Audi', 5.4, 2019]]
# Запишем эти данные в файл

with open('car_data.csv', 'w') as f:  # создаем файл car_data.csv в режиме записи 'w'
    writer = csv.writer(f)  # writer имеет второй (необязательный) параметр delimiter по умолчанию = ','
    writer.writerows(car_data)  # записываем в переменную writer с помощью ф-и writerows построчно данные
    # из переменной car_data
    # Будут записаны данные в файл построчно, в том же порядке, как они даны в строке.
    # Запускаем код
    # Появляется в папке файл car_data.csv
    # Содержимое файла:
    # Brand,Price,Year
    #
    # Volvo,1.5,2000
    #
    # Ford,2.5,2005
    #
    # Tayota,3.2,2018
    #
    # Audi,5.4,2019

# Теперь заменим разделитель по умолчанию на другой
with open('car_data.csv', 'w') as f:
    writer = csv.writer(f, delimiter='|')  # присваиваем новый разделитель '|'
    writer.writerows(car_data)  # записываем в переменную writer с помощью ф-и writerows

    # Снова запускаем.
    # Если стоит режим 'w', то следующий запуск перезаписывает данные файла и вставляет новые
    # Brand|Price|Year
    #
    # Volvo|1.5|2000
    #
    # Ford|2.5|2005
    #
    # Tayota|3.2|2018
    #
    # Audi|5.4|2019

# Считаем этот файл
with open('car_data.csv', 'r') as f:  # Считывание происходит в режиме 'r'
    reader = csv.reader(f)
    for row in reader:
        print(row)
        # ['Brand|Price|Year']
        # []
        # ['Volvo|1.5|2000']
        # []
        # ['Ford|2.5|2005']
        # []
        # ['Tayota|3.2|2018']
        # []
        # ['Audi|5.4|2019']
        # []



# Пример 2
# Запись из кода
with open('students.csv', 'w') as file:  # используем 'w' для создания файла students.csv
    # и записи из него в переменную file
    csv_writer = csv.writer(file)  # создаем переменную и передаем ей данные, которые считывает writer из file
    # С помощью метода writerow() создаем записи и передаем их в форме списков
    # через переменную csv_writer в файл students.csv
    csv_writer.writerow(['First name', 'Last name', 'Age'])
    csv_writer.writerow(['Jack', 'White', 24])  # цифры можно передавать в формате int
    csv_writer.writerow(['Jane', 'Black', 20])

    # Запускаем этот файл. Создается файл students.csv в том же каталоге, где и этот файл.
    # Открываем файл students.csv и там находим записи
    # First name,Last name,Age
    #
    # Jack,White,24
    #
    # Jane,Black,20

# -------------------- Считывание из одного файла и запись в новый файл. Выборка данных -----------------

# До этого мы создавали записи прямо в коде и передавали их в файл
# Можно считывать данные из другого файла и передавать их в новый файл.
# Сейчас считаем данный из файла car.csv и передадим их в новый файл
# Будем считывать только производителя машины и ее модель. То есть, сделаем выборку определенных данных

with open('cars.csv') as file:  # считывам данные из файла cars.csv и помещаем их в переменную file
    csv_reader = csv.reader(file)  # передаем считанные данные переменной csv_reader
    # проверим как он работает, распечатываем содержимое переменной
    print(csv_reader)  # плучаем объект <_csv.reader object at 0x00AB9C30> Но форма вывода не очень удобна
    # Чтобы увидеть данные из объекта, его надо прогнать через цикл
    # Заголовки нам не нужны, поэтому перед циклом вызваем ф-ю next() - она пропускает первую строку
    next(csv_reader)
    for car in csv_reader:
        print(car)
        # ['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00']
        # ['1999', 'Chevy', 'Venture "Extended Edition"', '', '4900.00']
        # ['1999', 'Chevy', 'Venture "Extended Edition, Very Large"', '', '5000.00']
        # ['1996', 'Feep', 'Grand Cherokee', 'MUST SELL! air, moon roof, loaded', '4799.00']

# Теперь можем сделать выборку из файла. Нам нужны название производителя и модель.
# Для приема выбранных данных создаем в коде переменную с пустым списком

with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    make_model_list = []  # создаем переменную make_model_list типа list для данных выборки
    for car in csv_reader:
        make_model = [car[1], car[2]]  # Делаем выборку из нужных полей и передаем их переменной make_model
        make_model_list.append(make_model)  # данные выборки передаем в переменную make_model_list
    print(make_model_list)  # выходим из цикла и распечатываем make_model_list
    # Получаем список, в котором находятся списки с двумя значениями: производителя и модели.
    # [['Ford', 'E350'], ['Chevy', 'Venture "Extended Edition"'], ['Chevy', 'Venture "Extended Edition, Very Large"'],
    # ['Feep', 'Grand Cherokee']]

# Теперь эти значения можно записать в файл. Для этого надо его создать и открыть
with open('cars_make_model.csv', 'w') as file:  # создаем новый файл cars_make_model.csv и связываем его с переменной
    csv_writer = csv.writer(file)  # связываем новый файл с переменной csv_writer
    for row in make_model_list:  # в цикле пролистываем данные из переменной make_model_list
        csv_writer.writerow(row)  # передаем данные в переменную csv_writer,
        # из которой по цепочке они попадают в созданный файл cars_make_model.csv
        # Запускаем этот код
        # В результате создается новый файл cars_make_model.csv с выборкой
        # Содержимое файла:
        # Ford,E350
        #
        # Chevy,"Venture ""Extended Edition"""
        #
        # Chevy,"Venture ""Extended Edition, Very Large"""
        #
        # Feep,Grand Cherokee

# Весь верхний код можно записать более коротким способом -
# совместить код выборки из файла и код записи в новый файл путем вложения один в другой

with open('cars.csv') as file:
    csv_reader = csv.reader(file)  # здесь считываем из файла
    next(csv_reader)

    with open('cars_make_model.csv', 'w') as file:
        csv_writer = csv.writer(file)  # здесь записываем в новый файл
        for row in csv_reader:  # здесь в цикле мы считываем из csv_reader, созданного во внешнем блоке
            csv_writer.writerow([row[1], row[2]])  # передаем в форме листа

# Но здесь присутствует подводный камень. На данный момент оба файла открыты:
# cars.csv - на чтение, cars_make_model.csv - на запись
# так как внутри одного блока with находится другой блок with
# Они закроются, если они будут не вложенные, один за другим.

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#
# with open('cars_make_model.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     for row in csv_reader:
#         csv_writer.writerow([row[1], row[2]])

# Но, в этом случае мы получим ошибку обращения к закрытому файлу
# ValueError: I/O operation on closed file. - второй блок with обращается к уже закрытому файлу cars.csv первого блока.
# В таком построении нам приходится использвать дополнительный лист, в который мы помещаем выбранные данные
# и эти сохраненные данные уже использовать для записи в другом блоке.
#         make_model = [car[1], car[2]]  # Делаем выборку из нужных полей и передаем их переменной make_model
#         make_model_list.append(make_model)  # данные выборки передаем в переменную make_model_list


# ----------------------------- Запись в файл DictWriter() ---------------------------

# Пример 1
# Запись из словаря
# Имеем словарь
data_dict = [{'Name': 'Dima', 'age': 28},
             {'age': 18, 'Name': 'Kate'},  # для учебного примера поменяем их местами и посмотрим, как сработает
             {'Name': 'Mike', 'age': 31}]

field_names = ['Name', 'age']  # отдельной строкой названия полей в форме листа
# Ссылаясь на название колонок, ф-я будет искать их в словаре и получать их значения.

with open('students_3.csv', 'w') as f:  # создаем файл students_3.csv
    writer = csv.DictWriter(f, delimiter='&', fieldnames=field_names)  # присваиваем атрибуту fieldnames имя переменной,
    # в которой находятся имена полей
    writer.writeheader()  # создаем строку с заголовками
    # далее добавляем информацию
    for i in range(len(data_dict)):  # циклом пробежимся по списку
        writer.writerow(data_dict[i])
        # Запускаем код
        # Создается файл students_3.csv
        # Name&age
        #
        # Dima&28
        #
        # Kate&18
        #
        # Mike&31

# Теперь считаем файл, который мы получили
with open('students_3.csv') as f:
    reader = csv.DictReader(f, delimiter='&')
    for row in reader:
        print(row)
        # Получаем вывод в классическом дикте
        # {'Name': 'Dima', 'age': '28'}
        # {'Name': 'Kate', 'age': '18'}
        # {'Name': 'Mike', 'age': '31'}

# Пример 2
# Запись из словаря, встроенного в код
# Открываем файл
with open('students_1.csv', 'w') as file:  # используем 'w' для создания файла students_1.csv
    # и записи из него в переменную file
    headers_list = ['First name', 'Last name', 'Age']  # здесь создаем массив из названий столбцов (заголовки)
    csv_writer = csv.DictWriter(file, fieldnames=headers_list)  # csv_writer создаем уже с заголовками
    # Далее создаем поле для заголовков
    csv_writer.writeheader()  # здесь заголовки не записываем, а просто создаем с помощью ф-и writeheader()
    # они уже переданы в csv_writer при его создании
    # Далее с помощью метода writerow() создаем записи и передаем их в форме словаря
    # через переменную csv_writer в файл students_1.csv.
    # То есть, здесь метод writerow() принимает словарь в качестве параметров
    csv_writer.writerow({
        'First name': 'Jack',
        'Last name': 'White',
        'Age': 24
    })
    csv_writer.writerow({
        'First name': 'Jane',
        'Last name': 'Black',
        'Age': 20
    })
    # Запускаем код
    # First name,Last name,Age
    #
    # Jack,White,24
    #
    # Jane,Black,20

# В этом и все отличие в использовании DictWriter() от writer()
# Если вы получаете данные в форме словаря, то конечно, удобнее использовать DictWriter() для помещения данных в файл.


# Получим данные по машинам с помощью DictWriter()

with open('cars.csv') as file:
    csv_reader = csv.DictReader(file)
    car_list = list(csv_reader)  # передаем данный из файла в переменную car_list
    print(car_list)
    # Получаем dict со всеми значениями
    # [{'Year': '1997', 'Make': 'Ford', 'Model': 'E350', 'Description': 'ac, abs, moon', 'Price': '3000.00'},
    # {'Year': '1999', 'Make': 'Chevy', 'Model': 'Venture "Extended Edition"', 'Description': '', 'Price': '4900.00'},
    # {'Year': '1999', 'Make': 'Chevy', 'Model': 'Venture "Extended Edition, Very Large"', 'Description': '',
    # 'Price': '5000.00'}, {'Year': '1996', 'Make': 'Feep', 'Model': 'Grand Cherokee', 'Description': 'MUST SELL! air,
    # moon roof, loaded', 'Price': '4799.00'}]

# Снова открываем файл, теперь уже для записи выборки

with open('make_model.csv', 'w') as file:  # создаем новый файл для выборки
    headers_list = ['Make', 'Model']  # Создаем список хэдеров, по которым будем выбирать данные
    # и присваиваем им значения
    csv_writer = csv.DictWriter(file, fieldnames=headers_list)
    csv_writer.writeheader()  # записываем значения в созданный файл
    # Запускаем код
    # Создается файл make_model.csv с полями:
    # Make,Model
    for car in car_list:  # в цикле листаем переменную car_list, созданную в предыдущем блоке with
        csv_writer.writerow({  # создаем здесь словарь
            # получаем значения из объекта car по ключам
            'Make': car['Make'],
            'Model': car['Model']
        })
        # Make,Model
        #
        # Ford,E350
        #
        # Chevy,"Venture ""Extended Edition"""
        #
        # Chevy,"Venture ""Extended Edition, Very Large"""
        #
        # Feep,Grand Cherokee







