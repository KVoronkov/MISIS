list_1 = [input(f'Введите {i}-е число для первого списка: : ')
          for i in range(1, 4)]
list_2 = [input(f'Введите {i}-е число для второго списка: : ')
          for i in range(1, 8)]

print(f'Первый список: {list_1}')
print(f'Второй список: {list_2}')

list_1 += list_2
list_1 = list(set(list_1))

print(f'Новый первый список с уникальными элементами: {list_1}')
