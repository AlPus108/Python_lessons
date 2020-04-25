# Здесь мы научимся получать конект с веб-сайтов

# Для обучения будем использовать веб-сайт, который создан именно для этих целей

# http://quotes.toscrape.com

# В нем помещены различные циататы разных авторов
# Мы будем получать с этого сйта сам текс цитаты и автора цитаты.
# Также, под каждой цитатой там есть теги, которые мы также можем получить.

# Прежде всего нам нужнро импортировать соответствующие модули

import requests
from bs4 import BeautifulSoup

# Создаем переменную, в которую передаем адрес сайта
response = requests.get('http://quotes.toscrape.com')
# далее распечатываем переменную с ее содержимым
# print(response.text)
# Получаем довольно массивный html-код с этого сайта
# В терминале все это выглядит запутано и не очень хорошо видно.
# Поэтому лучше перейти на сам сайт и открыть инструмент разработчика через ПКМ - "Исследовать элемент"

# В div class='row' находятся все элементы с цитатами.
# В нем находятся дивы с разными цитатами, к которым мы можем обращаться и выбирать все цитатаы.

# Создаем переменную
html_data = BeautifulSoup(response.text)
# То есть, здесь мы присваиваем этой переменной весь html-код этой страницы
# Создаем еще одну переменну для цитат
# quotes = html_data.find_all(class_='quote')
# print(quotes)
# Здесь мы получаем все дивы с цитатами в виде списка
# В этом диве класса quote находится класс span с классом text
# В нем находится сам текст цитаты. Мы можем обратиться по классу и получить этот текст
# Проделаме это в цикле
quotes = html_data.find_all(class_='quote')
for quote in quotes:
    print(quote.find(class_='text'))
# <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
# <span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>
# <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>
# <span class="text" itemprop="text">“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>
# <span class="text" itemprop="text">“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”</span>
# <span class="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>
# <span class="text" itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</span>
# <span class="text" itemprop="text">“I have not failed. I've just found 10,000 ways that won't work.”</span>
# <span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</span>
# <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>
# Мы получаем все элементы span с классом text
# Но, на самом деле, нам нужен сам текст
# Поэтому просто добавляем метод get_text()
quotes = html_data.find_all(class_='quote')
for quote in quotes:
    print(quote.find(class_='text').get_text())
    # “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
    # “It is our choices, Harry, that show what we truly are, far more than our abilities.”
    # “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
    # “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
    # “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
    # “Try not to become a man of success. Rather become a man of value.”
    # “It is better to be hated for what you are than to be loved for what you are not.”
    # “I have not failed. I've just found 10,000 ways that won't work.”
    # “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
    # “A day without sunshine is like, you know, night.”
    # Получаем все цитаты, которые находятся на этой странице. Это только одна страница!

    # Еще, помимо текста, мы можем извелечь автора и теги.
    # В каждом диве класса quote находится span класса text (его мы уже извлекли). Получим из него автора
    print(quote.find(class_='author').get_text())
    # “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
    # Albert Einstein
    # “It is our choices, Harry, that show what we truly are, far more than our abilities.”
    # J.K. Rowling
    # “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
    # Albert Einstein
    # “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
    # Jane Austen
    # “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
    # Marilyn Monroe
    # “Try not to become a man of success. Rather become a man of value.”
    # Albert Einstein
    # “It is better to be hated for what you are than to be loved for what you are not.”
    # André Gide
    # “I have not failed. I've just found 10,000 ways that won't work.”
    # Thomas A. Edison
    # “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
    # Eleanor Roosevelt
    # “A day without sunshine is like, you know, night.”
    # Steve Martin
    # Теперь мы получаем саму цитату с подписью автора.

    # Далее ищем див класса tags. В нем находится объект meta класса keywords
    # Мы можем получить этот элемент meta с указанием его атрибута content, в котором находятся теги.
    # То есть, нам нужен элемент по классу keywords
    print(quote.find(class_='keywords')['content'])
    # “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
    # Albert Einstein
    # change,deep-thoughts,thinking,world
    # “It is our choices, Harry, that show what we truly are, far more than our abilities.”
    # J.K. Rowling
    # abilities,choices
    # “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
    # Albert Einstein
    # inspirational,life,live,miracle,miracles
    # “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
    # Jane Austen
    # aliteracy,books,classic,humor
    # “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
    # Marilyn Monroe
    # be-yourself,inspirational
    # “Try not to become a man of success. Rather become a man of value.”
    # Albert Einstein
    # adulthood,success,value
    # “It is better to be hated for what you are than to be loved for what you are not.”
    # André Gide
    # life,love
    # “I have not failed. I've just found 10,000 ways that won't work.”
    # Thomas A. Edison
    # edison,failure,inspirational,paraphrased
    # “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
    # Eleanor Roosevelt
    # misattributed-eleanor-roosevelt
    # “A day without sunshine is like, you know, night.”
    # Steve Martin
    # humor,obvious,simile
    # Мы получили цитаты с указанием их авторов и тегов
    # То есть, мы получили все данные, которые в дальнейшем мы можем сохранить в какой угодно форме в базе данных
    # в CSV-файле

# Далее смотри разделы по CSV-файлам и Базе данных, где рассмотрим, как с этим работать дальше.
# По CSV-файлам смотри в разделе CVS-files - 5_4_quotes_scraping_reshenie


