"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile
import sys


# 1
@profile
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

    print('количество ссылок = ', sys.getrefcount(elem_list), 'количество ссылок = ', sys.getrefcount(result))
    return elem_list, result


if __name__ == '__main__':
    n = 100

    sum_for(n)

'''
n = 100
win = 10 x64
Python = 3.6

Line #    Mem usage    Increment   Line Contents
================================================
    16     38.6 MiB     38.6 MiB   @profile
    17                             def sum_for(n: int):
    18                                 """
    19                                 2.4. Найходит сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    20                                 n - количество элементов
    21                                 """
    22     38.6 MiB      0.0 MiB       order = 1
    23     38.6 MiB      0.0 MiB       result = 1
    24     38.6 MiB      0.0 MiB       i = 0
    25     38.6 MiB      0.0 MiB       elem_list = '1'
    26     38.6 MiB      0.0 MiB       while i < n:
    27     38.6 MiB      0.0 MiB           order = order / -2
    28     38.6 MiB      0.0 MiB           result += order
    29     38.6 MiB      0.0 MiB           i += 1
    30     38.6 MiB      0.0 MiB           elem_list += ' ' + str(order)
    31                             
    32     38.6 MiB      0.0 MiB       print('количество ссылок = ', sys.getrefcount(elem_list), 'количество ссылок = ', sys.getrefcount(result))
    33     38.6 MiB      0.0 MiB       return elem_list, result


[Finished in 1.2s]


n = 100000

Line #    Mem usage    Increment   Line Contents
================================================
    14     38.7 MiB     38.7 MiB   @profile
    15                             def sum_for(n: int):
    16                                 """
    17                                 2.4. Найходит сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    18                                 n - количество элементов
    19                                 """
    20     38.7 MiB      0.0 MiB       order = 1
    21     38.7 MiB      0.0 MiB       result = 1
    22     38.7 MiB      0.0 MiB       i = 0
    23     38.7 MiB      0.0 MiB       elem_list = '1'
    24     40.5 MiB      0.0 MiB       while i < n:
    25     40.5 MiB      0.0 MiB           order = order / -2
    26     40.5 MiB      0.0 MiB           result += order
    27     40.5 MiB      0.0 MiB           i += 1
    28     40.5 MiB      0.4 MiB           elem_list += ' ' + str(order)
    29                             
    30     40.5 MiB      0.0 MiB       return elem_list, result

Вывод: появившийся расход памяти связан с разрастанием списка  elem_list до "заметных" размеров.
'''