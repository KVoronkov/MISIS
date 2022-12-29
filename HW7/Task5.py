class IncorrectInputError(Exception):
    def __init__(self, message):
        super().__init__(message)


def calculation(answer):
    try:
        a, operation, b = answer.split(' ')
    except ValueError as ve:
        raise IncorrectInputError('Некорректно введены условия')
    if operation not in ['+', '-', '/', '*', '**', '//', '%']:
        raise IncorrectInputError('Некорректно введен символ операции')
    try:
        a = int(a)
        b = int(b)
    except ValueError as ve:
        raise IncorrectInputError('Не являются целыми числами')
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


while True:
    answer = input('Введите выражение: ')
    try:
        if answer == '':
            print('Пока!')
            break
        calculation(answer)
    except Exception as e:
        print(f'Ошибка в обработке ввода: {str(e)}')
        print('Попробуйте снова')
        continue
