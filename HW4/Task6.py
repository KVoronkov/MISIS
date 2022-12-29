def group_by_sign(*args):
    negative = []
    positive = []
    for number in args:
        if number < 0:
            negative.append(number)
        else:
            positive.append(number)
    return sorted(negative, reverse=True), sorted(positive)


result = group_by_sign(1, 3, 5, 6, 7, 8, -1, -4, -100, 0)
print(f'''Отсортированный массив отрицательных чисел: {result[0]}
Отсортированный массив положительных чисел: {result[1]}''')
