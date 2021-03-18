"""Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы. """

import random

m = 10
MIN_NUM = 1
MAX_NUM = 100

array = [random.randint(MIN_NUM, MAX_NUM - 1) for _ in range(2 * m + 1)]
print(array)


def seek_med(data):
    for num1 in set(data):
        left, right, count = 0, 0, 0
        for num2 in data:
            if num1 < num2:
                right += 1
            elif num1 > num2:
                left += 1
            else:
                count += 1
        if abs(right - left) < count:
            return num1


print(seek_med(array))
# array.sort()
# print(array[len(array) // 2])
