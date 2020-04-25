import requests
from bs4 import BeautifulSoup

# Это разбор практичкского задания по парсингу данных из веб-страницы.
# Мы должны отпарсить сайт и записать данные в файл формата cvs.

# response = requests.get('http://quotes.toscrape.com')
# html_data = BeautifulSoup(response.text)
# quotes = html_data.find_all(class_='quote')
# for quote in quotes:
#     print(quote.find(class_='text'))
# quotes = html_data.find_all(class_='quote')
# for quote in quotes:
#     print(quote.find(class_='text').get_text())
#     print(quote.find(class_='author').get_text())
#     print(quote.find(class_='keywords')['content'])

# Этот код скопирован из папки Web-parsing файл 4_quotes_scraping, где был рассмотрен

# Импортируем модуль csv

import csv

# Используем верхний код.

response = requests.get('http://quotes.toscrape.com')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_='quote')

# Только, вместо того, чтобы распечатывать, нам нужно добавить все в файл

with open('quotes.csv', 'w') as file:
    csv_writer = csv.writer(file)
    # сначала запишем заголовки: текст, автор, теги
    csv_writer.writerow(['Text', 'Author', 'Keywords'])
    for quote in quotes:
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        keywords = quote.find(class_='keywords')['content']
        # далее в цикле добавляем строку с этими данными
        csv_writer.writerow([text, author, keywords])

# В текущей папке создался файл quotes.csv
# Содержимое файла:
# Text,Author,Keywords
#
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”,Albert Einstein,"change,deep-thoughts,thinking,world"
#
# "“It is our choices, Harry, that show what we truly are, far more than our abilities.”",J.K. Rowling,"abilities,choices"
#
# “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”,Albert Einstein,"inspirational,life,live,miracle,miracles"
#
# "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”",Jane Austen,"aliteracy,books,classic,humor"
#
# "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",Marilyn Monroe,"be-yourself,inspirational"
#
# “Try not to become a man of success. Rather become a man of value.”,Albert Einstein,"adulthood,success,value"



