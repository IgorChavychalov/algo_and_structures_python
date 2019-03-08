"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

# условный ввод
factory = ['кондитерская', 'хлебопекарня', 'шиномонтаж']
profit_1 = [10, 9, 11, 13]
profit_2 = [9, 8, 5, 13]
profit_3 = [11, 13, 14, 16]

profit = list((profit_1, profit_2, profit_3))
base = collections.Counter()
average_annual_profit = collections.Counter()

# формируем базу
for i in range(len(factory)):
    base[factory[i]] = profit[i]

print(base)


def mean(nums):
    """ возвращает среднее значение """
    return sum(nums, 0.0) / len(nums)


# определяем среднюю годовую прибыль каждого предприятия
for elm in factory:
     average_annual_profit[elm] = mean(base[elm])

print(average_annual_profit)

# предприятия с прибылью выше среднего.
max_profit = max(average_annual_profit, key=lambda k: average_annual_profit[k])

# предприятия с наименьшей прибылью.
min_profit = min(average_annual_profit, key=lambda k: average_annual_profit[k])

# вывод
print(f'наибольшая прибыль у {max_profit} = {average_annual_profit[max_profit]},'
      f' наименьшая прибыль у {min_profit} = {average_annual_profit[min_profit]}')
