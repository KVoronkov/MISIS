def search_dict(site, search_key, depth):
    if isinstance(site, dict):
        if search_key not in site:
            print('Значение ключа нельзя определить')
            return None
        if search_key in site.keys() and (depth is None or depth == 0):
            print(f'Значение ключа: {site.values()}')
        elif search_key in site:
            return site.get(search_key)
        elif depth is not None and depth == 0:
            return None
        for value in site.values():
            if search_dict(value, search_key, (depth-1 if depth is not None else None)
                           ) is not None:
                break
        else:
            result = None
        print(f'Значение ключа: {result}')
        return result
    else:
        return None


site = {
    'html': {
        'head': {
            'title': 'This site'
        },
        'body': {
            'h2': 'here is my title',
            'div': "There's some kind of block here",
            'p': 'And here is a new paragraph'
        }
    }
}

answer_key = str(input('Введите искомый ключ: '))
answer_depth = str(input('Хотите ввести максимальную глубину? Y/N: '))
if answer_depth.lower() == 'Y':
    depth = int(input('Введите максимальную глубину: '))
else:
    depth = None
search_dict(site, answer_key, depth)
