# Задание 2
import math


def operators(a, b):
    print(f'{a}+{b} = {round(a+b, 2)}')
    print(f'{a}-{b} = {round(a-b, 2)}')
    print(f'{a}*{b} = {round(a*b, 2)}')
    print(f'{a}/{b} = {round(a/b, 2)}')
    print(f'{a}//{b} = {round(a//b, 2)}')
    print(f'{a}%{b} = {round(a%b, 2)}')
    print(f'{a}**{b} = {round(a**b, 2)}')
    for number in [a, b]:
        result = math.log10(number)
        if type(result) == float:
            result = round(result, 2)
        print(f'log_10({number}) = {result}')
    print(f'{a}>{b} = {a>b}')
    print(f'{a}>={b} = {a>=b}')
    print(f'{a}<{b} = {a<b}')
    print(f'{a}<={b} = {a<=b}')
    print(f'{a}!={b} = {a!=b}')
    print(f'{a}=={b} = {a==b}')


a = int(input(f'Введите значение первого числа:'))
b = int(input(f'Введите значение второго числа:'))
operators(a, b)
