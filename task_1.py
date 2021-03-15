"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Определить, какое число в массиве встречается чаще всего.
"""

import random
import sys

SIZE = 1000
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE)]
print(array)
print('*' * 50)


def show(*args):
    size_ = 0
    for arg in args:
        if hasattr(arg, '__iter__'):
            size_ += show(*arg)
        else:
            size_ += sys.getsizeof(arg)
    return size_


# Вариант 1. Со словарем
d = {}
freq_num = array[0]
for num1 in array:
    if num1 in d:
        d[num1] += 1
    else:
        d[num1] = 1
count1 = 1
for key in d:
    if d[key] > count1:
        count1 = d[key]
        freq_num = key

print(show(d, freq_num, num1, count1, key))  # 17808 байт
print('*' * 50)


# Вариант 2. С вложенными циклами и множеством
set_array = set(array)
num2 = array[0]
frequency = 1
for item in set_array:
    spam = 1
    for j in range(len(array)):
        if item == array[j]:
            spam += 1
    if spam > frequency:
        frequency = spam
        num2 = item

print(show(set_array, num2, frequency, spam, j, item))  # 17836 байт
print('*' * 50)


# Вариант 3. С сортировкой и без множества
array.sort()
count3 = 1
res = array[0]
last = len(array) - 1
k = 0
while k < last:
    eggs = 1
    while k < last and array[k] == array[k + 1]:
        eggs += 1
        k += 1
    if eggs > count3:
        count3 = eggs
        res = array[k]
    k += 1

print(show(count3, res, last, k, eggs))  # 140 байт

# Python 3.9.2, 64 bit
# Сложность первого алгоритма - O(n), третьего - O(n * logn),
# при этом третий занимает в разы меньше памяти (140 против 17808 байт).
# Второй алгоритм выполняется за O(n ** 2) и использует примерно такой же объем памяти,
# как и вариант со словарем (17836 байт).
