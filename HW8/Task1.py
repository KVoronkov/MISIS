import pathlib
import re


def calculation(name):
    with open(pathlib.Path(
            __file__).parent.resolve() / str(name), 'r') as n:
        data = n.read()
    numbers = [int(number) for number in re.findall(r'\d+', data)]
    result = sum(numbers)
    print(f'Сумма = {result}')


calculation(input('Введите наименование файла: '))  # numbers.txt
