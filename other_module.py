from module import CAT, DOG as _DOG, _FISH
# Можно импортировать изменяемую переменную DOG и при импорте сделать ее не изменяемой _DOG
# То есть, повышаем уровень доступа.
# Точно также при импорте можно уровень доступа снижать.
# Это все на усмотрение разработчиков. Но, об этой договоренности нужно знать и помнить.

# Есть договоренность на уровне разработчиков, что константные переменные пишутся большими буквами
APPLE = 'apple'
CHEEZ = 'cheez'

# Системные константы пишутся с нижним подчеркиванием "земля"
_CARROT = 'carrot'

__all__ = ('APPLE', '_CARROT')  # Список переменных, доступных для публичного пользования
print(_DOG)