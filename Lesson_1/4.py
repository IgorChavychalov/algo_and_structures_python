"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random

x = input('Укажите нижнюю границу: ')
y = input('Укажите верхнюю границу: ')

try:
    # пробуем целый числа
    xx = float(x)
    yy = float(y)
    result = random.uniform(xx, yy)
    if round(xx, 0) == xx and round(yy, 0) == yy:
        result = int(result)
    else:
        # определяем количество знаков после запятой
        if x.find('.') > 0:  # проверка на наличие точки
            split_x = x.split('.')
            len_x = len(split_x[1])
        else:
            len_x = 1

        if y.find('.') > 0:  # проверка на наличие точки
            split_y = y.split('.')
            len_y = len(split_y[1])
        else:
            len_y = 1

        # выбираем максимально длинную дробную часть
        if len_x >= len_x:
            len_max = len_x
        else:
            len_max = len_y

        result = round(result, len_max)

    print('целые', result)


except Exception:
    try:
        # пробуем текст
        xx = ord(x)
        yy = ord(y)
        print(xx, yy)

        result = random.randint(xx, yy)

        result = chr(result)

        print(result)

    except Exception:
        print('Не корректный ввод')
