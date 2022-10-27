# Задание 5

def check(a, b, m, n):
    x = (-1 * b)/a
    if x >= m and x <= n:
        print(f'Попадает, так как x = {x} и {m} <= {x} <= {n}')
    elif x < m:
        print(f'Не попадает, так как x = {x} и {x} > {m}')
    else:
        print(f'Не попадает, так как x = {x} и {n} < {x}')


a = int(input(f'Введите значения a:'))
b = int(input(f'Введите значения b:'))
m = int(input(f'Введите значения m:'))
n = int(input(f'Введите значения n:'))
check(a, b, m, n)
