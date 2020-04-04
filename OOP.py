# ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ

# Концепция ООП - это описание с помощью языка программирование объектов окружающего мира, либо какого-то процесса,
# который существует в окружающей нас действительности: пользователь, приложение, дом, машина, расписание занятий,
# какой-то банковский счет можно описать при помощи этой концепции.
# Для описания объектов при помощи языка программирования, испльзуются такие понятия, как классы и объекты.
# Класс подобен чертежу объкта или рецепту изготовления какого-то блюда, либо спецификация, по которой изготавливаются
# все объекты этого класса. Внутри класса описываются атрибуты и методы, которые затем содержаться в каждом объекте
# этого класса. Каждый автомобиль имеет какое-то количество колес, цвет, год выпуска, кол-во дверей.
# Все эти свойства автомобиля можно описать в атрибутах класса.
# Каждый автомобиль имеет способность к передвижению, возможность сигналить. Все эти и другие действия,
# которые может совершать объект класса, описываются в методах класса.
# И далее каждый объект класса имеет все эти свойства уже со своими персональными значениями.
# Методы, это те же функции. То есть, в каждом классе создаются какие-то функции, которые затем могут использовать
# объекты этого класса. Эти функции класса называются методами класса.
# В Пайтоне также есть и втроенные классы. Но, если мы хотим описать какой-то сторонний объект, то мы должны создать
# свой собственный класс с атрибутами и методами, которые нужны нм для реализации кокой-то функциональности
# объектов этого класса.

# Если ввести help(list), мы получим всю документацию по классу list
# Класс list, это встроенный класс со своими методами
help(list)
# Методы этого класса можно использовать для объектов данного класса.
# Когда мы созадем список
my_list = [1, 2, 3]
# в данном случае мы создаем объект класса list, который содежит в себе конкретные значения, и ссылку на эти значения
# мы передаем переменной my_list
# И далее, мы можем вызывать любой из методов, перечисленные в спецификации к этому классу, для объектов этого класса.
my_list.append(4)
# В Питоне есть большое количество встроеных классов, которые содержат различные атрибуты и методы.
# Но, если нам не хватает их функционала, мы можем создать собственный класс.
# Класс начинается с ключевого слова class и название класса всегда мишется с ЗаглавнойБуквы

class MyFirstClass:
    # Сохраняется отступ
    # Записываем какие-то атрибуты и методы
    pass


# Создаем объект класса
object_of_my_class = MyFirstClass()  # создаем переменную класса (назвать можно как угодно)
# Смотрим тип переменной
print(type(object_of_my_class))
# <class '__main__.MyFirstClass'>
# Это переменная созданного нами класса

# Создадим класс, описывающий автомобиль

class Car:
    # Первое, что пишем, при определении класса, это его специальный метод __init__() с андерскором (подчеркивания)
    # Это обязательный метод, который есть в каждом классе и который иницианилизует, создает объекты
    # Метод, это та же ф-я, находящаяся внутри класса. Поэтому метод определяется также, как и ф-я - через def

    wheels_number = 4  # - атрибут, общий для всех объектов данного класса

    def __init__(self, name, color, year, is_crashed):  # в классе может быть много атрибутов
        # Помещая атрибуты в класс, мы декларируем, что каждый объект этого класса убдет иметь такие атрибуты
        # В скобках автоматом вставляется ключевое слово self, после которого перечисяются названия атрибутов,
        # которые мы помещаем в этот класс. Атрибуты описывают свойства какого-то объекта из реального мира.
        # Дальше описываем тело метода, в котором будем производить какие-то действия
        # а именно - описываем атрибуты автомобиля
        # При помощи слова self для каждого атрибута этого класса мы можем присваивать какое-то значение.
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed  # была ли машина в аварии? Тип bool

# Создаем объект класса Car
mazda_car = Car(name='Mazda CX', color='Yellow', year=2017, is_crashed=True)
# в скобках вставляем значения для атрибутов, которые определены в этом классе

# Дальше мы можем обратиться к атрибуту этого объекта
print(mazda_car.name)  # после точки выпадает список с предоределенными методами (с андерскором)
print(mazda_car.color)  # в т.ч там есть и наши атрибуты, которые принадлежат классу Car
print(mazda_car.is_crashed)
# Mazda CX
# Yellow
# True
# Таким образом мы создали Класс и его Объект.
# Метод init() вызывается каждый раз, когда создается объект класс. Он определяет значения для всех объектов класса,
# которые передаются конкретным объектам через ключевое слово self (свой, собственный атрибут объекта)

# Создаем еще один объект класса Car
bmw_car = Car(name='BMW 7s', color='Black', year=2018, is_crashed=False)  # Присваиваем значения его атрибутам
print(bmw_car.name)  # BMW 7s
print(bmw_car.year)  # BMW 7s

# Если мы не присвоим значение хотя бы одному атрибуту, получим ошибку.
# Мы можем давать объектам атрибуты ранзых типов. Это могут быть списки, Таплы, Словари
# Например, is_crashed - параметр типа bool

# Мы разобрали, как присваивать значения атрибутам вновь созданного объекта.
# Но, допустим, есть свойство, которое присуще, одинаково для всех объектов этого класса
# Например, у всех автомобилей 4 колеса. И мы должны иметь возможность обратиться к этому свойству и к его значению.
# Можно, конечно поместить его в метод init() и дать ему значение wheels_number = 4.
# Но, тогда нам бы пришлось при создани объектов передавать каждому объекту одинаковое значение - 4.
# Для таких случаев, когда у всех объектов одного класса какое-то свойство имеет одно и тоже значение,
# существуют атрибуты уровня Класса. Ключевое слово Self обращается к вновь созданному объекту и присваивает
# его атрибуту какое-то значение. Но, мы можем создать атрибут для каждого объекта класса вне методов,
# и все объекты этого класса будут иметь этот атрибут с уже присвоеным значением, одинаковым для всех.
# И его уже не нужно прописывать в методе init() и передавать в параметры объектам.
# Но, выводить его можно так же для каждого объекта

print(mazda_car.wheels_number)
print(bmw_car.wheels_number)
# Получили для всех значение 4
# При этом мы не прописывали внутри каждого объекта этот параметр и не передавали каждому объекту его значение.
# Он для всех одинаковый.
# Так как это атрибут класса, то мы можем обращаться к нему не через объект, а через сам класс
# Допустим, мы хотим посчитать количество колес для трех автомобилей

number_of_wheels_of_3_cars = Car.wheels_number * 3  # обращаемся непосредственно к классу Car
print(number_of_wheels_of_3_cars)  # 12

