# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трёх значное число: '))
d1 = a // 100
d23 = a % 100
d2 = d23 // 10
d3 = d23 % 10

sum_digits = d1 + d2 + d2
multy_digits = d1 * d2 * d3

print(sum_digits, multy_digits)
