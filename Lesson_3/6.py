"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

data = [randint(0, 99) for i in range(20)]

max_elem = max(data)
min_elem = min(data)

max_index = data.index(max_elem)
min_index = data.index(min_elem)

if min_index > max_index:
    min_index, max_index = max_index, min_index

summ = 0

print(data)

for i in data[(min_index + 1): (max_index)]:
    summ += i
    print(i, end=' ')

print()
print('min =', min_elem, 'max=', max_elem)
print('summ=', summ)
