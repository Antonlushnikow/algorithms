"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

SIZE = 10
MIN_NUM = 0
MAX_NUM = 50

array = [random.randint(MIN_NUM, MAX_NUM - 1) for _ in range(SIZE)]
print(array)


def merge_sort(data):
    if len(data) == 1:
        return data
    else:
        arr1 = merge_sort(data[0:len(data) // 2])
        arr2 = merge_sort(data[len(data) // 2:len(data)])

    res = []
    while len(arr1) and len(arr2):
        spam = arr1.pop(0) if arr1[0] < arr2[0] else arr2.pop(0)
        res.append(spam)
    res.extend(arr1)
    res.extend(arr2)
    return res


print(merge_sort(array))
