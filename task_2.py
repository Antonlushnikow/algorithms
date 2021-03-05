"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1_000
my_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(*my_list, end='')

even_list = []

for i, num in enumerate(my_list):
    if not num % 2:
        even_list.append(i)

print()
print(*even_list, end='')
