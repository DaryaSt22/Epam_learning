# 1.1. Длина списка
# Дан список чисел numbers.
# Напиши код, который:
# выводит длину списка
# выводит первый и последний элемент списка
# Учти, что список может быть пустой — подумай, что в этом случае делать.
from typing import List


def lenght_list(numbers: List):
    # numbers = [1, 2, 6, 8, 10]
    # print(numbers[0])
    # print(numbers[4])
    # return len(numbers)

    print(len(numbers))
    print(numbers[0])
    print(numbers[-1])
    return numbers


lenght_list([1, 5, 9, 10, 55, 9])
