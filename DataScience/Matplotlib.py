import numpy as np
import matplotlib.pyplot as plt

# pyplot - ключевой модуль библиотеки matplotlib

# Рисуем ф-ю y = x**2 * e**(-)x**2

# Создаем равномерно распределенное множество
X = np.linspace(0, 3, 1001, dtype=np.float32)

print(X)  # [0.    0.003 0.006 ... 2.994 2.997 3.   ]

# Возведем 'x' в квадрат

print(X**2)
# [0.000000e+00 9.000000e-06 3.600000e-05 ... 8.964036e+00 8.982009e+00
#  9.000000e+00]
# Операция происходит над каждым элементом массива в отдельности
# Все операции над массивами в NumPy совершаются с каждым членом отдельно.
# Если нужно иное, то на это есть соответствующие ф-и

# Дальше вычисляем ф-ю
Y = X**2 * np.exp( -(X**2) )
# Формулу применяем прямо над массивом целиком.
# Соответствующие циклы будут запрятаны внутрь бибилотеку numpy

# Посмотрим чему равен Y

print(Y)
# [0.0000000e+00 8.9999194e-06 3.5998706e-05 ... 1.1467591e-03 1.1285910e-03
#  1.1106882e-03]

# Видим, что сначала У растет, потом падает.
# Выведем еще одну ф-ю Z = sin(x) / e**x

Z = np.sin(X) / np.exp(X)

# Выводим Z
print(Z)  # [0.0000000e+00 8.9999194e-06 3.5998706e-05 ... 1.1467591e-03 1.1285910e-03 1.1106882e-03]

# Дальше попробуем ее нарисовать
# Простейший способ вывода графика
plt.plot( X, Y )  # первый - массив Х, второй - массив Y. Они должны быть одинаковыми.
# При необходимости, здесь можно указать, каким цветом нужно рисовать их линии.
# 'b-'  - 'b' - синяя, '-' - сплошная
# ф-я plot возвращает нам объект типа line2d

print(plt.plot(X, Z, 'r-'))  # используем красную сплошную линию
# [<matplotlib.lines.Line2D object at 0x0970F4C0>]  - тип

# Выводим на экран график
print(plt.show())  # получаем два графика на одних осях

# На вид график странный.
# Давайте посмотрим просто график sin(X)
S = np.sin(X)
plt.plot(X,S, 'g-')
plt.show()
# Здесь мы до числа pi не доехали. Синус меняет знак, когда х = pi. Тогда график норм.
# Вот так можно рисовать графики в простейшем случае.
# 1:22:58

