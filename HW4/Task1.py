def gcd(a, b):
    a_max = max(a, b)
    b_min = min(a, b)
    while b_min != 0:
        a_max -= b_min
        if a_max < b_min:
            temp = a_max
            a_max = b_min
            b_min = temp
    print(f'Наибольший общий делитель: {a_max}')
    return a_max


def gcd_lcm(a, b):
    answer = gcd(a, b)
    print(f'Hаименьшее общее кратное: {a*b//answer}')


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

gcd_lcm(a, b)
