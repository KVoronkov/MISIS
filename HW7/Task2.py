def summarizing():
    sum_now = 0
    while True:
        user_input = input('Введите число: ')
        if user_input == '':
            return sum_now

        try:
            float_input = float(user_input)
        except ValueError as ve:
            print(f'"{user_input}" не является числом')
            continue

        sum_now += float_input
        print(f'Текущая сумма: {sum_now}')


print(f'=====================\nИтоговая сумма = {summarizing()}')
