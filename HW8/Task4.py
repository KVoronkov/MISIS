import pathlib


def calculation(answer):
    with open(pathlib.Path(
            __file__).parent.resolve() / str(answer), 'r') as n:
        file_n = n.readlines()
    for line in file_n:
        try:
            a, operation, b = line.split(' ')
        except ValueError as ve:
            print('Некорректно введены условия')
        if operation not in ['+', '-', '/', '*', '**', '//', '%']:
            print('Некорректно введен символ операции')
        try:
            a = int(a)
            b = int(b)
        except ValueError as ve:
            print('Не являются целыми числами')

        match operation:
            case '+':
                print(f'Результат: {a+b}')
            case '-':
                print(f'Результат: {a-b}')
            case '*':
                print(f'Результат: {a*b}')
            case '**':
                print(f'Результат: {a**b}')
            case '/':
                print(f'Результат: {a/b}')
            case '//':
                print(f'Результат: {a//b}')
            case '%':
                print(f'Результат: {a%b}')


calculation(input('Введите название файла: '))  # calc_nums.txt
