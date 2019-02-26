# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

data = [i for i in range(2, 99)]
check = [i for i in range(2, 9)]

num = 0
result = []

for i in check:
    for j in data:
        if j % i == 0:
            num += 1
    result.append([i, num])
    num = 0

for i in range(len(result)):
    print(f'{result[i][1]} чисел кратных {result[i][0]}')
