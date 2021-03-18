"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

import random

SIZE = 10
MIN_NUM = -100
MAX_NUM = 100

array = [random.randint(MIN_NUM, MAX_NUM - 1) for _ in range(SIZE)]
print(array)


def bubble_sort(data):
    data = data.copy()
    count = len(data) - 1
    while count > 0:
        for i in range(count):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        count -= 1

    return data


print(bubble_sort(array))
