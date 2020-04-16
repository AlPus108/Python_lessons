# ----------------- Конвертация Словаря в объект Shelve -------------------------

# Это сделать очень легко, так как обекты Shelve схожи со Словарями,
# но, есть некоторые моменты, на которые надо обращать внимание.

# Создадим словарь, в котором будет две пары ключ-значение
university = {
    # в значении находится еще один словарь
    'schedule': {
        'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
        'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
        'wednesday_schedule': ['Physics', 'English language', 'Python'],
        'thursday_schedule': ['Math', 'Chemistry', 'Java'],
        'friday_schedule': ['Running', 'Math', 'Python']
    },

    'tutors': {
        'Math': ['Jack White', 'Jim Black'],
        'Python': ['James Miller', 'Barbara Kusine']
    }
}

# Распечатаем из этого словаря, чтобы понять, что у нас все работает корректно.
# Выведем расписание унирвеситета на среду
print(university['schedule']['wednesday_schedule'])
# И список преподавателей по математике
print(university['tutors']['Math'])
# ['Physics', 'English language', 'Python']
# ['Jack White', 'Jim Black']

# Теперь попробуем все это сконвертировать в объект shelve
# Сначала импортируем модуль

import shelve

university = shelve.open('university_file')

university['schedule'] = {
        'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
        'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
        'wednesday_schedule': ['Physics', 'English language', 'Python'],
        'thursday_schedule': ['Math', 'Chemistry', 'Java'],
        'friday_schedule': ['Running', 'Math', 'Python']
    }  # <-- сейчас конечно уже убрали, но до этого не убрали запятую между массивами данных,
       # из-за этого получили ошибку


university['tutors'] = {
        'Math': ['Jack White', 'Jim Black'],
        'Python': ['James Miller', 'Barbara Kusine']
    }

print(university['schedule']['wednesday_schedule'])
print(university['tutors']['Math'])

# И в конце закрываем
university.close()

# При запуске получаем ошибку:
# print(university['schedule']['wednesday_schedule'])
# TypeError: tuple indices must be integers or slices, not str

# Это один из тех моментов, которые надо учитывать при конвертации
# Между university['schedule'] и ['wednesday_schedule'] мы не убрали запятую,
# из-за этого получаем объект типа tuple вместо dict
# Все запятые надо убирать!

# Теперть, после исправления ошибки, при выводе получаем информацию из объкта shelve
# ['Physics', 'English language', 'Python']
# ['Jack White', 'Jim Black']
