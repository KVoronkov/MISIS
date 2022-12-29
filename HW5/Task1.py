def unzipping_lists(target_list):
    final = []
    for obj in target_list:
        if isinstance(obj, list):
            obj = unzipping_lists(obj)
            final += obj
        else:
            final.append(obj)
    return final


check_list = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
print(
    f'Итоговый список: {unzipping_lists(check_list)}')
