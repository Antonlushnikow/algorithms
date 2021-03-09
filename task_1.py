"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.

Определить, какое число в массиве встречается чаще всего.
"""


import random
import timeit
import cProfile

SIZE_10 = 10
SIZE_20 = 20
SIZE_30 = 30
SIZE_40 = 40
SIZE_50 = 50
SIZE_60 = 60
SIZE_70 = 70
SIZE_80 = 80
SIZE_90 = 90
SIZE_100 = 100
SIZE_200 = 200
SIZE_300 = 300
SIZE_400 = 400
SIZE_10000 = 10000
MIN_ITEM = 0
my_array_10 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_10)]
my_array_20 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_20)]
my_array_30 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_30)]
my_array_40 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_40)]
my_array_50 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_50)]
my_array_60 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_60)]
my_array_70 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_70)]
my_array_80 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_80)]
my_array_90 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_90)]
my_array_100 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_100)]
my_array_200 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_200)]
my_array_300 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_300)]
my_array_400 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_400)]
my_array_10000 = [random.randint(MIN_ITEM, 1000) for _ in range(SIZE_10000)]


# со словарем
def func1(array):
    d = {}
    freq_num = array[0]
    for num in array:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    count = 1
    for key in d:
        if d[key] > count:
            count = d[key]
            freq_num = key
    return freq_num


# с вложенными циклами (с урока)
def func2(array):
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    return num


# упоротый
def func3(array):
    array.sort()
    count = 1
    res = array[0]
    last = len(array) - 1
    for i in range(last):
        tmp = 1
        while True:
            if i == last:
                break
            if array[i] == array[i + 1]:
                tmp += 1
                if tmp > count:
                    count = tmp
                    res = array[i]
            else:
                break
            i += 1
    return res


print(timeit.timeit('func1(my_array_10)', number=1000, globals=globals()))  # 0.001825
print(timeit.timeit('func1(my_array_20)', number=1000, globals=globals()))  # 0.003089
print(timeit.timeit('func1(my_array_30)', number=1000, globals=globals()))  # 0.005084
print(timeit.timeit('func1(my_array_40)', number=1000, globals=globals()))  # 0.005999
print(timeit.timeit('func1(my_array_50)', number=1000, globals=globals()))  # 0.007832
print(timeit.timeit('func1(my_array_60)', number=1000, globals=globals()))  # 0.009640
print(timeit.timeit('func1(my_array_70)', number=1000, globals=globals()))  # 0.010997
print(timeit.timeit('func1(my_array_80)', number=1000, globals=globals()))  # 0.011948
print(timeit.timeit('func1(my_array_90)', number=1000, globals=globals()))  # 0.013970
print(timeit.timeit('func1(my_array_100)', number=1000, globals=globals()))  # 0.015971
print(timeit.timeit('func1(my_array_200)', number=1000, globals=globals()))  # 0.030927
print(timeit.timeit('func1(my_array_300)', number=1000, globals=globals()))  # 0.047192
print(timeit.timeit('func1(my_array_400)', number=1000, globals=globals()))  # 0.062264

cProfile.run('func1(my_array_10000)')

#       4 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.001    0.001    0.001    0.001 task_1.py:45(func1)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('Второй')
print(timeit.timeit('func2(my_array_10)', number=1000, globals=globals()))  # 0.009603
print(timeit.timeit('func2(my_array_20)', number=1000, globals=globals()))  # 0.028369
print(timeit.timeit('func2(my_array_30)', number=1000, globals=globals()))  # 0.053433
print(timeit.timeit('func2(my_array_40)', number=1000, globals=globals()))  # 0.093879
print(timeit.timeit('func2(my_array_50)', number=1000, globals=globals()))  # 0.135961
print(timeit.timeit('func2(my_array_60)', number=1000, globals=globals()))  # 0.189270
print(timeit.timeit('func2(my_array_70)', number=1000, globals=globals()))  # 0.250543
print(timeit.timeit('func2(my_array_80)', number=1000, globals=globals()))  # 0.332202
print(timeit.timeit('func2(my_array_90)', number=1000, globals=globals()))  # 0.409958
print(timeit.timeit('func2(my_array_100)', number=1000, globals=globals()))  # 0.502445
print(timeit.timeit('func2(my_array_200)', number=1000, globals=globals()))  # 1.925197
print(timeit.timeit('func2(my_array_300)', number=1000, globals=globals()))  # 1.925197
print(timeit.timeit('func2(my_array_400)', number=1000, globals=globals()))  # 8.4245047

cProfile.run('func2(my_array_10000)')

#       10005 function calls in 5.492 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    5.492    5.492 <string>:1(<module>)
#      1    5.490    5.490    5.492    5.492 task_1.py:62(func2)
#      1    0.000    0.000    5.492    5.492 {built-in method builtins.exec}
#  10001    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('Третий')
print(timeit.timeit('func3(my_array_10)', number=1000, globals=globals()))  # 0.001854
print(timeit.timeit('func3(my_array_20)', number=1000, globals=globals()))  # 0.00317
print(timeit.timeit('func3(my_array_30)', number=1000, globals=globals()))  # 0.004949
print(timeit.timeit('func3(my_array_40)', number=1000, globals=globals()))  # 0.0061
print(timeit.timeit('func3(my_array_50)', number=1000, globals=globals()))  # 0.007834
print(timeit.timeit('func3(my_array_60)', number=1000, globals=globals()))  # 0.009123
print(timeit.timeit('func3(my_array_70)', number=1000, globals=globals()))  # 0.01197
print(timeit.timeit('func3(my_array_80)', number=1000, globals=globals()))  # 0.012114
print(timeit.timeit('func3(my_array_90)', number=1000, globals=globals()))  # 0.014454
print(timeit.timeit('func3(my_array_100)', number=1000, globals=globals()))  # 0.016646
print(timeit.timeit('func3(my_array_200)', number=1000, globals=globals()))  # 0.0334
print(timeit.timeit('func3(my_array_300)', number=1000, globals=globals()))  # 0.057
print(timeit.timeit('func3(my_array_400)', number=1000, globals=globals()))  # 0.08387

cProfile.run('func3(my_array_10000)')

#       6 function calls in 0.014 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#      1    0.012    0.012    0.014    0.014 task_1.py:77(func3)
#      1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}


# Первый и третий алгоритмы имеют сложность O(n), второй - O(n ** 2). Первый алгоритм выполняется быстрее.
# Графики - https://docs.google.com/spreadsheets/d/1e5zFEDkOG-EVbw8PSKAYfcz3cX30uXdBfTxIZgT9ytU/edit?usp=sharing
