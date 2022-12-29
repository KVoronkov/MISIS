def moving(n, x, y, z):
    if n == 1:
        print(f'1 {x} {y}')
        return
    moving(n-1, x, z, y)
    print(f'{n} {x} {y}')
    moving(n-1, z, y, x)


n = 3
moving(n, '1', '3', '2')
