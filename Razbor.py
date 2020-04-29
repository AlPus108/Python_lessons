import pymorphy2

# В файле содержится текст. Считать/скопировать текст из файла и выполнить следующую последовательность действий:

# LIGHT:
#
# 1) методами строк очистить текст от знаков препинания;
# 2) сформировать list со словами (split);
# 3) привести все слова к нижнему регистру (map);
# 4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
# 5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
#
# PRO:
#
# 6) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.

result = {}
morph = pymorphy2.MorphAnalyzer()
with open(file='text.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        for word in line.split():
            word = word.lower()
            if word == '—':
                continue
            word = ''.join(char for char in word if char.isalpha())
            p = morph.parse(word)[0]
            if word in result:
                result[word]['count'] += 1
            else:
                result[word] = {'count': 1, 'normal_form': p.normal_form}
tuple_res = list(result.items())
tuple_res.sort(key=lambda x: x[1]['count'], reverse=True)
for i in range(5):
    print(tuple_res[i])
print(len(result))

# ('be', {'count': 47, 'normal_form': 'be'})
# ('let', {'count': 41, 'normal_form': 'let'})
# ('it', {'count': 41, 'normal_form': 'it'})
# ('of', {'count': 11, 'normal_form': 'of'})
# ('words', {'count': 7, 'normal_form': 'words'})
# 62


# ---------------------------------------------------------------------

morph = pymorphy2.MorphAnalyzer()
# Читаем из файла
f = open('text.txt',encoding='utf-8')
text=f.read()
# Заменяем знаки препинания на ПРОБЕЛ
str=text
symbol_list=[' ','.',',','?','!','-','–','—',"'",'"','«','»',':',';','(',')','\n'] # Список знаков препинания
for a in range(len(symbol_list)):
    str=str.replace(symbol_list[a],' ')
print('Заменяем знаки препинания на ПРОБЕЛ')
print(str)
# Создаём List
text_list=str.split()
print('Создаём List')
print(text_list)
# Приводим к нижнему регистру
text_list=list(map(lambda x: x.lower(),text_list))
print('Приводим к нижнему регистру')
print(text_list)
# Получаем нормальную форму
text_list=list(map(lambda x: morph.parse(x)[0].normal_form,text_list))
print('Получаем нормальную форму')
print(text_list)
# Создание словаря СЛОВО:ВСТРЕЧАЕТСЯ
text_dict={a:text_list.count(a) for a in text_list}
print('Создание словаря СЛОВО:ВСТРЕЧАЕТСЯ')
print(text_dict)
# 5 наиболее встречающихся
sort_list=list(text_dict.items())
sort_list.sort(key=lambda i: i[1],reverse=True)
print('5 наиболее встречающихся')
print(sort_list[:5])
# Количество разных слов в тексте
text_set=set(text_list)
print('Количество разных слов в тексте')
print(len(text_set))