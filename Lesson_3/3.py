#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

data = [randint(0, 99) for i in range(10)]

print('исходный данные',data)

min_value = min(data)
max_value = max(data)

print('максимальное', max_value, ', минимальное', min_value)
for i in range(len(data)):
    if data[i] == max_value:
        max_index = i
    elif data[i] == min_value:
        min_index = i

data[max_index] = min_value
data[min_index] = max_value

print('с заменой', data)
