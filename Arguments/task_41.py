# 41. Валидатор аргументов
# Функция safe_divide(a, b) — делит a на b.
# Напиши обёртку call_safe(func, *args, **kwargs), которая:
# пытается вызвать func(*args, **kwargs),
# если поймала ZeroDivisionError, возвращает строку "division by zero".


def safe_divide(a, b):
    return a // b


def call_safe(func, *args, **kwargs):
    try:
        return func
    except ZeroDivisionError:
        return "division by zero"


print(call_safe(safe_divide(10, 2), 10, 15, time='123'))
