"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите количество элементов последовательности: '))


def sum_for(n):
    order = 1
    result = 1
    i = 0
    elem_list = '1'
    while i < n:
        order = order / -2
        result += order
        i += 1
        elem_list += ' ' + str(order)

    print('[', elem_list, ']', 'Сумма =', result)


sum_for(n)
