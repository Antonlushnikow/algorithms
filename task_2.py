"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""

import cProfile
import timeit


# Первый алгоритм
def prime(n):
    lst = []
    num = 2
    i = 0
    while i < n:
        count = 0
        for j in range(1, num):
            if num % j == 0:
                count += 1
        if count == 1:
            lst.append(num)
            i += 1
        num += 1
    return lst[n-1]


# Второй алгоритм (через решето Эратосфена)
def sieve(n):
    prime_lst = []
    k = 2
    while len(prime_lst) < n:  # пока длина списка с простыми числами меньше n
        a = [0] * k            # повторяем решето эратосфена на увеличивающемся диапазоне чисел
        for i in range(k):
            a[i] = i
        a[1] = 0

        m = 2
        while m < k:
            if a[m] != 0:
                j = m * 2
                while j < k:
                    a[j] = 0
                    j = j + m
            m += 1

        for i in range(k-1, len(a)):
            if a[i] != 0:
                prime_lst.append(a[i])
        k += 1
    return prime_lst[n-1]


def test_prime(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    for i, item in enumerate(lst):
        assert item == func(i+1), f'Ошибка {i}'
        print(f'Тест {i} OK')


# test_prime(prime)
# test_prime(sieve)

print(timeit.timeit('prime(5)', number=1000, globals=globals()))  # 0.0082692
print(timeit.timeit('prime(10)', number=1000, globals=globals()))  # 0.0371873
print(timeit.timeit('prime(20)', number=1000, globals=globals()))  # 0.186719
print(timeit.timeit('prime(40)', number=1000, globals=globals()))  # 1.056029
print(timeit.timeit('prime(60)', number=1000, globals=globals()))  # 2.70110
print(timeit.timeit('prime(80)', number=1000, globals=globals()))  # 5.6186
print(timeit.timeit('prime(100)', number=1000, globals=globals()))  # 9.7530

cProfile.run('prime(1000)')

#       1004 function calls in 2.372 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    2.372    2.372 <string>:1(<module>)
#      1    2.372    2.372    2.372    2.372 task_2.py:12(prime)
#      1    0.000    0.000    2.372    2.372 {built-in method builtins.exec}
#   1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit('sieve(5)', number=1000, globals=globals()))  # 0.02575
print(timeit.timeit('sieve(10)', number=1000, globals=globals()))  # 0.129408
print(timeit.timeit('sieve(20)', number=1000, globals=globals()))  # 0.689866
print(timeit.timeit('sieve(40)', number=1000, globals=globals()))  # 4.07719
print(timeit.timeit('sieve(60)', number=1000, globals=globals()))  # 10.82749
print(timeit.timeit('sieve(80)', number=1000, globals=globals()))  # 24.28957
print(timeit.timeit('sieve(100)', number=1000, globals=globals()))  # 44.75684

cProfile.run('sieve(1000)')

# 16843 function calls in 12.139 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   12.139   12.139 <string>:1(<module>)
#         1   12.136   12.136   12.139   12.139 task_2.py:29(sieve)
#         1    0.000    0.000   12.139   12.139 {built-in method builtins.exec}
#     15839    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# по графикам кажется, что оба O(n^2). Эратосфен получился не очень оптимальным, он скорее удобен,
# когда известно максимальное число. Или я неудачно реализовал.
# графики - https://docs.google.com/spreadsheets/d/1IUuztM-9sNmlg-0_VSX4G1NJLAaJ6zHccC0wybNG0RU/edit?usp=sharing
