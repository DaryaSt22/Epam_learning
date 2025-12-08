# 4. Сумма только положительных (флаг фильтрации)
# Функция sum_numbers(numbers, only_positive=False)
# Если only_positive=False → возвращает сумму всех чисел списка numbers.
# Если only_positive=True → суммирует только положительные числа.


def sum_numbers(numbers, only_positive=False):

    if only_positive:
        return sum(x for x in numbers if x > 0)
    else:
        return sum(numbers)



print(sum_numbers([2, 4, 6, 8, 3, 11, 15, 16, -4], True))
print(sum_numbers([2, 4, 6, 8, 3, 11, 15, 16, -4], False))
