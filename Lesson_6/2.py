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
import random
import collections

@profile
def profit_calculation(factory, profit_1, profit_2, profit_3):
    """
    1. Пользователь вводит данные о количестве предприятий, их наименования и
    прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
    Программа должна определить среднюю прибыль (за год для всех предприятий) и
    вывести наименования предприятий, чья прибыль выше среднего и отдельно
    вывести наименования предприятий, чья прибыль ниже среднего.
    """
    profit = list((profit_1, profit_2, profit_3))
    base = collections.Counter()
    average_annual_profit = collections.Counter()

    # формируем базу
    for i in range(len(factory)):
        base[factory[i]] = profit[i]

    def mean(nums):
        """ возвращает среднее значение """
        return sum(nums, 0.0) / len(nums)

    # определяем среднюю годовую прибыль каждого предприятия
    for elm in factory:
         average_annual_profit[elm] = mean(base[elm])

    # предприятия с прибылью выше среднего.
    max_profit = max(average_annual_profit, key=lambda k: average_annual_profit[k])

    # предприятия с наименьшей прибылью.
    min_profit = min(average_annual_profit, key=lambda k: average_annual_profit[k])

    # вывод
    # print(f'наибольшая прибыль у {max_profit} = {average_annual_profit[max_profit]},'
    #       f' наименьшая прибыль у {min_profit} = {average_annual_profit[min_profit]}')
    return average_annual_profit[max_profit], average_annual_profit[min_profit]


if __name__ == '__main__':
    factory = ['кондитерская', 'хлебопекарня', 'шиномонтаж']

    profit_1 = [random.randint(0, 100) for _ in range(10000)]
    profit_2 = [random.randint(0, 100) for _ in range(10000)]
    profit_3 = [random.randint(0, 100) for _ in range(10000)]

    profit_calculation(factory, profit_1, profit_2, profit_3)



'''
win = 10 x64
Python = 3.6

    profit_1 = [random.randint(0, 100) for _ in range(10000000)]
    profit_2 = [random.randint(0, 100) for _ in range(10000000)]
    profit_3 = [random.randint(0, 100) for _ in range(10000000)]


Line #    Mem usage    Increment   Line Contents
================================================
    45    268.5 MiB    268.5 MiB   @profile
    46                             def profit_calculation(factory, profit_1, profit_2, profit_3):
    47                                 """
    48                                 1. Пользователь вводит данные о количестве предприятий, их наименования и
    49                                 прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
    50                                 Программа должна определить среднюю прибыль (за год для всех предприятий) и
    51                                 вывести наименования предприятий, чья прибыль выше среднего и отдельно
    52                                 вывести наименования предприятий, чья прибыль ниже среднего.
    53                                 """
    54    268.5 MiB      0.0 MiB       profit = list((profit_1, profit_2, profit_3))
    55    268.5 MiB      0.0 MiB       base = collections.Counter()
    56    268.5 MiB      0.0 MiB       average_annual_profit = collections.Counter()
    57                             
    58                                 # формируем базу
    59    268.5 MiB      0.0 MiB       for i in range(len(factory)):
    60    268.5 MiB      0.0 MiB           base[factory[i]] = profit[i]
    61                             
    62    268.5 MiB      0.0 MiB       def mean(nums):
    63                                     """ возвращает среднее значение """
    64    268.5 MiB      0.0 MiB           return sum(nums, 0.0) / len(nums)
    65                             
    66                                 # определяем среднюю годовую прибыль каждого предприятия
    67    268.5 MiB      0.0 MiB       for elm in factory:
    68    268.5 MiB      0.0 MiB            average_annual_profit[elm] = mean(base[elm])
    69                             
    70                                 # предприятия с прибылью выше среднего.
    71    268.5 MiB      0.0 MiB       max_profit = max(average_annual_profit, key=lambda k: average_annual_profit[k])
    72                             
    73                                 # предприятия с наименьшей прибылью.
    74    268.5 MiB      0.0 MiB       min_profit = min(average_annual_profit, key=lambda k: average_annual_profit[k])
    75                             
    76                                 # вывод
    77                                 # print(f'наибольшая прибыль у {max_profit} = {average_annual_profit[max_profit]},'
    78                                 #       f' наименьшая прибыль у {min_profit} = {average_annual_profit[min_profit]}')
    79    268.5 MiB      0.0 MiB       return average_annual_profit[max_profit], average_annual_profit[min_profit]


    profit_1 = [random.randint(0, 100) for _ in range(10000)]
    profit_2 = [random.randint(0, 100) for _ in range(10000)]
    profit_3 = [random.randint(0, 100) for _ in range(10000)]


Line #    Mem usage    Increment   Line Contents
================================================
    16     38.9 MiB     38.9 MiB   @profile
    17                             def profit_calculation(factory, profit_1, profit_2, profit_3):
    18                                 """
    19                                 1. Пользователь вводит данные о количестве предприятий, их наименования и
    20                                 прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
    21                                 Программа должна определить среднюю прибыль (за год для всех предприятий) и
    22                                 вывести наименования предприятий, чья прибыль выше среднего и отдельно
    23                                 вывести наименования предприятий, чья прибыль ниже среднего.
    24                                 """
    25     38.9 MiB      0.0 MiB       profit = list((profit_1, profit_2, profit_3))
    26     38.9 MiB      0.0 MiB       base = collections.Counter()
    27     38.9 MiB      0.0 MiB       average_annual_profit = collections.Counter()
    28                             
    29                                 # формируем базу
    30     38.9 MiB      0.0 MiB       for i in range(len(factory)):
    31     38.9 MiB      0.0 MiB           base[factory[i]] = profit[i]
    32                             
    33     38.9 MiB      0.0 MiB       def mean(nums):
    34                                     """ возвращает среднее значение """
    35     38.9 MiB      0.0 MiB           return sum(nums, 0.0) / len(nums)
    36                             
    37                                 # определяем среднюю годовую прибыль каждого предприятия
    38     38.9 MiB      0.0 MiB       for elm in factory:
    39     38.9 MiB      0.0 MiB            average_annual_profit[elm] = mean(base[elm])
    40                             
    41                                 # предприятия с прибылью выше среднего.
    42     38.9 MiB      0.0 MiB       max_profit = max(average_annual_profit, key=lambda k: average_annual_profit[k])
    43                             
    44                                 # предприятия с наименьшей прибылью.
    45     38.9 MiB      0.0 MiB       min_profit = min(average_annual_profit, key=lambda k: average_annual_profit[k])
    46                             
    47                                 # вывод
    48                                 # print(f'наибольшая прибыль у {max_profit} = {average_annual_profit[max_profit]},'
    49                                 #       f' наименьшая прибыль у {min_profit} = {average_annual_profit[min_profit]}')
    50     38.9 MiB      0.0 MiB       return average_annual_profit[max_profit], average_annual_profit[min_profit]


Вывод: 
Вся помять расходуется сразу и не прирастает в процессе нахождение среднего значения.
Это связанно с тем что основной потребитель памяти является коллекции, а для нахождения среднего значения необходимо одна 
дополнительная переменная и циклический проход по коллекциям что не способствует серьёзному увеличению расхода памяти. 
'''
