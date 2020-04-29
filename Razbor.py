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