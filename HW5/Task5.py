def power_of_2(number):
    number = number / 2
    if number == 2:
        return 'YES'
    elif number > 2:
        return power_of_2(number)
    else:
        return 'NO'


number = int(input('Введите число: '))
print(power_of_2(number))
