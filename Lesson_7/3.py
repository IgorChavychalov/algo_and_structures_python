"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random


def quickselect_median(arr, pivot_fn=random.choice):
    # ищем середину массива
    if len(arr) % 2 == 1:
        # если длинна не чётная, то индекс округляем в большую сторону
        return quickselect(arr, len(arr) / 2, pivot_fn)
    else:
        # берём половину суммы пловины????
        return 0.5 * (quickselect(arr, len(arr) / 2 - 1, pivot_fn) +
                      quickselect(arr, len(arr) / 2, pivot_fn))


def quickselect(arr, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param l: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(arr) == 1:
        # если в массиве один элемент, то его и возвращаем
        # assert k == 0
        return arr[0]

    # выбираем случайное значение из массива для опорного элемента
    pivot = pivot_fn(arr)

    # сравниваем все значения с опорным элеменот и формируем 3 списка больше, меньше равные опорнуму элемнту
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    # если искомый индекс меньше чем количество элементов в списке (т.е. индекс последнего элемента + 1) со значениями
    # меньше опорного элемента, то медианый элемент нахожится в нём.
    if k < len(lows):
        # Вызываем реккурсию и делим этот список ещё на 3 списка пока не выполнеца условие len(l) == 1 или условие elif.
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        # тоже не понятно ???
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

m = 3

arr = [random.randint(0, 100) for _ in range(2 * m + 1)]

result = quickselect_median(arr)

print(arr)
print(result)

