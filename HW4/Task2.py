n = int(input(f'Введите кол-во предложений: '))
list = [input(f'Введите {i+1}-е предложение/слово/цифру: ')
        for i in range(n)]

result = 0
count = 0
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in range(len(list)):
    if result > 0:
        count += 1
        result = 0
    for j in range(len(numbers)):
        if numbers[j] in list[i]:
            result += 1
if result > 0:
    count += 1
print(f'\nКол-во предложений, содержащих цифру: {count}.')
