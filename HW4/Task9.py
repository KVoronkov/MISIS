def convert_to_decimal(number, value_from):
    return int(number, base=value_from)


def convert_to(value_from, value_to, number):
    letters = ['A', 'B', 'C', 'D', 'E', 'F'] 
    if value_from == value_to:
        print(f'Вы ввели одну и ту же систему счисления, ответ: {number}')
        return number
    if value_from < 2:
        print(
            f'Вы ввели некорректную систему счисления из которой надо переводить, ответ: {number}')
        return number
    if value_to > 16:
        print(
            f'Вы ввели некорректную систему счисления в которую надо переводить, ответ: {number}')
        return number
    number = convert_to_decimal(number, value_from)
    value_to = int(value_to)
    result = ''
    while number > 0:
        digit = number % value_to
        if digit < 10:
            result += str(digit)
        else:
            result += letters[number - 10]
        number //= value_to
    print(f'Ответ: {result[::-1]}')


number = input(f'Введите число: ')
value_from = int(input(f'Система счисления из которой надо перевести: '))
value_to = int(input(f'Система счисления в которую надо перевести: '))

convert_to(value_from, value_to, number)
