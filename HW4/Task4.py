row = str(input('Введите строку: '))
row = row.lower()
result = {}
for symbol in row:
    if symbol not in result.keys():
        result[symbol] = 1
    else:
        result[symbol] += 1
print(f'Статистика для предложения\n{result}')
