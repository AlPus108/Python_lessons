# beautifulsoup

# Перешли из 1_Web_Scrapng
# Теперь мы можем использовать этот пакет
from bs4 import BeautifulSoup

# Теперь мы можем с помощью объекта этого класса парсить html-код, то есть распознавать html-элементы
# Для начала будем парсить вот такой код:
# Для этого создаем переменную и присваиваем ей код.


html_string = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Development Page</title>
        <style type="text/css">
            
            h1{
                color: white;
                background: red;
            }
    
            li{
                color: red;
            }
    
            #css-li{
                color: blue;
            }
    
            .green{
                color: green;
            }
    
        </style>
    </head>
    <body>
        <h1>Web Development</h1>
        <h1 class="green">Web</h1>
        <h3>Programming Languages</h3>
    
        <ol>
            <li>HTML</li>
            <li id="css-li">CSS</li>
            <li class="green bold">JavaScript</li>
            <li class="green">Python</li>
            <li class="green" id="python-li">Python</li>
        </ol>
    
    </body>
    </html>


"""

# Допустим, мы получили это код с веб-страницы. Теперь нам надо его как-то парсить,
# то есть выбирать какие-то элементы по своему желанию. Именно для этого мы будем использовать BeautifulSoup

# Для этого созадем еще одну переменную

parsed_html = BeautifulSoup(html_string, 'html.parser')  # первый параметр - срока с нашим кодом
# BeautifulSoup может распознавать не только html, но xml-файлы (немного другой язык разметки),
# поэтому сейчас мы ему указываем, что будем распознавать именно html - 'html.parser'
# И сделаем вывод на экран
print(parsed_html)
print(type(parsed_html))
# Мы получаем всю строку html

# <!DOCTYPE html>
#
# <html>
# <head>
# <title>Web Development Page</title>
# <style type="text/css">
#
#             h1{
#                 color: white;
#                 background: red;
#             }
#
#             li{
#                 color: red;
#             }
#
#             #css-li{
#                 color: blue;
#             }
#
#             .green{
#                 color: green;
#             }
#
#         </style>
# </head>
# <body>
# <h1>Web Development</h1>
# <h1 class="green">Web</h1>
# <h3>Programming Languages</h3>
# <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green">JavaScript</li>
# <li class="green">Python</li>
# </ol>
# </body>
# </html>

# И тип
# <class 'bs4.BeautifulSoup'>

# Но, это уже не строка, это объект класса BeautifulSoup
# Теперь мы можем использовать разные методы этого класса, для получения нужных нам объектов.


# Давайте выведем код тела страницы

print(parsed_html.body)
# <body>
# <h1>Web Development</h1>
# <h1 class="green">Web</h1>
# <h3>Programming Languages</h3>
# <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green">JavaScript</li>
# <li class="green">Python</li>
# </ol>
# </body>

# Здесь мы получаем только тело/body веб-страницы

# Чтобы обратиться к элементу веб-страницы h1
print(parsed_html.body.h1)
# <h1>Web Development</h1>
# Получаем самый первый элемент h1

# Также можно обратиться к элементам li, которых там несколько
# Но, при этом надо сохранять иерархию
print(parsed_html.body.ol.li)
# <li>HTML</li>

# То же самое мы можем делать по  другому. Можем вызвать метод find().
print(parsed_html.find('li'))  # передаем строку с названием элемента
# <li>HTML</li>  - получаем самый первый li
# Хотя это выглядит как строка, но это не строка. Можно посмотреть его тип
print(type(parsed_html.find('li')))
# <class 'bs4.element.Tag'>
# Это элемент Tag типа bs4
# То есть, когда мы парсим html-код при помощи BeautifulSoup, он каждый тэг этого кода помещает в объект,
# с которым мы можем работать.

# Для того, чтобы получить все элементы li, нам нужно использовать метод find_all()
print(parsed_html.find_all('li'))  #
# [<li>HTML</li>, <li id="css-li">CSS</li>, <li class="green">JavaScript</li>, <li class="green">Python</li>]
# получаем весь html-код этих элементов.

# Так же, мы можем получить элемент по id или по классу.
print(parsed_html.find(id="css-li"))  #
# <li id="css-li">CSS</li>  - получаем именно этот элемент

# Для класса происходит то же самое.
# Если мы хотим выбрать все элементы какого-то класса, нужно использвать find_all()
# print(parsed_html.find_all(class='green'))  # но, здес мы не можем использвать слово class, так как оно зарезер-но
# поэтому указываем его с андерскором class_ - это надо помнить, когда вы работаете с BeautifulSoup
print(parsed_html.find_all(class_='green'))
# [<h1 class="green">Web</h1>, <li class="green">JavaScript</li>, <li class="green">Python</li>]
# получаем список всех элементов класса green

# Также, мы можем выбирать с помощью css-селекторов, используя ф-и select()
print(parsed_html.select('#css-li'))
# [<li id="css-li">CSS</li>]  - получаем тот же элемент, но уже в списке
# Для классов так же используем метод select()
print(parsed_html.select('.green'))  # но здесь через точку
# [<h1 class="green">Web</h1>, <li class="green">JavaScript</li>, <li class="green">Python</li>]
# Получаем такой же список
# То есть, при помощи метода select() всегда выдается список, даже если в списке один элемент.
# Если нам надо обратиться к какому-то конкретному элементу, мы можем обратиться по индексу.
print(parsed_html.select('.green')[1])  # здесь получаем второй элемент из этого списка.
# <li class="green">JavaScript</li>
print(parsed_html.select('#css-li')[0]) # здесь получаем перый элемент, но он единственный.
# <li class="green">JavaScript</li>  # получаем элемент JavaScript класса green
# Здесь уже вывод без квадратных скобок. То есть, это уже не список, а именно этот элемент,
# так как мы обращаемся по индексу именно к конкретному элементу этого листа.

# Также, мы можем извлекать элементы по их названиям
# Если мы не указываем индекс, мы получим список всех элементов
print(parsed_html.select('li'))
# [<li>HTML</li>, <li id="css-li">CSS</li>, <li class="green">JavaScript</li>, <li class="green">Python</li>]
# А если хотим получить какой-то конкретный, то указываем его индекс в списке
print(parsed_html.select('li')[3])
# <li class="green">Python</li>

# Но, допустим, мы хотим получить доступ не ко всему элементу <li class="green">Python</li>,
# а только к его атрибуту class="green", либо только к тексту 'Python', который находится внутри этого элемента
# Для этого есть отдельные методы.

# Присвоим код вызова отдельной переменной
html_elem = parsed_html.select('li')[3]
# Теперь, для того, чтобы получить текст из этого элемента, нам нужно использвать метод get_text()
print(html_elem.get_text())  # таким образом получаем доступ к тексту этого элемента
# Python  - получили текст 4-го элемента
# Получим текст из 1-го элемента
html_elem = parsed_html.select('li')[0]
print(html_elem.get_text())
# HTML

# Также, можем получить список всех элементов какого-то объекта
html_elem_list = parsed_html.select('li')  # здесь не указываем конкретный элемент
# И дальше можем распечатать каждый из этих элементов в цикле

for html_elem in html_elem_list:  # перебираем все элементы списка, находящегося в пересенной html_elem_list
    print(html_elem.get_text())  # выводим на экран содержимое (текст) этих элементов
    # HTML
    # CSS
    # JavaScript
    # Python

# Точно также мы можем обращаться и к классу.
# Выведем элементы класса 'green'
green_class_elem_list = parsed_html.select('.green')
for html_elem in green_class_elem_list:
    print(html_elem.get_text())
    # Получаем все элементы принадлежащие классу 'green'
    # Web
    # JavaScript
    # Python

# В основном, когда занимаются веб-скрапингом, делают это с целью получить текст элемента.
# Но, мы можем получать доступ не только к тексту, но и к имени элемента
green_class_elem_list = parsed_html.select('.green')
for html_elem in green_class_elem_list:
    print(html_elem.name)  # это обращение к именно к именам элементов класса 'green'
    # h1
    # li
    # li

# Также, мы можем обращаться к атрибутам, которые находятся в элементе.
# Атрибуты, это ключ-значение. Они могут быть самые разнообразные.
# Выберем аттрибуты элемента li
green_class_elem_list = parsed_html.select('li')
for html_elem in green_class_elem_list:
    print(html_elem.attrs)  #
    # {}   - у первого 'li' нет никаких атрибутов, поэтому получаем пустой словарь
    # {'id': 'css-li'}  - здесь получили атрибуты в виде пары ключ-значение
    # {'class': ['green', 'bold']}  - в этом элементе два класса 'green' и 'bold', поэтому они заключены в список
    # {'class': ['green']}  - здесь значение тоже заключено в список
    # {'class': ['green'], 'id': 'python-li'}  - в последнем элементе получаем Словарь, состоящий из двух элементов
    # в первом элементе Ключ - class, а значение - список, в котором находится одно значение 'green',
    # во втором случае Ключ - id, и, так как id может быть только один,
    # то значение дано без квадратных скобок, без списка.
    # Если мы захотим получить эти значения, нам нужно будет обращаться к ним через индекс

# Также мы можем при обращении к атрибутам, указать что именно нам надо.
# Например, если нам нужны классы, то пишем название класса, но если он там есть в этом елементе:
html_elem_list = parsed_html.select('li')[3]
print(html_elem_list.attrs['class'])  # в этом случае атрибут 'id' не будет выбран
# ['green'] - получили только класс из атрибута

html_elem_list = parsed_html.select('li')[3]
# print(html_elem_list.attrs['id'])  # в этом случае получаем 'id'
# python-li - получили только класс из атрибута
# Таким образом можно обращаться к конкретным атрибутам

# Так же можно обращаться с помощью более короткой записи
# Можно убрать вызов attrs и просто указать 'id'
# print(html_elem_list['id'])  # указываем, что нам нужен 'id' именно этого элемента
# Также и с классом. Если мы укажем класс, то получим класс
print(html_elem_list['class'])  # указываем, что нам нужен 'id' именно этого элемента
# ['green']

# Это были способы различных обращений к html-элементам, выбора разных нужных нам частей этого html-элемента:
# названия, атрибутов, текста



