# До этого мы рассматривали сериализацию объекта при помощи модуля pickle.
# Это не плохая опция языка Пайтон. Но, у него есть один недостаток. Дело в том, что при его работа все объекты
# помещаются в память компьютера, и, когда объектов очень много или объект очень большой, то эта опция не очень выгодна.
# Но, в Пайтоне есть альтернатива. Для этого используется модуль shelve.
# Он реализует хранение данных на подобие словаря при помощи пар ключ-значение. Но, в отличии от словаря,
# данные он хранит не в памяти, а в файле. В файловой системе.
# Ключи должны быть обязательно строками, в отличии от словарей, где ключами могут быть любые имьютбл-объекты.
# Практически все методы, которые используются для словарей, могут быть использованы и для объектов shelve.
# Их можно представлять, как сохраненный в файле словарь. Поэтому очень легко конвертировать код,
# который используют словари, в объекты shelve.
# Значения пиклируются, маринуются, когда сохраняются. То есть, используется модуль pickle.

# Рассмотрим на практике, как пользоваться модулем shelve
# В первую очередь его надо импортировать.
import shelve

with shelve.open('shelve_test') as cars:  # даем название файлу и переменной, в которой будет храниться ключ-значение
    # Размещаем ключи со значениями
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'
    cars['honda'] = 'Japan'


    print(cars['ford'])  # USA
    print(cars['renault'])  # France


# Теперь попробум вывести инфу из словаря за пределами блока with
# print(cars['mazda'])  # Получаем ошибку
# ValueError: invalid operation on closed shelf
# Так как лишь внутри блока with мы можем указывать обращение к объекту shelve - cars
# Вне блока мы не можем уже этого сделать, так как он уже закрыт.
# Он автоматически закрывается после того, как мы выходим из него, то есть не соблюдаем отступ.

# Видно, что обращения к значениям shelve идентичны обращениям к словарю.
# Единственная разница в том, что создается отельный файл shelve_test.dir.
# Он не может быть открыт в текстовом формате, так как это база данных.
# Именно в этом файле создается данный объект shelve с парами ключ-значение,
# тогда как словари хранят свои данные в памяти компьютера.
# Именно из этого файла мы извлекаем информацию

# Так как мы записываем информацию в файл, здесь возможен подводный камень.
# Если вы случайно обратитесь к ключу с ошибкой,
#     print(cars['hond'])
# Мы все равно получим значение по этому ошибочному обращению так как часть его там присутствует.
# Ключ можно удалить из БД.
# Для этого БД надо проитерировать как обычный словарь в цикле
# При этом надо сохранять отступ, чтобы он оставался в пределах конструкции with
    for key in cars:
        print(key)
    # Вывод:
    # opel
    # ford
    # mazda
    # renault
    # hond
    # honda
    # Видим, что там содержится и неправильный ключ.
    # Чтобы его удалить, надо применить ф-ю del
    # del cars['hond']
    # Снова запустим цикл
    for key in cars:
        print(key)
    # opel
    # ford
    # mazda
    # renault
    # honda
# Если еще раз запусим этот код, то получим ошибку KeyError: b'hond'
# так в базе уже нет записи по такому ключу.



