import zipfile
import pathlib
import io

from collections import Counter


def read_text_from_zip(file, file_format, name, name_format):
    lines = []
    with zipfile.ZipFile(pathlib.Path(
    __file__).parent.resolve()/ str(f'{file}.{file_format}'), 'r') as z:
        with io.TextIOWrapper(z.open(str(f'{name}.{name_format}')), encoding="utf-8") as f:
            for line in f:
                lines.append(line)

    result = Counter()
    for data in lines:
        result += Counter(data)

    most_common_letters = result.most_common()
    most_common_letters.reverse()
    with open(pathlib.Path(
        __file__).parent.resolve() / str(f'{answer_file}-count.txt'), 'w') as f:
        f.write('\n'.join('{} {}'.format(
            x[0], x[1]) for x in most_common_letters))
    print(f'Подсчеты записаны в {answer_file}-count.txt')

answer_zip = input('Введите название архива: ') #voyna-i-mir
answer_zip_format = input('Введите формат архива: ') #zip
answer_file = input('Введите название файла: ') #voyna-i-mir
answer_file_format = input('Введите формат файла: ') #txt

read_text_from_zip(answer_zip, answer_zip_format, answer_file, answer_file_format)