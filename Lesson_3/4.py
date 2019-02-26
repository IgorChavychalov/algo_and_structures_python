# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint

data = [randint(0, 99) for i in range(20)]

max_volume = 1
max_index = 0

for i in range(len(data)):
    j = data.count(data[i])
    if j > max_volume:
        max_volume = j
        max_index = i

result = data[max_index]

print('исходные данные', data)
print('чаще всего встречаеться число ', result, '-', max_volume, 'раз(а)')
