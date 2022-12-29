class CheckError(Exception):
    def __init__(self, message):
        super().__init__(message)


def converter(answer):
    if answer.upper() not in ['A', 'B', 'C', 'D', 'E', 'P', '5', '4', '3', '2', '']:
        raise CheckError('Ошибка при вводе: такой оценки нет')
    marks_numbers = {
        '2': 'P',
        '3': ['E', 'D'],
        '4': ['C', 'B'],
        '5': 'A'}

    marks_letters = {
        'A': 5,
        'B': 4,
        'C': 4,
        'D': 3,
        'E': 3,
        'P': 2
    }
    if answer == '':
        print('_________')
        print('Пока!')
    if answer in marks_numbers.keys():
        print(f'Для оценки {answer}: {marks_numbers[answer]}')
    elif answer.upper() in marks_letters.keys():
        print(f'Для оценки {answer}: {marks_letters[answer.upper()]}')


def converting(answer):
    try:
        converter(answer)
    except CheckError as e:
        print(f'Внимание!\n{str(e)}')


while True:
    answer = input('Введите оценку: ')
    converting(answer)
    if answer == '':
        break
