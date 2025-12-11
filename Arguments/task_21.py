# 21. Умножение всех чисел
# Функция multiply_all(*nums) — перемножает все числа.
# Если чисел нет — верни 1.
# Подумай, почему логично вернуть 1, а не 0.

import math


def multiply_all(*nums):
    return math.prod(nums)


print(multiply_all(1, 2, 4))
print(multiply_all())
