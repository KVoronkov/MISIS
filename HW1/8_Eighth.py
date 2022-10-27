# Задание 8

def sorting(a, b, c):
    tuple = (a, b, c)
    third = max(tuple)
    first = min(tuple)
    second = sum(tuple) - first - third
    print(f'Отсортированные числа: {first, second, third}')


a = int(input(f'Введите первое число:'))
b = int(input(f'Введите второе число:'))
c = int(input(f'Введите третье число:'))
sorting(a, b, c)
