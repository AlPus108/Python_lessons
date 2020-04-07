# МЕТОДЫ УРОВНЯ КЛАССА
# К ним можно обращаться через имя класса, а не через имя объекта. Они одинаковы для всех объектов этого класса.

# 1 Создаем класс
class Gamer:
    # 4 При инициализации нового игрока, будем фиксировать количество игроков в игре. Для этого создадим поле класса.
    # Это атрибут уровня класса
    active_gamers = 0  # изначально их 0.

    # 2 создаем init этого класса, который принимает параметры, описывающие объект класса - игрока.
    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        # 5 Каждый раз, при создании нового объекта этого класса, мы будем увеличивать счетчик игроков +1
        Gamer.active_gamers += 1

    # 3 Создадим Геттеры - методы, которые выдают информацию об атрибутах этого класса
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

    # 6 В зависимости от того, совершеннолетний игрок или нет (проверяется по последнему Геттеру),
    # игроку разрешается или запрещается переходить на уровень для взрослых
    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print('You can\'t go to adult level')


# 7 Создаем объекты этого класса
gamer_1 = Gamer('hell_boy', 23, 5, 13)
gamer_2 = Gamer('harry_potter', 12, 3, 5)

# 8 Теперь мы можем получать информацию об игроках при помощи Геттеров или через прямое обращение к атрибутам.

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()  # здесь мы просто вызываем метод без print и он сам распечатывает информацию
# 23
# You can go to adult level

print(gamer_2.get_age())
gamer_2.get_adult_level_permission()  # здесь мы просто вызываем метод без print и он сам распечатывает информацию
# 12
# You can't go to adult level


