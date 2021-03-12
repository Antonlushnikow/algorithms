"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего. """

from collections import defaultdict

companies = defaultdict(float)
count = int(input('Введите количество предприятий\n'))
over_profit = 0

for i in range(1, count+1):
    comp_name = input(f'Введите название предприятия {i}\n')
    for j in range(1, 5):
        companies[comp_name] += float(input(f'Введите прибыль за {j} квартал\n'))
    over_profit += companies[comp_name]

avg = over_profit / count

print(f'Средняя прибыль: {avg:.2f}')

print(f'\nПредприятия с прибылью выше среднего:')
for name, profit in companies.items():
    if profit >= avg:
        print(f'{name} ({profit})', end=', ')

print(f'\n\nПредприятия с прибылью ниже среднего:')
for name, profit in companies.items():
    if profit < avg:
        print(f'{name} ({profit})', end=', ')
