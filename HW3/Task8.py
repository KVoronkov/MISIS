count_people = int(input('Кол-во человек: '))
num = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {num}-й человек')

people = list(range(1, count_people + 1))
start = 0
while len(people) > 1:
    print(f' \nТекущий круг людей: {people}')
    print(f'Начало счёта с номера {people[start]}')
    start += num
    start %= len(people)
    start -= 1
    print(f'Выбывает человек под номером {people[start]}')
    people.pop(start)
    if start < 0:
        start = 0
print('______________________________')
print(f'Остался человек под номером {people[0]}')
