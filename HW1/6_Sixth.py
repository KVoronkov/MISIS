# Задание 6

def rounds(v, t):
    s = v * t
    rounds = 0
    if s >= 123:
        rounds = int(s // 123)
        km = s % 123
    print(
        f'{rounds} круг(а/ов) преодолел спортсмен и остановился на {km} километре, проехав всего {s} километров')


v = int(input(f'Введите скорость v:'))
t = int(input(f'Введите время (в часах) t:'))
rounds(v, t)
