"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def f_odd(num):
    if num:
        i = num % 10
        if i % 2:
            return 1 + f_odd(num // 10)
        else:
            return f_odd(num // 10)
    return 0


def f_len(num):
    if num:
        return 1 + f_len(num // 10)
    return 0


user_num = int(input('Введите натуральное число:\n'))

odd = f_odd(user_num)
even = f_len(user_num) - odd
print(f'Нечетных цифр - {odd}, четных - {even}')
