# 10. Передача списка в функцию
# Создай функцию print_three(a, b, c), которая печатает три аргумента.
# Создай список nums = [1, 2, 3].
# Задача: подумай, чем отличается вызов:
# print_three(nums[0], nums[1], nums[2])
# print_three(*nums)

def print_three(a, b, c):
    return a, b, c


nums = [1, 2, 3]

print(print_three(nums[0], nums[1], nums[2]))
print(print_three(*nums))
print(print_three(5, 8, 9))
