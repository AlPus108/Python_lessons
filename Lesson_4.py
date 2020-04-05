import random

# 1. Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

lst_name = ['Marry', 'Alex', 'Kate', 'Jack', 'Anna', 'Ronald', 'Tatyana', 'Evgeniy', 'Maria', 'Svetlana', 'Artem', 'Igor', 'Ilya']
N = 100


def f(lst, n):
    rand_list = []                            # пустой список для вывода результата
    for i in range(n):                        # запускаем цикл на n итераций
        # rand_name = random.choice(lst)      # выбираем случайное имя из списка и присваиваем ее переменной
        # rand_list.append(rand_name)         # добавляем случайное имя в результирующий список
        rand_list.append(random.choice(lst))  # объединил две предыдущие строки в одну
    return rand_list                          # возвращаем список с количеством случайных имен n


fin_list = f(lst_name, N)                     # вызываем ф-ю с передачей в нее параметров
print(fin_list)                               # выводим результат


# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

# 1-й вариант решения
# Это говно-код, Но логика как на ладоне.

def pop_name(lst):
    # Первый этап - группируем имена в словаре: key - имя, value - количество повторений
    dic_name = {}                        # пустой словарь
    for i in range(len(lst)):            # внешний цикл
        s = 0                            # счетчик обнуляем с каждой итерацией внешнего цикла
        name = lst[i]                    # присваиваем переменной name текущее занчение i (имя)
        for j in range(len(lst)):        # внутренний цикл
             if lst[j] == lst[i]:        # если текущее значение внутр.цикла совпадает с тек.значением внешнего цикла
                s += 1                   # увеличиваем счетчик на 1
        dic_name[name] = s               # заполняем словарь с каждой итерацией внешнего цикла
    # Второй этап - ищем в словаре имя (key) с самым большим количество повторений (value)
    pop_k = ''
    pop_v = 0
    for key, value in dic_name.items():  # листаем полученный словарь
        if value > pop_v:                # если значение в словаре больше значения в переменной pop_v
            pop_k = key                  # меняем значение переменной
            pop_v = value                # меняем значение переменной
    return print(f'Имя {pop_k} встречается в строке {pop_v} раз')


pop_name(fin_list)  # вызываем ф-ю

# 2-й вариант решения через функции (просто мистика)

# Решение с помощью функции
def max_word(lst):
    # Получаем уникальные значения списка через обертку set
    # Через обертку Словарь листаем в цикле список и считаем количество повторений каждого уникального слова (set)
    pop_name = dict((fin_list.count(i), i) for i in set(fin_list))
    return pop_name[max(pop_name.keys())]  # Выводим слово с наибольшим количество повторений (max)

print(f'Имя {max_word(fin_list)} встречается в строке {fin_list.count(max_word(fin_list))} раз.')

# 3. Напишите функцию вывода самой редкой буквы, с которой начинаются имена в списке на выходе функции F.

def rare_letter(lst):
    let_lst = list(map(lambda string: string[0], lst))  # получаем список всех заглавных букв списка имен.
    rar_let = ''
    rar_let_fin= ''
    n = len(let_lst)
    for i in range(len(let_lst)):                       # внешний цикл
        s = 0                                           # обнуляем переменную
        for j in range(len(let_lst)):                   # внутренний цикл
            if let_lst[i] == let_lst[j]:                # ищем совпадения по значению
                rar_let = let_lst[i]                    # присваиваем текущее значение переменной
                s += 1                                  # увеличиваем переменную на 1
        if s < n:                                       # сравниваем переменные, если значение текущей переменной меньше,
            n = s                                       # прибавляем к результирующей переменной
            rar_let_fin = rar_let                       # запоминаем значение с наименьшим количеством повторений
    return print(f'Заглавная буква {rar_let_fin} встречается в строке {n} раз')


rare_letter(fin_list)
