# 5. Функция с 4 аргументами
# Создай функцию rectangle_info(width, height, symbol, border), которая просто печатает все полученные аргументы.
# Вызови:
# всеми позиционными аргументами,
# частично позиционными, частично именованными.



def rectangle_info(width, height, symbol, border):
    print(width, height, symbol, border)


rectangle_info(5, 4, border=6, symbol=8)
rectangle_info(5, 4, 46, 88)