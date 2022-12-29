import pathlib


class IncorrectInputError(Exception):
    def __init__(self, message):
        super().__init__(message)


def delete_comments(name, name_2, type_file):
    try:
        with open(pathlib.Path(
                __file__).parent.resolve() / str(name+'.'+type_file), 'r') as n:
            file_n = n.readlines()
    except Exception as ex:
        raise IncorrectInputError('Некорректно введено имя исходного файла')
    file_d = [line for line in file_n if '#' not in line]
    with open(pathlib.Path(
            __file__).parent.resolve() / str(name_2+'.'+type_file), 'w') as d:
        d.writelines(file_d)
    print('Комментарии удалены')


def delete():
    try:
        delete_comments(input('Введите наименование файла: '), input(
            'Введите наименование файла назначения: '), input(
            'Введите тип: '))  # test.py
    except Exception as e:
        print(f'Ошибка в обработке ввода: {str(e)}')


delete()
