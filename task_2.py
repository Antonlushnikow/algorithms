"""Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’,
‘C’, ‘9’, ‘F’, ‘E’]. """

from collections import deque

num1_ = deque('A2')
num2_ = deque('C4F')

hex_int = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def hex_sum(num1, num2):
    tmp1, tmp2 = num1.copy(), num2.copy()
    diff = len(tmp2) - len(tmp1)
    if diff > 0:
        tmp1, tmp2 = tmp2, tmp1
    else:
        diff *= -1

    for _ in range(diff):  # выравниваем нулями слева
        tmp2.appendleft('0')

    res = deque()
    mem = 0

    for _ in range(len(tmp1)):
        i1 = tmp1.pop()
        i2 = tmp2.pop()
        digit = hex_int[((hex_int.index(i1) + hex_int.index(i2)) % 16 + mem) % 16]  # пишем цифру
        mem = (hex_int.index(i1) + hex_int.index(i2) + mem) // 16  # оставляем "в уме"
        res.appendleft(digit)
    if mem:
        res.appendleft(hex_int[mem])
    return res


def hex_mul(num1, num2):
    lst = []
    count = 0
    for i2 in reversed(num2):
        tmp_num = deque()
        mem = 0
        for i1 in reversed(num1):
            digit = hex_int[((hex_int.index(i1) * hex_int.index(i2)) % 16 + mem) % 16]
            mem = (hex_int.index(i1) * hex_int.index(i2) + mem) // 16
            tmp_num.appendleft(digit)
        if mem:
            tmp_num.appendleft(hex_int[mem])
        for _ in range(count):
            tmp_num.append('0')
        count += 1
        lst.append(tmp_num)

    res = deque()
    for i in range(len(lst)):
        res = hex_sum(res, lst[i])

    return res


print(hex_sum(num1_, num2_))
print(hex_mul(num1_, num2_))
