alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
            'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

choose = int(input('''Предложение зашифровано или его нужно зашифровать?
1 - нужно зашифровать
2 - нужно расшифровать
Ответ: '''))
sentence = input('Введите предложение: ')
step = int(input('Введите шаг при шифровании: '))
if choose == 1:
    encode_dict = {}
    for num, letter in enumerate(alphabet):
        if letter not in encode_dict.keys():
            if num+step <= 32:
                encode_dict[letter] = alphabet[num+step]
            if num+step > 32:
                encode_dict[letter] = alphabet[num-33+step]
    encoded_sentence = ''
    for letter in sentence:
        if letter in encode_dict.keys():
            encoded_sentence += encode_dict[letter]
        else:
            encoded_sentence += letter
    print(f'Зашифрованное предложение: {encoded_sentence}')

if choose == 2:
    decode_dict = {}
    for num, letter in enumerate(alphabet):
        if letter not in decode_dict.keys():
            if num-step >= 0:
                decode_dict[letter] = alphabet[num-step]
            if num-step < 0:
                decode_dict[letter] = alphabet[num+33-step]
    decoded_sentence = ''
    for letter in sentence:
        if letter in decode_dict.keys():
            decoded_sentence += decode_dict[letter]
        else:
            encoded_sentence += letter
    print(f'Расшифрованное предложение: {decoded_sentence}')
