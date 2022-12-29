shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], [
    'седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = str(input(f'Введите название детали: '))

quantity = 0
price = 0
for description in shop:
    if name.lower() == description[0]:
        quantity += 1
        price += description[1]
print(f'Название детали: {name} \n \
Кол-во деталей — {quantity} \n \
Общая стоимость — {price}')
