# 38. Функция-обёртка
# Напиши функцию debug_call(func, *args, **kwargs), которая:
# печатает, какие аргументы ей передали (args, kwargs),
# вызывает func(*args, **kwargs),
# возвращает результат func.
# Потренируй на простой функции add(a, b).


def add(a, b):
    return a, b


def debug_call(func, *args, **kwargs):
    print(args, kwargs)
    result = func(4, 5), args, kwargs
    return result


print(debug_call(add, 55, 88, a=10, b=89))
# print(add(2, 2))
