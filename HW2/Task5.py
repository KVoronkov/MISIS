# В данной задаче все значения задаются в коде (без input())

# 1. Создание словаря
# Создать пустой словарь
info = {}

# Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
info["фио"] = 'Воронков Кирилл Евгеньевич'
# По хорошему datetime.date(2000, 2, 24)
info['дата_рождения'] = '30/04/2001'
info['место_рождения'] = 'Моздок'

# Напечатать словарь
print(info)

# Создать ключ "хобби" со значением = список из строк -
# наименований хобби (например "плавание" и т.д.)
info['хобби'] = ['машины', 'гитара']

# Добавить "программирование" в список хобби
info["хобби"].append('программирование')

# Создать ключ "животные" со значением = кортеж из строк -
# имен домашних животных (например "кошка Мурка" и т.д.)
info['животные'] = ('пес Кантор')

# Создать ключ "ЕГЭ" и поместить в него пустой словарь
info['ЕГЭ'] = {}

# В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах,
# где ключ - наименование предмета, а значение - количество баллов

info['ЕГЭ']['Математика'] = 78
info['ЕГЭ']['Русский язык'] = 90
info['ЕГЭ']['Английский язык'] = 93
info['ЕГЭ']['Обществознание'] = 86

# Добавить экзамен, который не был сдан, после чего удалить его
info['ЕГЭ']['Информатика'] = None
del info['ЕГЭ']['Информатика']

# Создать ключ "вузы" и поместить в него пустой словарь
info['вузы'] = {}

# В словарь info["вузы"] добавить информацию о вузах,
# где ключ - аббревиатура вуза, а значение -
# количество баллов для специальности, на которую хотели поступить
info['вузы']['РАНХиГС'] = 345
info['вузы']['Финансовый университет'] = 376


# 2. Вывод на экран
print("Данные:")
# Получившийся словарь
print(info)

# Список экзаменов ЕГЭ в алфавитном порядке
# (используйте метод ``keys()``, преобразовав результат в кортеж)
exams = sorted(info['ЕГЭ'].keys())
print("Предметы:", exams)
# Список вузов в алфавитном порядке
uni = sorted(info['вузы'].keys())
print("Вузы:", uni)

# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

# Выделить имя из info["фио"]
name = info['фио'].split(' ')[1]
# Начинается на гласную? (True/False)
starts_with_vowel = name[0] in 'ауоиэыяюеё'
print("* мое имя начинается на гласную букву:", starts_with_vowel)

# Выделить месяц из info["дата_рождения"]
# Если бы использовали datetime: month = info["дата_рождения"].month
month = int(info["дата_рождения"].split('/')[1])
# Родился зимой или летом? (True/False)
born_in_winter_or_summer = month in (1, 2, 6, 7, 8, 12)
print("* родился летом или зимой:",  born_in_winter_or_summer)

# Количество хобби и первое из них
hobbies_count = len(info['хобби'])
print(
    "* у меня {} хобби, первое \"{}\"".format(hobbies_count, info['хобби'][0]))

# Количество сданных экзаменов
print("* после окончания школы сдавал {} экз.".format(len(info['ЕГЭ'])))


# Сумма баллов по экзаменам
sum_mark = sum(info['ЕГЭ'].values())
print("* сумма баллов = {}".format(sum_mark))

# Максимальный балл среди сданных
max_mark = max(info['ЕГЭ'].values())
print("* макс. балл = {}".format(max_mark))

# Количество вузов, в которые Вы проходите по баллам
# Подсказка: определить, проходите Вы или нет, можно простым сравнением
# суммы баллов с проходным баллом вуза - ``True/False``.
# Для того, чтобы определить количество таких вузов, преобразуйте
# сравнение в целое число (используя ``int()``) и сложите все сравниваемые вузы.
vuz_count = len(
    [value for value in info['вузы'].values() if value <= sum_mark])
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))
