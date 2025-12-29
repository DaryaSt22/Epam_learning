# 26. Печать именованных аргументов
# Напиши функцию print_kwargs(**kwargs), которая печатает все пары ключ=значение построчно.
# Например:
# print_kwargs(a=1, b=2)
# a = 1
# b = 2


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(a=1, b=2)
