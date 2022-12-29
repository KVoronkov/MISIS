team_name = str(input('Введите название футбольной команды:\n'))
print(f'{team_name} - чемпион!')
team_name = team_name.lower()
print(len(team_name)*'-')
print(f'Длина наименования команды - {len(team_name)} символов')
# if team_name.find('п') >= 0:
#     print(f'Буква "п" присутствует')
# else:
#     print(f'Буква "п" отсутствует')
print(f'Буква "п" присутствует: {team_name.find("п") >= 0}')
print(f'Количество повторений буквы "а": {team_name.count("а")}')
