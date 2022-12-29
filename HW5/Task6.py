def inverter(number, inverted_number):
    if number == 0:
        return inverted_number
    return inverter(number // 10, 10 * inverted_number + number % 10)


print(f'Ответ: {inverter(int(input("Введите число: ")))}')
