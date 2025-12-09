# 7. Диапазон чисел с флагом чётности
# Функция make_range(start, end, only_even=False)
# Возвращает список чисел от start до end включительно.
# Если only_even=True, в список попадают только чётные числа.

def make_range(start, end, only_even=False):
    lst_new = list(range(start, end + 1))
    lst_two = []
    if only_even:
        for ls in lst_new:
            if ls % 2 == 0:
                lst_two.append(ls)
        return lst_two

    return lst_new


print(make_range(2, 14, False))
