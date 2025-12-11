# 18. Поиск максимума
# Создай функцию my_max(*nums), которая:
# если аргументов нет — возвращает None,
# иначе — максимальное число.
# Потренируй разные вызовы.


def my_max(*nums):
    if nums == ():
        return None
    else:
        return max(nums)

print(my_max(10, 55, 88, 642, 2, 0))
print(my_max())

