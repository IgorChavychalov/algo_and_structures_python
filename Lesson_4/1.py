"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

from timeit import timeit
from cProfile import run


def sum_for(n: int):
    """
    2.4. Найходит сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    n - количество элементов
    """
    order = 1
    result = 1
    i = 0
    elem_list = '1'
    while i < n:
        order = order / -2
        result += order
        i += 1
        elem_list += ' ' + str(order)

    return elem_list, result


def sum_rec(i, num, n, summ):
    if i == n:
        return summ
    elif i < n:
        return sum_rec(i + 1, num / (-2), n, summ + num)

i = 0
num = 1
summ = 0

n = 10

# timeit('sum_for(n)', - изучаемая функция с переменной. Переменную необходимо определить в сомом модуле с кодом
#        setup="from __main__ import sum_for, n", - импорт функции и переменной
#        number=100 - количество замеров. 100 что-бы избежать экспоненцального формата числа)

#  1. Сравнение скорости
time_for = timeit('sum_for(n)',
                  setup='from __main__ import sum_for, n',
                  number=100)
time_rec = timeit('sum_rec(i, num, n, summ)',
                  setup='from __main__ import sum_rec, i, num, n, summ',
                  number=100)

time_difference = int(1 - (time_rec / time_for) * 100)

print('-' * 15, 'Сравнение скорости', '-' * 15)
print('Через цикл for: ', time_for, '100 %')
print('Через рекурсию: ', time_rec, time_difference, "%")

#  2. Сравнение сложности
print('-' * 15, 'Сравнение сложности', '-' * 15)


def main():
    n = 10
    result_for = sum_for(n)

    i = 0
    num = 1
    summ = 0
    result_rec = sum_rec(i, num, n, summ)


run('main()')
print('Всё по нулям')

