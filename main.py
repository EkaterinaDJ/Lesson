# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = int(input("Введите сумму вклада:"))
# deposit = []
# deposit.append(money / 100 * 5.6)
# deposit.append(money / 100 * 5.9)
# deposit.append(money / 100 * 4.28)
# deposit.append(money / 100 * 4.0)
# print(deposit)
# print("Максимальная сумма, которую можно заработать:", max(deposit))


# if x > 0:
#     if y > 0:               # x > 0, y > 0
#          print("Первая четверть")
#     else:                   # x > 0, y < 0
#          print("Четвертая четверть")
# else:
#     if y > 0:               # x < 0, y > 0
#          print("Вторая четверть")
#     else:                   # x < 0, y < 0
#          print("Третья четверть")



# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)


# запишите цикл for для подсчета произведения
# for i in range(1, N+1):
#     P *= i
# print(P)

# def char_frequency():
#    text = """
#    У лукоморья дуб зелёный;
#    Златая цепь на дубе том:
#    И днём и ночью кот учёный
#    Всё ходит по цепи кругом;
#    Идёт направо -- песнь заводит,
#    Налево -- сказку говорит.
#    Там чудеса: там леший бродит,
#    Русалка на ветвях сидит;
#    Там на неведомых дорожках
#    Следы невиданных зверей;
#    Избушка там на курьих ножках
#    Стоит без окон, без дверей;
#    Там лес и дол видений полны;
#    Там о заре прихлынут волны
#    На брег песчаный и пустой,
#    И тридцать витязей прекрасных
#    Чредой из вод выходят ясных,
#    И с ними дядька их морской;
#    Там королевич мимоходом
#    Пленяет грозного царя;
#    Там в облаках перед народом
#    Через леса, через моря
#    Колдун несёт богатыря;
#    В темнице там царевна тужит,
#    А бурый волк ей верно служит;
#    Там ступа с Бабою Ягой
#    Идёт, бредёт сама собой,
#    Там царь Кащей над златом чахнет;
#    Там русский дух... там Русью пахнет!
#    И там я был, и мёд я пил;
#    У моря видел дуб зелёный;
#    Под ним сидел, и кот учёный
#    Свои мне сказки говорил.
#    """
#
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#     print(f"Символ {char} встречается {cnt} раз")


# def greet(name):
#     print('Привет,' + name + 'Доброе утро!')
# greet(' Джон. ')

# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#          return -num
# print(absolute_value(2))
# print(absolute_value(-4))

# def my_func():
#     x = 10
#     print('начение внутри функции', x)
# x = 20
# my_func()
# print('значение вне функции', x)

# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))
# hello_world_func()

# Синтаксис функции
# def имя функции (аргументы)
# инструкции
# return список выражений None
# Вызов функции () (через ее имя)

# def greet(name):
#     print('Привет ' + name + '. Доброе утро!')
# greet('Иван')


# Возвращаемое значение return
# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return  -num
# print(absolute_value(2))
# print(absolute_value(-4))

# Область видимости (scope) и время жизни переменной

# def my_func():
#     x = 10
#     print('Значение внутри функции', x )
# x = 20
# my_func()
# print('Значение вне функции', x)

# аргументы функции
# Фиксированное количество аргументов

# def greet(name, age):
#     print('Привет ' + name + '. Доброе утро! ' + 'Мне ' + age + ' лет')
# greet('Иван', '15')

# Аргументы по умолчанию

# def greet(name, age = '15'):
#     print('Привет ' + name + '. Доброе утро! ' + 'Мне ' + age + ' лет')
# greet('Иван')

# Именованный аргумент

# def greet(name, age):
#     print('Привет ' + name + '. Доброе утро! ' + 'Мне ' + age + ' лет')
# greet(name = 'Иван', age = '15')
# greet(age = '12', name = 'Катя', )

# Произвольныый список документов
# *

# def greet(*names):
#     for name in names:
#         print('Helllo', name)
# greet('Катя', 'John', 'Иван' )

# def adder(*nums):
#     sum = 0
#     for n in nums:
#         sum += n
#     print('sum =', sum)
# adder(3,5,6,7,8)

# Глобальные переменные

# x = 'Глобальная переменная'
# def foo():
#     print("x внутри функции", x)
# foo()
# print("x вне функции")

# локальные переменные

# def foo():
#     y = 'Локальная функция'
#     print(y)
# foo()

#  Глобальные и локальные переменные в одной программе

# x = ' global variable'
# def foo():
#     global x
#     y = 'local  variable'
#     x = x * 2
#     print(x)
#     print(y)
# foo()

 # Глобальные и локальные переменные с одинаковым именем
#
# x = 5
# def foo():
#     x = 10
#     print('local variable :', x)
# foo()
# print('global variable x:', x)

#  Нелокальные переменные nonlocal
#
# def outer():
#     x = 'локальная переменная'
#     print('Внешняя функция: ', x)
#     def inner():
#         nonlocal  x
#         x = 'нелокальная переменная'
#         print('Вложенная функция:', x)
#     inner()
# outer()

# Замыкания

# def say():
#     greeting = 'Привет'
#     def display():
#         print(greeting)
#     display()
# say()

# Вернуть функцию из функций

# Декораторы

# def net_price(price, tax):
#     return price * (1+tax)
#
# def currency(fn):
#     def wrapper(*args, **kwars):
#         result = fn(*args, **kwars)
#         return f'${result}'
#     return wrapper
# net_price = currency(net_price)
# print(net_price(100, 0.05))

# @currency
# def net_price(price, tax):
#     return price * (1+tax)

