"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random


def bubble_sort(n: list):
    is_sotred = 1
    for i in range(len(n)):
        for j in range(len(n)-1):
            if n[j] < n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                is_sotred = 0
        if is_sotred == 1:
            print('не сортировался')
            return n
    return n


test = [random.randint(-100, 100) for _ in range(10)]
test2 = [i for i in range(-10, 0)]

# 1 сортировка по убыванию
print(bubble_sort(test))

# 2 сортировка по убыванию сортированного списка
print(bubble_sort(test2[::-1]))
