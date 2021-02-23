"""
https://drive.google.com/file/d/19bi2DvVf_7hyZynGFKdoL0HwExYewfKL/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

num = int(input('Введите трехзначное число\n'))

n1 = num // 100
n2 = (num % 100) // 10
n3 = num % 10

print(f'Сумма цифр: {n1 + n2 + n3}')
print(f'Произведение цифр: {n1 * n2 * n3}')
