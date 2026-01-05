# 32. Объединение двух словарей через ** при вызове
# Есть два словаря:
# base = {"name": "Anna", "age": 25}
# extra = {"city": "Tallinn", "hobby": "Python"}
# Функция merge_profile(**kwargs) просто возвращает kwargs.
# Задача: вызвать её так, чтобы объединить оба словаря в один с помощью распаковки **.


def merge_profile(**kwargs):
    return kwargs
    base = {"name": "Anna", "age": 25}
    extra = {"city": "Tallinn", "hobby": "Python"}
    merged_dict = {**base, **extra}

    return merged_dict
base = {"name": "Anna", "age": 25}
extra = {"city": "Tallinn", "hobby": "Python"}

print(merge_profile(**base, **extra))