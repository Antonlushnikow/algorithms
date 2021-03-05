"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

SIZE = 50
MIN_ITEM = 0
MAX_ITEM = 1_000
my_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(*my_list, end='')

min1, min2 = (my_list[0], my_list[1]) if my_list[0] < my_list[1] else (my_list[1], my_list[0])

for num in my_list:
    if num < min1:
        min1, min2 = num, min1
    elif num < min2:
        min2 = num

print()
print(min1, min2)
