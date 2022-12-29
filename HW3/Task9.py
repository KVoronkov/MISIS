friends = int(input('Кол-во друзей: '))
num = int(input('Кол-во долговых расписок: '))

result = [0]*friends
for i in range(num):
    print(f'{i+1}-я расписка')
    borrower = int(input('Кому: '))
    debtor = int(input('От кого: '))
    money = int(input('Сколько: '))
    result[borrower - 1] = result[borrower - 1] - money
    result[debtor - 1] = result[debtor - 1] + money
print('=============\nБаланс друзей')
for id in range(len(result)):
    print(f'{id + 1} : {result[id]}')

# Пример 1:
# Кол-во друзей: 2
# Долговых расписок: 3

# 1-я расписка
# Кому: 1
# От кого: 2
# Сколько: 10

# 2-я расписка
# Кому: 1
# От кого: 2
# Сколько: 20

# 3-я расписка
# Кому: 1
# От кого: 2
# Сколько: 20

# Баланс друзей:
# 1: -50
# 2: 50

# Пример 2:
# Кол-во друзей: 3
# Долговых расписок: 1

# 1-я расписка
# Кому: 3
# От кого: 1
# Сколько: 100

# Баланс друзей:
# 1 : 100
# 2 : 0
# 3 : -100
