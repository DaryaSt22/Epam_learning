# 22. Функция-отладчик
# Сделай debug(*values), которая печатает все значения на одной строке через |.
# Например: debug(1, "hi", True) → 1 | hi | True.


def debug(*values):
    print(*values, sep=" | ")
    result = ' | '.join(map(str, values))
    print(result)


debug(1, "hi", True)
