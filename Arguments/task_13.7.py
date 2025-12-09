# 7. Диапазон чисел с флагом чётности
# Функция make_range(start, end, only_even=False)
# Возвращает список чисел от start до end включительно.
# Если only_even=True, в список попадают только чётные числа.
from typing import List


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

def make_range_from_raman(start, end, only_even=False) -> List[int]:
    lst_new = list(range(start, end + 1))
    if only_even:
        return list(x for x in lst_new if x % 2 == 0)
    else:
        return lst_new

print(make_range_from_raman(2, 14, True))