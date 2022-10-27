# Задание 3

def function(x, y, z):
    f = (((x**5 + 7)/(abs(-6)*y))**(1/3))/(7 - z % y)
    return round(f, 2)


x = int(input(f'Введите значения x:'))
y = int(input(f'Введите значения y:'))
z = int(input(f'Введите значения z:'))
print(f'Для x = {x}, y = {y} и z = {z} значение f = {function(x, y, z)}')
