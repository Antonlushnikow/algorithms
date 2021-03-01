"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def func(num):
    tmp = num
    i = 0
    while tmp // 10:
        tmp //= 10
        i += 1
    num = num - tmp * 10 ** i
    if num:
        return tmp + 10 * func(num)
    return tmp


user_num = int(input('Введите натуральное число:\n'))
res = func(user_num)

print(f'Обратное по порядку цифр число: {res}')
