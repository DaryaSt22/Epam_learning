# 37. Обязательный именованный аргумент (через синтаксис)
# Напиши функцию:
# def greet_user(name, *, polite=True):
# name — позиционный/именованный,
# polite — обязательно именованный.
# Проверь, что:
# greet_user("Anna") — работает или нет?
# greet_user("Anna", polite=False) — работает.


def greet_user(name, *, polite=True):
    print(name, polite)


greet_user("Anna", polite=False)
greet_user("Anna")