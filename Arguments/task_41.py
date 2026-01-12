# 41. Валидатор аргументов
# Функция safe_divide(a, b) — делит a на b.
# Напиши обёртку call_safe(func, *args, **kwargs), которая:
# пытается вызвать func(*args, **kwargs),
# если поймала ZeroDivisionError, возвращает строку "division by zero".


def safe_divide(a, b):
    return a // b

def call_safe(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except ZeroDivisionError:
        return "division by zero"


print(call_safe(10, 5))
