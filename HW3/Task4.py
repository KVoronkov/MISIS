guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


while True:
    print('-'*5)
    action = input(
        f'Сейчас на вечеринке {len(guests)} человек: {guests}\nГость пришёл или ушёл?: ')
    while action.lower() not in ['пришёл', 'ушёл', 'пора спать', 'ушел', 'пришел']:
        action = input('Уточни еще раз, пожалуйста: ')
    if action.lower() == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    name = input('Имя гостя: ')
    if action.lower() in ('пришёл', 'пришел') and len(guests) < 6:
        guests.append(name)
        print(f'Привет, {name}!')
    elif action.lower() in ('пришёл', 'пришел') and len(guests) >= 6:
        print(f'Прости, {name}, но мест нет')
    elif action.lower() in ('ушёл', 'ушел') and name not in guests:
        print(f'Прости, {name} ушел до этого или вовсе не приходил')
    elif action.lower() in ('ушёл', 'ушел') and len(guests) == 0:
        print(f'Прости, но все уже ушли')
    else:
        guests.remove(name)
        print(f'Пока, {name}')
