# 35. Фильтрация по типу значений
# Функция only_ints(**kwargs) должна вернуть новый словарь, куда попадают только те пары, где значение — int.
# Пример:
# only_ints(a=1, b="hi", c=3) → {"a": 1, "c": 3}.


def only_ints(**kwargs):
    sorted_kwargs = {k: v for k, v in kwargs.items() if isinstance(v, int)}
    return sorted_kwargs


print(only_ints(a=1, b="hi", c=3))


