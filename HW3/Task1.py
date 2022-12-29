main = [1, 5, 3]
list_a = [1, 5, 1, 5]
list_b = [1, 3, 1, 5, 3, 3]


main += list_a
print(f'Кол-во цифр 5 при первом объединении: {main.count(5)}')

index = [value for value in range(0, len(main)) if main[value] == 5]
for i, number in enumerate(main):
    if number == 5:
        del main[i]

main += list_b
print(f'Кол-во цифр 3 при втором объединении: {main.count(3)}')
print(f'Итоговый список: {main}')
