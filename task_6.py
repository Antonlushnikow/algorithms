"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
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
    elif num < my_list[idx_min]:
        idx_min = i

print()
print(f'Минимум - {my_list[idx_min]} (элемент {idx_min})\nМаксимум - {my_list[idx_max]} (элемент {idx_max})')

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

my_sum = 0
for i in range(idx_min + 1, idx_max):
    my_sum += my_list[i]

print(f'Сумма между минимумом и максимумом - {my_sum}')
