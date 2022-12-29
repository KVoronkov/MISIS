def polindrom(word):
    for i in range(len(word)):
        if not word[i] == word[len(word) - 1 - i]:
            return False
    return True


row = input('Введите строку: ')
print(f'Слово является полиндромом: {polindrom(row)}')
