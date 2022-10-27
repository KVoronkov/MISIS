# Задание 7

from math import prod

def number_split(num):
    list = []
    while num != 0:
        list.append(num % 10)
        num = num // 10
    return list


def output(a, b) -> None:
    for num in (a, b):
        numbers = number_split(num)
        print(
            f'[ Для числа {num} сумма цифр = {sum(numbers)}, а произведение цифр = {prod(numbers)}]')


a = int(input(f'Введите двузначное число:'))
b = int(input(f'Введите трехзначное число:'))
output(a, b)
