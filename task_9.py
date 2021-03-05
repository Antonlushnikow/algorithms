"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

SIZE_N = 5
SIZE_M = 6
MIN_ITEM = 0
MAX_ITEM = 1_000
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]

col_min = matrix[0]
max_min = matrix[0][0]  # это не нужно, но иначе pycharm ругается, что переменная может быть не определена

for i, line in enumerate(matrix):
    for j, num in enumerate(line):
        print(f'{num:>7}', end='')
        if num < col_min[j]:
            col_min[j] = num
        if i == len(matrix) - 1:
            if j == 0:
                max_min = col_min[0]
            else:
                if col_min[j] > max_min:
                    max_min = col_min[j]
    print()

print()
for num in col_min:
    print(f'{num:>7}', end='')

print('\n')
print(f'Максимальный элемент - {max_min}')
