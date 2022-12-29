def number_search():
    numbers = list(range(1, 101))
    answer = 0
    while answer != 1:
        number = numbers[len(numbers)//2]
        answer = int(input(
            f'''\nТвое число равно, меньше или больше {number}?
            1 - равно
            2 - больше
            3 - меньше
            Ответ: '''))
        if answer == 2:
            numbers = numbers[len(numbers)//2+1:]
        if answer == 3:
            numbers = numbers[:len(numbers)//2]
    return number

print(f'Загаданное число: {number_search()}')



