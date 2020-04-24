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
            <li class="green">JavaScript</li>
            <li class="green">Python</li>
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
