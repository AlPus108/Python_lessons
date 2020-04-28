# МЕТОДЫ УРОВНЯ КЛАССА
# К ним можно обращаться через имя класса, а не через имя объекта. Они одинаковы для всех объектов этого класса.

# 1 Создаем класс
class Gamer:
    # -> 4 При инициализации нового игрока, будем фиксировать количество игроков в игре. Для этого создадим поле класса.
    # Это атрибут уровня класса - количество активных игроков
    active_gamers = 0  # изначально их 0. -> 5 ↓

    # -> 11 Метод на уровне класса.
    # Методы уровня класса используются довольно редко. Но, мы должны знать как он выглядит и как с ним обращаться.
    # Создадим метод, который будет возвращать количество всех игроков.
    # То есть, мы будем обращаться не через атрибут, как мы делали до этого, а через этот метод
    # Метод на уровне класса создается при помощи декоратора @classmetod
    @classmethod
    def get_active_gamers(cls):  # в скобках cls добавляется автоматически во все методы уровня класса
        return Gamer.active_gamers

    # Так как метод возвращает результат, а не распечатывает его, то выводим командой print при вызове --> 12 ↓

    # -> 13 Создадим еще одни метод, более приближенный к жизни.
    # Бывает, когда у вас есть какая-то информация в виде данных, разделенных запятыми, например в текстовом файле.
    # Допустим, эти данные об игроках. И мы можем использовать эти данные для создания игроков.
    # Но, добавлять в ручную каждую характеристику игрока, это очень долго. Это можно делать из файла.
    # Но, сейчас мы это сделаем со строки, из текста.
    # Создадим новый метод на уровне класса, который будет создавать объекты класса,
    # но пока без обращения к строке. Просто для примера.
    # Обращение к данным игрока будет через ключевой параметр cls
    # С помощью этого параметра cls можно создавать объекты класса также, как и через метод __init__
    @classmethod
    def gamer_from_cls(cls):
        # Игрок создается у нас при помощи ф-и __init__, но мы можем сделать то же самое при помощи обращения
        # через cls - параметр
        lacky = cls('hari', 16, 9, 108)  # передаем те же самые параметры и присваиваем это переменной
        print('Вывод данных об объекте через создающий объекты метод уровня класса - ', lacky.get_age())
        # метод будет выводить возраст игрока через обращение к Геттеру age
        # и далее вызываем метод --> 14 ↓

    # -> 15 Создаем метод, распознающий строку
    @classmethod
    def gamer_from_string(cls, data_string):  # сюда добавляем еще одни параметр - строку с данными.
        nickname, age, level, points = data_string.split(',')  # данные строки будут разделяться через ','
        return cls(nickname, age, level, points)  # объект будет создан через cls - параметр.
    # Теперь при помощи этого метода мы сможем создавать объекты класса.
    # Мы можем передать методу какую-то строку, в которой через запятую перечисленны нужные нам данные
    # Если есть файл с данными, мы можем аналогично считывать построчно данные из этого файла. --> 16 ↓

    # -> 2 создаем init этого класса, который принимает параметры, описывающие объект класса - игрока.
    def __init__(self, nickname, age, level, points):
        # параметр self добавляется аввтоматом во все методы уровня объекта
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        # -> 3
        # -> 5 Каждый раз, при создании нового объекта этого класса, мы будем увеличивать счетчик игроков +1
        Gamer.active_gamers += 1  # -> 6 ↓

    # -> 9 Так же мы можем создать метод, при помощи которого игроки будут выходить из игры
    # и тогда их количество будет уменьшаться.

    def logout(self):
        Gamer.active_gamers -= 1
        # -> 10 ↓

    # -> 3 Создадим Геттеры - методы, которые выдают информацию об атрибутах этого класса
    # Они будут возвращать имя, возраст, уровень игрока, и количество очков
    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18
    # -> 4 ↑

    # 6 В зависимости от того, совершеннолетний игрок или нет (проверяется по последнему Геттеру),
    # игроку разрешается или запрещается переходить на уровень для взрослых
    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print('You can\'t go to adult level')


# 7 Создаем объекты этого класса
gamer_1 = Gamer('hell_boy', 23, 5, 13)
print('Количество игроков после создания первого игрока - ', Gamer.active_gamers)  # 1
gamer_2 = Gamer('harry_potter', 12, 3, 5)
print('Количество игроков после создания второго игрока - ', Gamer.active_gamers)  # 2

# Проверяем количество игроков


# 8 Теперь мы можем получать информацию об игроках при помощи Геттеров или через прямое обращение к атрибутам.

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()  # здесь мы просто вызываем метод без print и он сам распечатывает информацию
# 23
# You can go to adult level

print(gamer_2.get_age())
gamer_2.get_adult_level_permission()  # здесь мы просто вызываем метод без print и он сам распечатывает информацию
# 12
# You can't go to adult level

# У нас должен изменяться атрибут уровня класса active_gamers
# Проверим
print('Количество игроков (через атрибут) - ', Gamer.active_gamers)  # 2  - обращение через атрибут
# -> 9 ↑

# -> 10 Один игрок у нас вышел из игры
gamer_1.logout()
print('Количество игроков после выхода одного из игры - ', Gamer.active_gamers)  # 1
# -> 11

# -> 12 Выводим результат работы метода уровня класса
print('Количество игроков (через метод уровня класса) - ', Gamer.get_active_gamers())
# Вывод: 2 - обращение через метод уровня класса
# -> 13 ↑

# -> 14 Вызываем метод уровня класса
Gamer.gamer_from_cls()
# Далее, создадим метод, принимающий строку с параметрами --> 15 ↑

# -> 16 Создаем новых игроков через метод класса, считывающий строку
james = Gamer.gamer_from_string('James, 34, 5, 16')
jane = Gamer.gamer_from_string('Jane, 24, 4, 5')
print(james.get_age())  # 34
print(jane.get_level())  # 4

# Проверяем количество игроков
print(Gamer.get_active_gamers())  # 4




