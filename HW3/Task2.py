class_1 = list(range(160, 177, 2))
class_2 = list(range(162, 181, 3))

union_class = class_1 + class_2
sorted(union_class, reverse=False)

print(f'Отсортированный список учеников: {union_class}')
