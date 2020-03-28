
s = open("C:/Users/Lenovo 330s/Documents/UII/text.txt",  encoding='utf-8')
str = s.read()
s.close()


# 1) методами строк очистить текст от знаков препинания;

# Вариант 1
symbols = '.,!?:—(«'
str_2 = str
for sym in symbols:
    if sym in str:
        str_2 = str_2.replace(sym, '')
print('Вывод текста без знаков препинания (Вар 1)\n', str_2)

# Вариант 2
str_3 = str.translate({ord(x): '' for x in symbols})
print('Вывод текста без знаков препинания (Вар 2)\n', str_3)


# 2) сформировать list со словами (split);

str_3 = str_3.split()
print('Вывод текста тип list\n', str_3)


# 3.1) привести все слова к нижнему регистру (map);

str_4 = list(map(lambda x: x.lower(), str_3))
print('Вывод текста в нижнем регистре (map)\n', str_4)

# # Без map
# str_5 = str.lower()
# print('Вывод текста в нижнем регистре (без map)\n', str_5)


# 3.2) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;


dict_str = {}            # Пустой Словарь
for i in str_4:          # Внешний цикл
    x = 0                # Счетчик. При каждом выходе из внутреннего цикла, обнуляется. Формирует значения для Словаря
    for j in str_4:      # Внутренний цикл
        if i == j:       # Если найдено совпадение
            x += 1       # Увеличиваем счетчик на 1
    dict_str[i] = x      # Вносим данные в Словарь: i - ключи, x - значения
print(dict_str.items())  # Выводим словарь


# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

# Отсортировать Словарь на прямую вроде как нельзя, поэтому
list_dict = list(dict_str.items())  # Получаем из словаря список кортежей: ключ - значение
# print(list_dict)
list_dict.sort(key=lambda i: i[1])  # делаем сортировку по значениям
list_dict.reverse()  # разворачиваем список
# print(list_dict)
for i in list_dict[:5]:  # в цикле выводим первые пять наиболее часто встречающихся слов
    print(i[0], ':', [i[1]])

# выводим количество разных слов в списке через Set

set_from_list_dict = (list_dict)
print(set_from_list_dict)