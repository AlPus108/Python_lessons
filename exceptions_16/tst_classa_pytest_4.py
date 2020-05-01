import random

# Копируем класс из модуля OOP/incapsulation_9

class Dice_incap:
    def __init__(self, N):  # принимает на вход количество бросков (попыток)
        self.throw_num = N  # установленное количество бросков передаем переменной
        self.current_throw = 0  # количество текущих бросков

    def set_hidden_numbers(self):
        self.__hidden_num_1 = random.randint(1, 6)  # получаем первое рандомное число
        self.__hidden_num_2 = random.randint(1, 6)  # получаем второе рандомное число


    # Это та же самая ф-я, только с соответствующим названием - для смены значений,
    # название показывет цель действий пользователя
    def change_daces(self):
        self.__hidden_num_1 = random.randint(1, 6)  # первая кость
        self.__hidden_num_2 = random.randint(1, 6)  # вторая кость

    # Далее две ф-и по ручному вводу значений пользователем. Это сеттеры, которые устанавливают новые значения
    # Еще один плюс этих ручных настроек в том, что в них можно зашить проверку
    # Первая кость
    def set_dice_1(self, dice):
        # Здесь можно сделать проверку
        if (dice > 0) & (dice < 6): # если введено значение от 0 до 6
            self.__hidden_num_1 = dice  # выполняем присваивание
        else:   # иначе выкидываем ошибку
            raise ValueError('Числа должны быть от 1 до 6')


    # Вторая кость
    def set_dice_2(self, dice):
        self.__hidden_num_2 = dice
    # Теперь значения обоих __hidden_num нам доступны, потому что это внутри класса

    # Создаем ф-ю, которая будет просто возвращать нам значение
    # и обвесим ее встроенным декоратором property
    @property
    def hidden_num_1(self):
        return self.__hidden_num_1

    # Первая кость
    @hidden_num_1.setter  # В Питоне есть такие организованные декораторы для получения доступа к срытым переменным
    def hidden_num_1(self, dice):  # здесь указываем входную переменную dice
        if (dice > 0) & (dice < 6): # если введено значение от 0 до 6
            self.__hidden_num_1 = dice  # выполняем присваивание
        else:   # иначе выкидываем ошибку
            raise ValueError('Числа должны быть от 1 до 6')

    # То же самое и для второго параметра
    @property
    def hidden_num_2(self):
        return self.__hidden_num_2


    # Вторая кость
    @hidden_num_2.setter
    def hidden_num_2(self, dice):  # здесь указываем входную переменную dice
        if (dice > 0) & (dice < 6): # если введено значение от 0 до 6
            self.__hidden_num_2 = dice  # выполняем присваивание
        else:   # иначе выкидываем ошибку
            raise ValueError('Числа должны быть от 1 до 6')
    # Таким образом, теперь мы можем орбащаться к этим переменным просто через '='

    def get_dice_1(self):
        return self.__hidden_num_1  # просто возвращает значение

    def get_dice_2(self):
        return self.__hidden_num_2  # просто возвращает значение

    # Метод бросания костей
    # Если полученные значения совпадут со значениями, полученные в методе set_hidden_nummbers - это выигрыш.

    def throw_daces(self):
        dice_1 = random.randint(1, 6)  # первая кость
        dice_2 = random.randint(1, 6)  # вторая кость
        self.current_throw += 1  # считаем количество попыток
        if self.current_throw > self.throw_num:  # если кол-во попыток превышают установленное значение попыток
            raise Exception('Вы привысили количество попыток')  # выбрасываем исключение
        if {dice_1, dice_2} == {self.__hidden_num_1, self.__hidden_num_2}:
            return True
        else:
            return False


if __name__ == '__main__':
    dice_game = Dice_incap(2)  # создаем объект "Новый заход" класса Dice и передаем количество бросков
    dice_game.set_hidden_numbers()  # применяем к нему метод set_hidden_nummbers()

    print(dice_game.hidden_num_1, dice_game.hidden_num_2)
    # Так как параметры __hidden_num_1, __hidden_num_2 строго инкапсулированны - двойная земля,
    # то при попытке их вывести, будет выдана ошибка, что их не существует.
    # Хотя, можно ограничется и одной землей _hidden_num. Это визуально говорит о том, что данный метод инкапсулирован
    # но доступ к нему будет.
    # Поэтому пользуемся Геттерами
    # print(dice_game.get_dice_1(), dice_game.get_dice_2())  # проверяем настройки

    # -> 1
    # Проверяем работу декораторов.
    print(dice_game.hidden_num_1, dice_game.hidden_num_2)  # здесь, благодаря декоратору,
    # мы обращаемся к ф-ям hidden_num_1 и hidden_num_2 как к атрибутам.
    # При этом вызывается ф-я и мы получаем ее значение.


    # Для ручного ввода параметров вызываем Сетты
    dice_game.hidden_num_1 = 7
    dice_game.hidden_num_2 = 4

    print(dice_game.get_dice_1(), dice_game.get_dice_2())  # выводим на экран


    for i in range(4):
        try:
            print(dice_game.throw_daces())
        except:
            print('Игра закончена')

