"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 30
my_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(*my_list, end='')

idx_min, idx_max = (0, 1) if my_list[0] < my_list[1] else (1, 0)

for i, num in enumerate(my_list):
    if num > my_list[idx_max]:
        idx_max = i
    if num < my_list[idx_min]:
        idx_min = i

my_list[idx_min], my_list[idx_max] = my_list[idx_max], my_list[idx_min]

print()
print(*my_list, end='')
