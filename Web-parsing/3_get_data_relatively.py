# Получение данных относительно html-документов

from bs4 import BeautifulSoup


# Рассмотрим наш код

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
            <li class="green bold" id="python-li">Python</li>
        </ol>

    </body>
    </html>


"""
# Элемент body
# Включает в себя дочерние элементы, то есть своих птомков, которые окружены открывающим тегом <body>
# и закрывающим тегом <body>
'''
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
'''
# Соответственно, внутри тега <ol> находятся потомки <li>
# Точно также элементы <head> и <body> находятся в своем родителе <html>
# То есть, относительнро внешего тега внутрении называется потомком, вшение теги относительно внутренних - родители.
# Теперь мы будем пробовать извелкать данных исходя из этих наследственных отношений: родитель - потомок.
# Элементы, находящиеся на одном уровне иерархии, называются sibling (родной брат) - элементы одного уровня.

# Теперь давайте получим доступ к body

parsed_html = BeautifulSoup(html_string, 'html.parser')
# data = parsed_html.body
# Чтобы получить внутренний контект body, всех его потомков
data = parsed_html.body.contents
print(data)
# ['\n', <h1>Web Development</h1>, '\n', <h1 class="green">Web</h1>, '\n', <h3>Programming Languages</h3>, '\n', <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green bold">JavaScript</li>
# <li class="green">Python</li>
# <li class="green" id="python-li">Python</li>
# </ol>, '\n']
# Вывод начинается с '[' и закончивается ']' - получаем данные в виде списка.
# Все элементы перечислены через запятую. В пределах [] тега li нет, так как мы сейчас получили доступ только
# к потомкам body. <li> - потомки <ol> и они выводятся внутри него, но запятые между ними не стоят.
# То есть, <ol> мы получаем как целое значение со всеми его внутренносями.
# Но также, по мимо этого, мы получаем знаки перехода на новую строку '\n'.
# То есть. если мы захотим обратиться к элементу <h1> по его индексу, то будем обращаться к индексу [1],
# так как в индексе [0] находится знак переноса строки '\n'
data = parsed_html.body.contents[1]
print(data)
# <h1>Web Development</h1>
# Если же укажем первый индекс [0], то получим пустую строку.
# Чтобы получить <ol>, надо обратиться к 7-му индексу
data = parsed_html.body.contents[7]
print(data)
# <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green bold">JavaScript</li>
# <li class="green">Python</li>
# <li class="green" id="python-li">Python</li>
# </ol>

# если укажем contents дважды, то получим содержимое <ol>
data = parsed_html.body.contents[7].contents
print(data)
# ['\n', <li>HTML</li>, '\n', <li id="css-li">CSS</li>, '\n', <li class="green bold">JavaScript</li>,
# '\n', <li class="green">Python</li>, '\n', <li class="green" id="python-li">Python</li>, '\n']
# Получаем список, в котором содержатся потомки <ol> - элементы <li>

# Обратимся к первому элементу - h1
data = parsed_html.body.contents[1]
print(data)
# <h1>Web Development</h1>
# Если нам надо получить элементы на том же уровне, что и <h1> (sibling), можно обращаться к следующему сиблингу
# при помощи атрибута next_sibling
data = parsed_html.body.contents[1].next_sibling
print(data)
# Получаем пустую строку, так как там переход после <h1>
# Если надо получить второй <h1>, можно дописать еще один next_sibling
data = parsed_html.body.contents[1].next_sibling.next_sibling
print(data)
#  - здесь пробел
# <h1 class="green">Web</h1>
# Вот так последовательно мы можем получать элемент за элементом
data = parsed_html.body.contents[1].next_sibling.next_sibling.next_sibling.next_sibling
print(data)
# <h3>Programming Languages</h3> - получили последний элемент

# Так же мы можем получить родителя.
# Мы можем получит доступ к <li> - элементу по id через метод find()
data = parsed_html.find(id='css-li')
print(data)
# <li id="css-li">CSS</li>
# Также, мы можем получить его родителя - <ol>
data = parsed_html.find(id='css-li').parent
print(data)
# <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green bold">JavaScript</li>
# <li class="green">Python</li>
# <li class="green" id="python-li">Python</li>
# </ol>
# Получаем полностью весь <ol>

# Если еще раз вызовем parent, то получим <body>
data = parsed_html.find(id='css-li').parent.parent
print(data)
# <body>
# <h1>Web Development</h1>
# <h1 class="green">Web</h1>
# <h3>Programming Languages</h3>
# <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green bold">JavaScript</li>
# <li class="green">Python</li>
# <li class="green" id="python-li">Python</li>
# </ol>
# </body>

# Помимо атрибута next_sibling, есть атрибут previous_sibling - предыдущий код
data = parsed_html.find(id='css-li').parent.previous_sibling
print(data)
# Здесь поулчаем пустую строку, так как предыдущая строка к <ol> пустая.
# Добавляем еще одни сиблинг
data = parsed_html.find(id='css-li').parent.previous_sibling.previous_sibling
print(data)
# <h3>Programming Languages</h3>

# Итак, мы научились с вами обращаться при помощи различных атрибутов иерархически к разным элементам
# Далее рассмотрим, как можно делать то же самое при помощи методов.

# Обратимся к элементу <li> с id='css-li'
# Мы уже деллали это
data = parsed_html.find(id='css-li')
# и теперь далее получим доступ к слудеющему <li>
data = parsed_html.find(id='css-li').next_sibling
print(data)

#
# <h3>Programming Languages</h3>
# Здесь сначала мы получаем пробел, так как там перед элементом знак перехода на новую строку,
# а затем уже сам элемент. Чтобы обратиться к следующему элементу, нам нужно учитывать и пустые строки.
# Но, есть еще метод find_next_next_sibling(), и, если мы обратимся с помощью него, то знаки перехода
# на новую строку не учитываются.
data = parsed_html.find(id='css-li').find_next_sibling()
print(data)
# <li class="green bold">JavaScript</li>
# В данном случае без пробела. Переходы на новую строку не учитываются. Так намного удобнее.
# Получаем следующий элемент того же уровня
data = parsed_html.find(id='css-li').find_next_sibling().find_next_sibling()
print(data)
# <li class="green">Python</li>

# Также, здесь можем получить доступ к предыдущему элементу
data = parsed_html.find(id='css-li').find_next_sibling().find_previous_sibling()
print(data)
# <li id="css-li">CSS</li>

# Также, мы можем указывать определенные атрибуты
# В двух наших сиблингах у одного есть id="python-li". Мы можем получить это элемент по его id
data = parsed_html.find(id='css-li').find_next_sibling(id='python-li')
print(data)
# <li class="green" id="python-li">Python</li>
# Здесь мы получаем не следующий сиблинг, а тот, который содержит id, указанное в атрибутах. То есть, через один
# после элемента с id='css-li'
# Также мы можем сдесь указывать вместо атрибута класс через андерскор
data = parsed_html.find(id='css-li').find_next_sibling(class_='bold')
print(data)
# <li class="green bold">JavaScript</li>
# Здесь также получаем элемент через один.

# Таже, мы можем найти родителя определенного элемента
data = parsed_html.find(id='css-li').find_next_sibling(class_='bold').find_parent()
print(data)
# </ol>

# Эту цепочку роидтелей мы можем продолжить и найти следующего родителя текущего родителя
data = parsed_html.find(id='css-li').find_next_sibling(class_='bold').find_parent().find_parent()
print(data)
# </body>


# Также, можем найти потомков родителя. Например, найдем потомков body
data = parsed_html.body
print(data)
# <body>
# <h1>Web Development</h1>
# <h1 class="green">Web</h1>
# <h3>Programming Languages</h3>
# <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green bold">JavaScript</li>
# <li class="green">Python</li>
# <li class="green bold" id="python-li">Python</li>
# </ol>
# </body>
# Здесь получаем все тело body
# Используем метод findChildren() для поиска его потомков
data = parsed_html.body.findChildren()
print(data)
# [<h1>Web Development</h1>, <h1 class="green">Web</h1>, <h3>Programming Languages</h3>, <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green bold">JavaScript</li>
# <li class="green">Python</li>
# <li class="green bold" id="python-li">Python</li>
# </ol>, <li>HTML</li>, <li id="css-li">CSS</li>, <li class="green bold">JavaScript</li>, <li class="green">Python</li>,
# <li class="green bold" id="python-li">Python</li>]
# Получаем список всех потомков элемента body
# Здесь мы получаем потомков без знаков перехода на новую строку.
# Можем получить конкретного потомка через его индекс
data = parsed_html.body.findChildren()[2]
print(data)
# <h3>Programming Languages</h3>
# Дальше можем получить следующий сиблинг
data = parsed_html.body.findChildren()[2].find_next_sibling()
print(data)
# То есть, мы можем делать цепочки этих методов, связывая их.
# <ol>
# <li>HTML</li>
# <li id="css-li">CSS</li>
# <li class="green bold">JavaScript</li>
# <li class="green">Python</li>
# <li class="green bold" id="python-li">Python</li>
# </ol>
# Здесь мы получаем все тело следующего сиблинга <ol>



