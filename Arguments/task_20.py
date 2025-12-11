# 20. Первый и остальные
# Напиши функцию first_and_rest(first, *rest), которая печатает:
# first отдельно,
# потом кортеж rest.
# Потренируй вызовы с 1, 2 и 5 аргументами.

def first_and_rest(first, *rest):
    print(first)
    print(rest)

first_and_rest(1)
first_and_rest(1, 2)
first_and_rest(1, 2, 5, 4, 9)
