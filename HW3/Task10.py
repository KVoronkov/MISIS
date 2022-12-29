def add_to_polindrom(start_list):
    temp_shift, final_shift = 0, 0
    changed = False
    reversed_list = start_list.copy()
    reversed_list.reverse()
    for original_list_item in start_list:

        if original_list_item != reversed_list[temp_shift]:
            print(
                f'{original_list_item} != {reversed_list[temp_shift]}')
            final_shift = temp_shift
            temp_shift = 0
            changed = True
        else:
            print(
                f'{original_list_item} == {reversed_list[temp_shift]}')
            temp_shift += 1

    if not changed:
        print('Уже полиндром')
        return start_list
    else:
        result = reversed_list[final_shift+1:]
        print(f'Итоговый сдвиг: {final_shift + 1}')
        print(f'Нужно добавить: {result}')
        return result


if __name__ == "__main__":
    test_list_1 = [1, 2, 3, 4, 5]  # 4, 3, 2, 1
    test_list_2 = [1, 2, 3, 2, 2]  # 3, 2, 1
    test_list_3 = [3, 1, 2, 2, 3, 1]  # 3, 2, 2, 1, 3
    test_list_4 = [1, 2, 1]  # None
    for test_list in [test_list_1, test_list_2, test_list_3, test_list_4]:
        print('---------')
        add_to_polindrom(test_list)
