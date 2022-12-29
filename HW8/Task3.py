import pathlib


class OpenFile:
    def __init__(self, name, mode):
        self.p = pathlib.Path(name)
        if not self.p.is_file() and mode in ['r', 'rb']:
            self.f = open(name, 'w')
        else:
            self.f = open(name, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.f.close()
        return True


name = input('Введите наименование: ')
with OpenFile(pathlib.Path(
        __file__).parent.resolve() / str(name), 'r') as file_obj:
    print(file_obj.read())
