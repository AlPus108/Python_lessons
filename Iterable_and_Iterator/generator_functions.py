# ГЕНЕРАТОРЫ
# Генераторы, это итераторы. При помощи генераторов мы можем перебирать какой-то iyerable
# Не каждый итератор является генератором.
# Но, все генераторы являются итераторами.
# Генераторы могут быть созданы при помощи ф-и generator
# Так же, генераторы могут быть созданы при помощи generator expressions (генераторы выражений)

# Здесь разберем, как создавать генераторы при помощи ф-й генераторов
# Мы уже разбирали ф-и, которые могут возвращать какое-то значание.


def my_function(x):
    return x


my_function(4)  # 4 - получаем значение, возвращаемое этой ф-ей

# ф-и генераторы тоже возвращают значения, но они могут возвращать значения из последовательности несколько раз.
# И возвращают они это значение не при помощи ключевого слова return, а при помощи слова yield (йилд)
# Слово yield в английском языке имеет много значений: уступать, выработать. То есть - вырабатываются какие-то значения.
# И вырабатываться они могут несколько раз.
# В случае с обычной ф-ий мы получаем возвращаемое значение. В случае с функцией-генераторм, мы возвращаем генератор.
# Генератор, в свою очередь, является итератором.
# Это немного запутано, поэтому, лучше разобрать на практике.
# Создадим нашу первую функцию-генератор


def count_up_to(x):  # 'считать до..'
    count = 1        # создаем переменную с начальным значением
    while count <= x:
        yield count
        count += 1


# Запускаем ф-ю
print(count_up_to(3))
# <generator object count_up_to at 0x02E9EAE0>
# Мы получаем generator object - объект класса generator
# Эта ф-я произвела генератор.
# Когда мы используем в ф-и ключевое слово yield, автоматически мы получаем из этой ф-и генератор.
# С этим генератором мы можем поместить значение, которое вырабатывает эта ф-я, в переменную.
counter = count_up_to(3)
# Nак как это генератор, который в свою очередь является итератором, у него есть метод next()
# И этот метод мы можем назначить переменной.
# print(counter.__next__())  # 1
# # если повторим
# print(counter.__next__())  # 2
# print(counter.__next__())  # 3
# print(counter.__next__())  # StopIteration
# На последенм шаге получаем ошибку StopIteration

# То же самое, по-мимо метода next(), мы можем проделать при помощи ф-и next.
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# Что же тут происходит?
# def count_up_to(x):  # 'считать до..'
#     count = 1        # создаем переменную с начальным значением
#     while count <= x:
#         yield count
#         count += 1

# Эта фунция-генератор count_up_to, которая генерирует сам генератор,
# который мы потом помещаем в counter = count_up_to(3), он запускается.
# После слова yield вырабатывается текущее значение, которое помещено в count.
# После этого ф-я как-бы становится на паузу, засыпает.
# После этого значение возвращается из этой ф-и, count прибавляется 1, count += 1. Ф-я остановлена.
# И, при последующем запуске в count уже находится не 1, а 2. То есть, запоминается предыдущее значение.
# Оно не обнуляется, как в случае с обычной ф-ей. И, каждый раз, мы получаем новое значение до тех пор,
# пока не будет получена ошибка StopIteration
# То есть, при помощи ф-и генератора, мы можем легко получать пследовательность iterable и использовать ее в цикле.

for number in count_up_to(10):  # вызываем ее в цикле
    print(number)
    # получаем вывод от 1 до 10

# То есть, нам не нужно имплементировать для этого, как мы делали в кастомном классе MyRange (пакет 2_custom_iterable)
# методы next и iter.
# Здесь при помощи вот такой ф-и генератора мы можем создавать такую же функциональность.
# Фишка в том, что при помощи ф-и генератора, когда мы вырабатываем значение с помощью ключевого слова yield,
# мы не обнуляем все наши действия. И, в следующий раз, при вызове метода next, будет использовано значение не с начала,
# а с того значения, на котором была остановка.

# В цикле for остановка происходит также на выбросе ошибки StopIteration, но там эта ошибка обрабатывается
# при помощи конструкции try - except, поэтому мы ее не замечаем
# и программа не останавливается и выполянет следующий код.

# Резюме по созданной нами ф-и count_up_to()
# Здесь мы также можем работать не только с числами, но и с любыми последовательностями и производить любые манипуляции.
# Эта ф-я, логика которой может быть какой угодно до ключевого слова yield, которое вырабатываем какое-то значение,
# которое будет помещено в переменную. Затем ф-я останавливается/засыпает и сохраняет свое состояние -
# запоминает, где она остановилась. И, при следующем вызове, будет продолжена работа с запомненного значения.
# То есть, будет выработан следующий элемент последовательности. Каждый раз вырабатывается только один элемент из
# последовательности. Мы, конечно, можем сгенерировать все элементы последовательности при помощи list

print(list(count_up_to(7)))  # [1, 2, 3, 4, 5, 6, 7]
# получим последовательность в форме списка





