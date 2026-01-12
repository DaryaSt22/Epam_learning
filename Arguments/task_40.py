# 40. Перенаправление аргументов
# Напиши две функции:
# def inner(a, b, c):
# def outer(*args, **kwargs):

#     # внутри outer вызвать inner, аккуратно передав ей аргументы
# Задача: сделать так, чтобы outer принимала те же аргументы,
# что и inner, но через *args, **kwargs, и просто передавала их дальше.


def inner(a, b, c):
    return a, b, c


def outer(*args, **kwargs):
    return inner(*args, **kwargs)


print(outer(5, 4, 6))