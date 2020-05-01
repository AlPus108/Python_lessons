# Здесь будет делать тесты библиотекой Unittest

# Импортируем библиотеку unittest и тестируемый класс из модуля tst_classa_pytest_4

import unittest

from tst_classa_pytest_4 import Dice_incap


#  Создаем класс
class TestDice_unittest(unittest.TestCase):  # чтобы применять методы unittest,
    # мы должны унаследовать этот класс от класса unittest
    # В unittest есть аналог ф-ий из pytest. Там они наываются setup() и teardown()
    # эти две ф-и будут выполняться при вызове каждого теста написанного далее в коде.
    # по функциональности они чем-то похожи на декоратор
    def setUp(self):
        print('Start test')
        # и создаем объект dice_game
        self.dice_game = Dice_incap(3)  # теперь объект dice_game является объектом класса TestDice_unittest
        # и мы можем его использовать в других ф-ях.
        # Также в сетап вставим инициализацию костей. Сначала их созадем строчкой выше и затем вызываем
        self.dice_game.set_hidden_numbers()

    def tearDown(self):
        self.dice_game.current_throw = 0  # по завершению теста обнуляем счетчик current_throw
        print('Test completed!')
        # Обычно, при окончании теста, делают чистку памяти.
        # Мы удалим созданный объект dice_game, потому что при каждом запуске будет создаваться новый
        del self.dice_game


    # Дальше переписываем классы из test_pytest_dice_5 и подправляем их под синтаксис unitttest
    # В Unittest есть много различных ф-й, которые включают в себя assert, но они весьма конкретные
    # Вот выражение из pytest
    # assert self.dice_game.throw_num == 2  - если эти два выражения не равны друг другу, то вызывается assert
    # В unittest пишем по другому
    def test_unit(self):
        self.assertEqual(self.dice_game.throw_num, 3)  # при унаследовании от unittest, у объекта self появляются
        # различные ф-и этго класса. В скобках перечисляются сравниваемыые параметры.
        # Здесь применяем уже встроенный метод assertEqual класса unittest.
        self.assertFalse(self.dice_game.throw_num > 0)  # ф-я assertFalse проверяет, является ли выражение ложным.
        # если выражение ложное, то assert не возникает, если истинно - возникает assert

    def test_dice_setter(self):
        self.dice_game.hidden_num_1 = 5
        self.dice_game.hidden_num_2 = 5
        self.assertTrue((self.dice_game.hidden_num_1 == 5) & (self.dice_game.hidden_num_2 == 5))
        # здесь происходит проверка на истинность выражения - если это так, то все хорошо, если нет - выдается ошибка.

        # with pytest.raises(ValueError):  - это выражение из pytest, переписываем его для unittest
        with self.assertRaises(TypeError):  # ValueError - должно быть, но так как TypeError - выбросится ошибка.
            # далее идет следующий код, который должен вызвать ошибку ValueError. Если это ошибка именно ValueError
            # то тогда ошибка выброшена не будет, а если не она - будет assert
            self.dice_game.hidden_num_1 = 6  # происходит присваивание значение за пределами диапазона

    def test_throw_dices(self):

        # Ради примеров придумываем тесты
        # создаем пустой список бросков
        list_throw = []
        list_throw.append(self.dice_game.current_throw)  # вносим в него первый бросок
        self.dice_game.throw_daces()
        list_throw.append(self.dice_game.current_throw)  # вносим в него второй бросок

        self.assertTrue(self.dice_game.current_throw == 1)  # после первого броска результат True
        # этот тест будет пройден, так как после первого броска current_throw действительно == 1

        # Применяем ф-ю сравнения значений
        self.assertListEqual(list_throw, [0, '1'])  # намерено совершаем ошибку - второй аргумент в строковом типе
        # Получаем ошибку
        # AssertionError: Lists differ: [0, 1] != [0, '1']



        # Библиотеку unittest состоит из таких отдельных ф-ий assert
        # Более подробней о них можно почитать на официальном сайте документацию



