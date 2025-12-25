# 25. Внутри функции использовать args как список
# Функция reverse_all(*args) должна вернуть список, где все аргументы идут в обратном порядке.
# Например: reverse_all(1, 2, 3) → [3, 2, 1].


def reverse_all(*args):
    return list(reversed(*args))


print(reverse_all((1, 2, 3)))