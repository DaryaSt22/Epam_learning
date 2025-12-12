# 22. Функция-отладчик
# Сделай debug(*values), которая печатает все значения на одной строке через |.
# Например: debug(1, "hi", True) → 1 | hi | True.


def debug(*values):
    result = '|'.join(map(str, values))
    return result


print(debug(1, "hi", True))
