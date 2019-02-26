#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint
from math import inf

data = [randint(-99, 99) for i in range(20)]

max_elem = -inf
max_index = 0

for i in range(len(data)):
    elem = data[i]
    if max_elem < elem < 0:
        max_elem = elem
        max_index = i

print('исходные данные', data)
print('Максимально близкое к нулю', max_elem, 'индекс ', max_index)